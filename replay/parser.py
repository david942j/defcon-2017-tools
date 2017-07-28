import base64
import json
import os
import hashlib
from scapy.all import *
from collections import defaultdict
from multiprocessing import Pool

class PcapParser(object):
    def __init__(self, filename):
        self.data = self._parse(filename)

    def _parse(self, filename):
        h = defaultdict(list)
        pcap = rdpcap(filename)
        s = pcap.sessions()
        for k, v in s.iteritems():
            v = sorted(v, key=lambda x: x.time)
            h[v[0].seq+1].append(v)
            if v[0].ack != 0:
                h[v[0].ack].append(v)
        res = []
        for v in h.values():
            if len(v) != 2:
                continue
            d = [ (0, x) for x in v[0] ]
            d += [ (1, x) for x in v[1] ]
            d = sorted(d, key=lambda x: x[1].time)
            res.append(d)
        return res

    def get_streams(self):
        res = defaultdict(list)
        for i in self.data:
            counter = [0, 0]
            arr = []
            for a,b in i:
                val = base64.b64encode(str(b[Raw])) if Raw in b else ''
                arr.append({ 'id': a, 'counter': counter[a], 'timestamp': b.time, 'data': val })
                counter[a] += 1
            prob_id = str(i[1][1].getlayer('TCP').sport)
            res[prob_id].append(arr)
        return res

def parse(fname):
    streams = PcapParser(fname).get_streams()
    if not os.path.exists('stream'):
        os.mkdir('stream')
    cwd = os.getcwd()+'/'
    for prob_id,arr in streams.iteritems():
        path = os.path.join('stream', prob_id)
        path2 = os.path.join('json', 'todo')
        if not os.path.exists(path):
            os.mkdir(path)
        for res in arr:
            md5 = hashlib.md5(json.dumps(res)).hexdigest()
            fname = os.path.join(path, md5 + '.json')
            print 'Save Packet Stream:',fname
            f = file(fname, 'w')
            json.dump(res, f)
            fname2 = os.path.join(path2, md5 + '.json')
            fname = cwd+fname
            fname2 = cwd+fname2
            os.symlink(fname,fname2)
            #f = file(fname, 'w')
            #json.dump(res, f)

if __name__ == '__main__':
    fdir = 'pcap'
    if len(sys.argv) >= 2:
        fdir = sys.argv[1]
    flist = [fdir+'/'+name for name in os.listdir(fdir)]
    p = Pool(10)
    p.map(parse,flist)
