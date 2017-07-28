from pwn import *
import json
import base64
import sys

if len(sys.argv) <= 3:
    print 'Usage: %s host port json' % (sys.argv[0])
    exit()

def from9(s):
    b = ''.join([bin(ord(c))[2:].rjust(8, '0') for c in s])
    p = ''
    for i in range(len(b)/9):
        p += chr(int(b[i*9:(i+1)*9], 2))
    return p
    #return ''.join([chr(int(c, 2)) for c in group(9, b)])

host = sys.argv[1]
port = int(sys.argv[2])
arr = json.loads(open(sys.argv[3]).read())
r = remote(host, port)
#print arr
cur_t = 0
prev_t = 0

for idx, p in enumerate(arr):
    cur_t = p['timestamp']
    if idx != 0:
        time.sleep(cur_t-prev_t)
    prev_t = cur_t
    if len(p['data']) == 0:
        continue
    if p['id'] == 0:
        s1 = base64.b64decode(p['data'])
        #print s1
        r.send(s1)
    else:
        s2 = r.recv(4096)
        print from9(s2)

