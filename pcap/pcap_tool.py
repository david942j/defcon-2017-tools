#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess as sp
from pwn import *
import re
import sys
import os
import tempfile
import argparse

def to_8bit(d9):
    bits = ''
    for c in d9:
        bits += bin(ord(c))[2:].rjust(8, '0')
    log.debug(bits)
    d8 = ''
    for i in range(0, len(bits), 9):
        tmp = bits[i:i+9]
        tmp = tmp if len(tmp) == 9 else tmp.ljust(9, '0')
        log.debug('%s : %s' % (tmp, hex(int(tmp, 2))))
        d8 += chr(int(tmp, 2))
    d8 = d8.strip('\x00')
    return d8

def dump_io(pcap, cid, split=False):
    fol = []

    p = sp.Popen('tshark -r %s -z follow,tcp,raw,%d' % (pcap, cid), shell=True, stdout=sp.PIPE)
    o = p.stdout.read()
    o = o[o.find('========'):].strip('=\n')
    o = '\n'.join(o.split('\n')[4:]).strip()
    if len(o) == 0:
        return None

    if split:
        for l in o.split('\n'):
            if re.search('^\t', l):
                fol.append('out: ' + l[1:].decode('hex'))
            else:
                fol.append('in : ' + l.decode('hex'))

        return fol
    else:
        for l in o.split('\n'):
            if re.search('^\t', l):
                log.debug((l[1:]))
                fol.append('out: ' + to_8bit(l[1:].decode('hex')))
            else:
                fol.append('in : ' + to_8bit(l.decode('hex')))

        result = ''
        for _ in fol:
            result += _ + '\n'
        return result

def dump(pcap, cid):
    if cid != None:
        result = dump_io(pcap, cid)
        if result:
            sys.stdout.write(result)
        else:
            log.warning('No data')
    else:
        p = sp.Popen('tshark -r %s -z conv,tcp | grep "<->" | wc -l' % pcap, shell=True, stdout=sp.PIPE)
        count = int(p.stdout.read())
        log.debug('tcp conversion: %d' % count)
        for i in xrange(count):
            log.info('%s conversation %d' % (pcap, i))
            result = dump_io(pcap, i)
            log.info(result)


def search(pcap, pattern, is_hex):
    p = sp.Popen('tshark -r %s -z conv,tcp | grep "<->" | wc -l' % pcap, shell=True, stdout=sp.PIPE)
    count = int(p.stdout.read())
    log.debug('tcp conversion: %d' % count)

    data = pattern if not is_hex else pattern.decode('hex')

    for i in xrange(count):
        result = dump_io(pcap, i)
        if data in result:
            log.info('Find in %s conversation %d' % (pcap, i))
            log.info(result)
        else:
            log.warning('Not found')

def batch(in_f, out_f):
    if not out_f:
        out_f = tempfile.mkdtemp()
    pcaps = sp.Popen('ls %s/*.pcap' % in_f, shell=True, stdout=sp.PIPE).stdout.read().split()
    for pcap in pcaps:
        out_dir = '%s/%s' % (out_f, pcap.split('/')[-1])
        log.info('Dump to %s ...' % out_dir)
        os.mkdir(out_dir)
        count = int(sp.Popen('tshark -r %s -z conv,tcp | grep "<->" | wc -l' % pcap, shell=True, stdout=sp.PIPE).stdout.read())
        for i in xrange(count):
            with open('%s/%d' % (out_dir, i), 'w') as f:
                f.write(dump_io(i))

def replay(pcap, cid, host, port):
    r = remote(host, port)
    for st in dump_io(pcap, cid, split=True):
        direct = st.split(':')[0].strip()
        data = ':'.join(st.split(':')[1:]).strip()
        if 'in' in direct:
            r.send(data)
        elif 'out' in direct:
            if len(data) > 0:
                data = r.recv()
                log.info(to_8bit(data))
        else:
            log.error('error happend')

    r.close()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='avaiable subcommands')

parser_search = subparsers.add_parser('search', help='tranfer pattern to 9 bit data and search in pcap')
parser_search.add_argument('pcap', type=str, help='search target')
parser_search.add_argument('pattern', type=str, help='search pattern')
parser_search.add_argument('--hex', action='store_true', help='search hex pattern')
parser_search.set_defaults(func=search)

parser_dump = subparsers.add_parser('dump', help='dump pcap to 8 bit data.')
parser_dump.add_argument('pcap', type=str, help='dump target')
parser_dump.add_argument('cid', type=int, help='tcp conversation id', nargs='?')
parser_dump.set_defaults(func=dump)

parser_batch = subparsers.add_parser('batch', help='batch dump pcap to 8 bit data.')
parser_batch.add_argument('indir', type=str, help='input pcap folder')
parser_batch.add_argument('outdir', type=str, help='output data folder', nargs='?')
parser_batch.set_defaults(func=batch)

parser_replay = subparsers.add_parser('replay', help='replay pcap data')
parser_replay.add_argument('pcap', type=str, help='replay target')
parser_replay.add_argument('cid', type=int, help='tcp conversation id')
parser_replay.add_argument('host', type=str, help='replay target host')
parser_replay.add_argument('port', type=str, help='replay target port')
parser_replay.set_defaults(func=replay)

args = parser.parse_args()

if args.func == batch:
    args.func(args.indir, args.outdir)
elif args.func == dump:
    args.func(args.pcap, args.cid)
elif args.func == search:
    args.func(args.pcap, args.pattern, args.hex)
elif args.func == replay:
    args.func(args.pcap, args.cid, args.host, args.port)
