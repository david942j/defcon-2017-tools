import json
import sys,os
from pwn import *
import subprocess
from multiprocessing import *

if len(sys.argv)<3: 
    print 'GG'
    exit(0)

binary = sys.argv[1]
port = sys.argv[2]
dirname = 'stream/'+str(port)

def check(name):
    proc = current_process()
    print proc.name
    print name
    n = int(proc.name[len('PoolWorker-'):])+8888
    res = json.load(open(dirname+'/'+name))
    payloads = []
    response = []
    for r in res:
        if len(r['data'])!=0 and r['id'] == 0: payloads.append(r['data'].decode('base64'))
        if len(r['data'])!=0 and r['id'] == 1: response.append(r['data'].decode('base64'))
    
    cmd = './clemency-emu bin/'+binary+' -L '+str(n)+' > /tmp/'+proc.name
    process = subprocess.Popen(cmd, shell=True)
    
    sleep(0.1)
    r = remote('127.0.0.1',n)
    try:
        for payload in  payloads:
            r.send(payload)
            r.recvrepeat(0.2)
            #print repr(r.recvrepeat(0.2))
    except:
        pass
    #for resp in response: print repr(resp)
    
    out = open('/tmp/'+proc.name).read()
    if 'exception' in out or 'Exception' in out:
        print out
        print '!'
    else:
        print 'ok'

p = Pool(10)
p.map(check,os.listdir(dirname))
