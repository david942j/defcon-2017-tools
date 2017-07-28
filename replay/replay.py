import json
import sys,os
from pwn import *
import subprocess

if len(sys.argv)<3: 
    print 'GG'
    exit(0)

binary = sys.argv[1]
port = sys.argv[2]
dirname = 'stream/'+str(port)


for j in os.listdir(dirname):
    res = json.load(open(dirname+'/'+j))
    payloads = []
    response = []
    for r in res:
        if len(r['data'])!=0 and r['id'] == 0: payloads.append(r['data'].decode('base64'))
        if len(r['data'])!=0 and r['id'] == 1: response.append(r['data'].decode('base64'))
    if os.fork() > 0:
        cmd = 'timeout 3 ./clemency-emu bin/'+binary+' -l 8888 > /tmp/a'
        os.system(cmd)
        out = open('/tmp/a').read()
        if 'exception' in out or 'Exception' in out:
            print out
            print '!'
        else:
            print 'ok'
    else: 
        sleep(0.1)
        r = remote('127.0.0.1',8888)
        for payload in  payloads:
            r.send(payload)
            print repr(r.recvrepeat(0.2))
        #for resp in response: print repr(resp)
        exit(1)
