import os
import time

port = 1974


while True:
    binlist = os.listdir('/tmp2/alpha/'+str(port))
    print binlist
    flist = os.listdir('cache')
    print flist
    for b in binlist:
        if b not in flist:
            print b
            os.system('cp /tmp2/alpha/'+str(port)+'/'+b+' cache')
            os.system('python new_binary.py cache/'+b)
    time.sleep(300)
