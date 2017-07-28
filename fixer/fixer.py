import yaml
import glob
import sys
import emudisasm
import tempfile
import subprocess
import os

from optparse import OptionParser
from pwn import *

def p9(v):
    assert 0 <= v < 512
    return bin(v)[2:].rjust(9, '0')

def endi(bits):
    assert len(bits) % 9 == 0
    arr = group(9, bits)
    if len(arr) >= 2:
        a, b = arr[0:2]
        arr[0], arr[1] = b, a

    if len(arr) >= 5:
        a, b = arr[3:5]
        arr[3], arr[4] = b, a

    return ''.join(arr)

def regid(reg):
    return bin(reg)[2:].rjust(5, '0')

def mh(reg, imm):
    return endi('10001' + regid(reg) + bin(imm)[2:].rjust(17, '0'))

def ml(reg, imm):
    return endi('10010' + regid(reg) + bin(imm)[2:].rjust(17, '0'))

def bra(imm):
    return endi('111000100' + bin(imm)[2:].rjust(27, '0'))

def smp(rega, regb, prot):
    return endi('1010010' + regid(rega) + regid(regb) + '1' + bin(prot)[2:].rjust(2, '0') + '0' * 7)

def sbi(rega, regb, imm):
    return endi('0000100' + regid(rega) + regid(regb) + bin(imm)[2:].rjust(7, '0') + '011')

def cmi(rega, imm):
    return endi('10111001' + regid(rega) + bin(imm)[2:].rjust(14, '0'))

def bn(offset):
    return endi('110000' + '0000' + bin(offset)[2:].rjust(17, '0'))

def sts(rega, regb, offset):
    return endi('1011000' + regid(rega) + regid(regb) + '0' * 5 + '00' + bin(offset)[2:].rjust(27, '0') + '000')

def lds(rega, regb, offset):
    return endi('1010100' + regid(rega) + regid(regb) + '0' * 5 + '00' + bin(offset)[2:].rjust(27, '0') + '000')

def mov(rega, imm):
    return ml(rega, imm & ((1<<17) - 1)) + mh(rega, (imm>>10))

parser = OptionParser(usage="usage: %prog --dir DIR --bin BIN")
parser.add_option("-b", "--bin", dest="bin",
                  help="firmware file name", metavar="BIN")
parser.add_option("-d", "--dir", dest="dir", default='.', metavar="DIR",
                  help="directory that includes patches.yml (see sample/)")
parser.add_option("-o", "--output", metavar="FILE", dest="output", help="output filename, default is <bin>.patch")
(options, args) = parser.parse_args()

def collect_patches(setting, dir):
    patches = []
    for item in setting['targets']:
        config = item.values()[0]
        assert config['start'] != None
        assert config['asmfile'] != None
        config['asmfile'] = os.path.join(dir, config['asmfile'])
        print("Patch '{}' to 0x{:x}".format(config['asmfile'], config['start']))
        patches.append(config)
    return patches

# return bit stream
def load_bin(file):
    with open(file, 'rb') as infile:
        indata = infile.read()
    data = ''.join(bin(ord(d))[2:].rjust(8, '0') for d in indata)
    return data[0:len(data) - (len(data) % 9)]

def get_oribytelen(address, minlen):
    data = emudisasm.parse_function(os.path.realpath(options.bin), address)
    addresses = list(int(line.split(':')[0], 16) for line in data.split('\n'))
    bytelen = None
    for addr in addresses:
        if addr >= address + minlen:
            bytelen = addr - address
            break

    assert bytelen is not None
    return bytelen

def get_first_inst_len(address):
    return get_oribytelen(address, 1)

def do_inline(base_address, append_bits):
    base_bddress = base_address * 9
    bits[base_bddress:base_bddress + len(append_bits)] = append_bits
    return bits

def do_setup(base_address, append_bits, setup_address=0x3c, pages=1):
    '''
    We don't preserve R00 !!!!
    1. patch entry point (0x0) to extend whole binary size (additional page in the end)
        * therefore, DO NOT patch bin[0:0x12]
    2. collect and append patches to the additional page
    3. hook each `start'  to jmp to correspond address
    '''
    global bits

    setup_bddress = setup_address * 9

    # Align
    bits = bits + '0' * (1024 * 9 - (len(bits) % (1024 * 9)))

    offset = len(bits) // 9
    oribytelen = get_oribytelen(setup_address, 0x11)

    bits += append_bits

    # Clean
    stage2 = ''
    stage2 += mov(20, offset) + smp(20, 26, 2)
    stage2 += ml(20, pages * 1024) + ml(21, 0) + sts(21, 20, offset - 1) + sbi(20, 20, 1) + bn((-9) & ((1<<17) - 1))
    # Recover
    stage2 += bits[setup_bddress:setup_bddress + oribytelen * 9] + bra(setup_address + oribytelen)

    bits += stage2

    stage2_address = base_address + len(append_bits) // 9
    patchlen = (len(append_bits) + len(stage2)) // 9
    patchend = len(bits) // 9

    # Copy
    bits += mov(20, base_address) + smp(20, 26, 2)
    bits += ml(20, patchlen) + lds(21, 20, offset - 1) + sts(21, 20, base_address - 1) + sbi(20, 20, 1) + bn((-15) & ((1<<17) - 1))
    bits += mov(20, base_address) + smp(20, 26, 3)

    # Jump second stage
    bits += bra(stage2_address)

    # Check appended size
    assert (len(bits) - offset * 9) < pages * 1024 * 9

    payload = mov(20, offset) + ml(26, 1) + smp(20, 26, 3) + bra(patchend)
    assert oribytelen * 9 >= len(payload)
    # Assume old code is PIE
    bits[setup_bddress:setup_bddress + len(payload)] = payload
    assert len(bits) % 9 == 0
    return bits

def gen_back(address, oribytelen):
    # Assume old code is PIE
    bddress = address * 9
    oribits = bytes(bits[bddress:bddress + oribytelen * 9])
    return oribits + bra(address + oribytelen)

def cwd():
    return os.path.dirname(os.path.realpath(__file__))

def preprocess(asmname, back_address, skip_address):
    asmdata = open(asmname, 'r').read()
    asmdata = asmdata.replace('BACK', 'bra {}'.format(back_address))
    asmdata = asmdata.replace('SKIP', 'bra {}'.format(skip_address))
    inf = tempfile.NamedTemporaryFile()
    inf.write(asmdata)
    inf.flush()
    inf.seek(0)
    outf = tempfile.NamedTemporaryFile()
    subprocess.check_output(['ruby', cwd() + '/../assembler/asm.rb', inf.name, outf.name])
    outf.seek(0)
    return load_bin(outf.name)

def gen_patches(base_address, patches):
    append_bits = ''
    back_offsets = []
    skip_offsets = []
    patch_offsets = []
    for patch in patches:
        start = patch['start']
        back_gadget_offset = len(append_bits) // 9
        back_offsets.append(back_gadget_offset)
        skip_offsets.append(back_gadget_offset + get_first_inst_len(start))
        append_bits += gen_back(start, get_oribytelen(start, 4))

    # Preprocessing
    for back_offset, skip_offset, patch in zip(back_offsets, skip_offsets, patches):
        patch_offsets.append(len(append_bits) // 9)
        append_bits += preprocess(patch['asmfile'], back_offset + base_address, skip_offset + base_address)

    return append_bits, patch_offsets

def do_hooks(base_address, patches, patch_offsets):
    for patch, offset in zip(patches, patch_offsets):
        address = patch['start']
        bddress = address * 9
        bits[bddress:bddress + 4 * 9] = bra(offset + base_address)

def load_setting(dir):
    files = glob.glob(os.path.join(dir, 'patches.yml'))
    assert len(files) == 1
    file = files[0]
    return yaml.safe_load(open(file, 'rb').read())

setting = load_setting(options.dir)
patches = collect_patches(setting, options.dir)
bits = bytearray(load_bin(options.bin))
base_address = setting['base_address']

mode = setting['mode']

append_bits, patch_offsets = gen_patches(base_address, patches)

do_hooks(base_address, patches, patch_offsets)

if mode == 'append':
    setup_address = setting['append']['setup_address']
    patched_bits = bytes(do_setup(base_address, append_bits, setup_address))
elif mode == 'inline':
    patched_bits = bytes(do_inline(base_address, append_bits))

output = options.output or (options.bin + '.patch')
print('\nPatched file: ' + output)
open(output, 'wb').write(''.join(chr(int(x, 2)) for x in group(8, patched_bits, 'fill', '0')))
