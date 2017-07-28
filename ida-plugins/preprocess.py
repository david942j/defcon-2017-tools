#!/usr/bin/env python

from pwn import *
import sys

if len(sys.argv) != 2:
    print "./t.py input_file"
    sys.exit(1)

b = open(sys.argv[1]).read()

bit = ''.join(['{:08b}'.format(ord(x)) for x in b])
out = ''.join([p16(int(x.rjust(16, "0"), 2)) for x in group(9, bit)])

open(sys.argv[1] + ".t.bin", 'wb').write(out)
