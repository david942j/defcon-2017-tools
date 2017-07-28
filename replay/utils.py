import json
import sys,os
from pwn import *
import subprocess
from shutil import move
from multiprocessing import *

def tcheck(arg):
    name,binary,in_dir,out_dir = arg

    proc = current_process()
    n = int(proc.name[len('PoolWorker-'):])+8888
    res = json.load(open(in_dir+'/'+name))
    payloads = []
    response = []
    for r in res:
        if len(r['data'])!=0 and r['id'] == 0: payloads.append(r['data'].decode('base64'))
        if len(r['data'])!=0 and r['id'] == 1: response.append(r['data'].decode('base64'))
    
    cmd = './checker bin/'+binary+' -L '+str(n)+' > /tmp/'+proc.name
    p = process(cmd, shell=True)
    
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
    if 'Memory read @' in out:
        pos = out.index('Memory read @')
        data = out[pos:]
        pos = data.index('\n')
        data = data[:pos].split()[-1]
        v = 0
        try:
            v = int(data,16)
        except:
            pass
        if v>=0x4010000 and v<0x4010fff:
            move(in_dir+'/'+name,out_dir+'/touch_flag')
        else:
            move(in_dir+'/'+name,out_dir+'/exception')
    elif 'exception' in out or 'Exception' in out:
        move(in_dir+'/'+name,out_dir+'/exception')
    else:
        move(in_dir+'/'+name,out_dir+'/ok')

def check(binary,in_dirname,out_dirname):
    """
    if len(sys.argv)<3: 
        print 'Usage: %s binary problem_port' %sys.argv[0]
        exit(1)
    """
    #binary = sys.argv[1]
    #port = sys.argv[2]
    #dirname = 'stream/'+str(port)

    if not os.path.exists(os.path.join('bin', binary)):
        print 'Binary bin/%s not exists' % binary
        exit(1)

    if not os.path.exists(in_dirname):
        print 'Dir %s not exists' % in_dirname
        exit(1)

    p = Pool(10)
    p.map(tcheck,[(f,binary,in_dirname,out_dirname) for f in os.listdir(in_dirname)])
