#!/usr/bin/env python

from pwn import *
import sys

if len(sys.argv) != 2:
    print "%s <input_file>" % sys.argv[0]
    sys.exit(1)

fn = sys.argv[1]
b = open(fn).read()

bit = ''.join(['{:08b}'.format(ord(x)) for x in b])
out = ''.join([p16(int(x.rjust(16, "0"), 2)) for x in group(9, bit)])


if fn.rfind('.') != -1:
    fn = fn[:fn.rfind(".")]
open(fn + ".t.bin", 'wb').write(out)
