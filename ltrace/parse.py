#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

i = 1
for l in open(sys.argv[1]):
    t = l.split()
    if len(t) == 2:
        print "%d: %s @ %07X 0" % (i, t[1], int(t[0],16) )
    i += 1
