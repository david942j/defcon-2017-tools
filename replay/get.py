import glob,time,os
import shutil


while True:
    pcap = glob.glob('/home/public/pcap/*.pcap')
    print pcap
    flist = os.listdir('pcap')
    print flist
    for p in pcap:
        if 'latest' in p: continue
        if '07-29-00:53:06' in p: continue
        pp = os.path.basename(p)
        if pp not in flist:
            os.system('cp '+p+' pcap')
            os.system('python parser.py pcap/'+pp)
    time.sleep(250)
