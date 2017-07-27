import sys
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

patchbits = endi('101000000011000000')
oribitlen = 0x12

with open(sys.argv[1], 'rb') as infile:
    indata = infile.read()
    bits = ''.join(bin(ord(d))[2:].rjust(8, '0') for d in indata)
    bits = bits + '0' * (1024 * 9 - (len(bits) % (1024 * 9)))
    offset = len(bits) / 9
    bits += patchbits
    patchend = len(bits) / 9
    bits += ml(0, 0) + ml(1, 0) + bits[0:oribitlen * 9] + bra(oribitlen)
    assert len(bits) < 1024 * 9

    payload = ml(0, offset & ((1<<17) - 1)) + mh(0, (offset>>10)) + ml(1, 1) + smp(0, 1, 3) + bra(patchend)
    assert oribitlen * 9 >= len(payload)

    # Assume old code is PIE
    bits = bytearray(bits)
    bits[0:len(payload)] = payload
    bits = bytes(bits)
    assert len(bits) % 9 == 0
    open(sys.argv[1] + '.patch', 'wb').write(''.join(chr(int(x, 2)) for x in group(8, bits, 'fill', '0')))
