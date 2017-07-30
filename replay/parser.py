import base64
import json
import os
import hashlib
import logging
from scapy.all import *
from collections import defaultdict
from multiprocessing import Pool

logging.basicConfig(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'replay_parser.log'),
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s:%(name)s:%(levelname)s: %(message)s')

d = {'1974':'prob1', '2525':'prob2', '2001':'prob3', '80':'prob4',
        '5050':'prob5','2600':'prob6','7845':'prob7'}
fset = {}

def concat_data(arr):
    res = ''
    for i in arr:
        if i['id'] == 1: continue
        res += i['data'].decode('base64')
    return res

class PcapParser(object):
    def __init__(self, fname):
        self.fname = fname
        self.basename = os.path.basename(fname).replace('.pcap', '')

    def solve(self):
        h = defaultdict(list)
        pcap = rdpcap(self.fname)
        s = pcap.sessions()
        logging.info('Find {} sessions'.format(len(s)))
        for k, v in s.iteritems():
            if 'TCP' not in k: continue
            v = sorted(v, key=lambda x: x.time)
            h[v[0].seq+1].append(v)
            if v[0].ack != 0:
                h[v[0].ack].append(v)
        for v in h.values():
            if len(v) != 2:
                continue
            if v[0][0].seq > v[1][0].ack:
                v[0],v[1] = v[1],v[0]
            dat = [ (0, x) for x in v[0] ]
            dat += [ (1, x) for x in v[1] ]
            dat = sorted(dat, key=lambda x: x[1].time)
            self.gen_stream(dat)

    def gen_data(self, i):
        counter = [0, 0]
        arr = []
        prob_id = None
        for a,b in i:
            val = base64.b64encode(str(b[Raw])) if Raw in b else ''
            arr.append({ 'id': a, 'counter': counter[a], 'timestamp': b.time, 'data': val })
            counter[a] += 1
            if a == 0:
                prob_id = str(b.getlayer('TCP').dport)
            if prob_id != None and prob_id not in d:
                return (None, None)
        if prob_id == None:
            return (None, None)
        return (arr,prob_id)

    def gen_stream(self, i):
        cwd = os.getcwd()+'/'
        res, prob_id = self.gen_data(i)
        if res == None or prob_id == None:
            return
        path = os.path.join('stream', prob_id)
        path2 = os.path.join('json', 'todo')
        path2 = os.path.join(d[prob_id], path2)
        data = concat_data(res)
        md5 = hashlib.md5(data).hexdigest()
        outfname = os.path.join(path, self.basename + '_' + md5 + '.json')
        if (md5 + '.json') in fset[prob_id]:
            logging.info('Skip %s due to same' % md5)
            return
        logging.info('Save Packet Stream: %s' % outfname)
        fset[prob_id].add(md5 + '.json')
        f = file(outfname, 'w')
        json.dump(res, f)
        outfname2 = os.path.join(path2, self.basename + '_' + md5 + '.json')
        outfname = cwd+outfname
        outfname2 = cwd+outfname2
        os.symlink(outfname,outfname2)

def parse(fname):
    if not os.path.exists('stream'):
        os.mkdir('stream')
    for prob_id in d:
        path = os.path.join('stream', prob_id)
        if not os.path.exists(path):
            os.mkdir(path)
        path2 = os.path.join('json', 'todo')
        path2 = os.path.join(d[prob_id], path2)
        if not os.path.exists(path2):
            os.mkdir(path2)
        fset[prob_id] = set([ i.split('_')[-1] for i in os.listdir(path) ])
    PcapParser(fname).solve()

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print 'no input file'
            exit(1)
        logging.info('Parse %s' % sys.argv)
        parse(sys.argv[1])
        logging.info('Parse %s Successed' % sys.argv)
    except:
        logging.error('Parse %s error' % sys.argv)
