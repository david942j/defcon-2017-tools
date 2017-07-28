import json
import sys,os
from pwn import *
import subprocess
from multiprocessing import *

if len(sys.argv)<3: 
    print 'Usage: %s binary problem_prot' %sys.argv[0]
    exit(1)

binary = sys.argv[1]
port = sys.argv[2]
dirname = 'stream/'+str(port)

if not os.path.exists(os.path.join('bin', binary)):
    print 'Binary bin/%s not exists' % binary
    exit(1)

if not os.path.exists(dirname):
    print 'Dir %s not exists' % dirname
    exit(1)

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
    
    cmd = './clemency-emu-no-access-flag bin/'+binary+' -L '+str(n)+' -d 0 > /tmp/'+proc.name
    p = process(cmd, shell=True)
    p.sendline('g')
    p.sendline('q')
    
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
    
    p.close()
    out = open('/tmp/'+proc.name).read()
    if 'exception' in out or 'Exception' in out:
        flag = False
        for i in range(1000):
            s = '4010%0x' % i
            if s in out:
                print 'Find %s' % s
                flag = True
                break
        if flag:
            print 'leak flag'
        else:
            print 'crash'
    else:
        print 'ok'

p = Pool(2)
p.map(check,os.listdir(dirname))
