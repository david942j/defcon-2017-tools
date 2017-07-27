import yaml
import glob
import sys

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
        a, b = arr[3:4]
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

oribitlen = 0x12

parser = OptionParser(usage="usage: %prog --dir DIR --bin BIN")
parser.add_option("-b", "--bin", dest="bin",
                  help="firmware file name", metavar="BIN")
parser.add_option("-d", "--dir", dest="dir", default='.', metavar="DIR",
                  help="directory includes patch files (see sample/)")
parser.add_option("-o", "--output", metavar="FILE", dest="output", help="output filename, default is <bin>.patch")
(options, args) = parser.parse_args()

def collect_patches(dir):
    files = glob.glob(os.path.join(dir, '*.yml'))
    assert len(files) > 0
    patches = []
    for file in files:
        config = yaml.safe_load(open(file, 'rb').read())
        assert config['start'] != None
        if config.get('bits'):
            bits = config['bits']
        elif config.get('asmfile'):
            # TODO
            raise
        else:
            raise 'Either "bits" or "asmfile" should present'
        patches.append({'start': config['start'], 'bits': bits})
    return patches
    
# return bit stream
def load_bin(file):
    with open(file, 'rb') as infile:
        indata = infile.read()
    return ''.join(bin(ord(d))[2:].rjust(8, '0') for d in indata)

def do_patch(bits, patches):
    '''
    1. patch entry point (0x0) to extend whole binary size (additional page in the end)
        * therefore, DO NOT patch bin[0:0x12]
    2. collect and append patches to the additional page
    3. hook each `start'  to jmp to correspond address
    '''
    # TODO: consider multiple patches
    patchbits = patches[0]['bits']
    st = patches[0]['start']

    bits = bits + '0' * (1024 * 9 - (len(bits) % (1024 * 9)))
    offset = len(bits) / 9
    bits += patchbits
    patchend = len(bits) / 9
    bits += ml(0, 0) + ml(1, 0) + bits[st:st + oribitlen * 9] + bra(oribitlen)
    assert len(patchbits) < 1024 * 9

    payload = ml(0, offset & ((1<<17) - 1)) + mh(0, (offset>>10)) + ml(1, 1) + smp(0, 1, 3) + bra(patchend)
    assert oribitlen * 9 >= len(payload)

    # Assume old code is PIE
    bits = bytearray(bits)
    bits[st:st+len(payload)] = payload
    bits = bytes(bits)
    assert len(bits) % 9 == 0
    return bits

patches = collect_patches(options.dir)
bits = load_bin(options.bin)
patched_bits = do_patch(bits, patches)

output = options.output or (options.bin + '.patch')

open(output, 'wb').write(''.join(chr(int(x, 2)) for x in group(8, patched_bits, 'fill', '0')))
