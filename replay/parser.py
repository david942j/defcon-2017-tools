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

class PcapParser(object):
    def __init__(self, filename):
        self.data = self._parse(filename)

    def _parse(self, filename):
        h = defaultdict(list)
        pcap = rdpcap(filename)
        s = pcap.sessions()
        logging.info('Find {} sessions'.format(len(s)))
        for k, v in s.iteritems():
            if 'TCP' not in k: continue
            v = sorted(v, key=lambda x: x.time)
            h[v[0].seq+1].append(v)
            if v[0].ack != 0:
                h[v[0].ack].append(v)
        res = []
        for v in h.values():
            if len(v) != 2:
                continue
            if v[0][0].seq > v[1][0].ack:
                v[0],v[1] = v[1],v[0]
            d = [ (0, x) for x in v[0] ]
            d += [ (1, x) for x in v[1] ]
            d = sorted(d, key=lambda x: x[1].time)
            res.append(d)
        logging.info('Find {} streams'.format(len(res))) 
        return res

    def get_streams(self):
        res = defaultdict(list)
        for i in self.data:
            counter = [0, 0]
            arr = []
            prob_id = None
            for a,b in i:
                val = base64.b64encode(str(b[Raw])) if Raw in b else ''
                arr.append({ 'id': a, 'counter': counter[a], 'timestamp': b.time, 'data': val })
                counter[a] += 1
                if a == 0:
                    prob_id = str(b.getlayer('TCP').dport)
            if prob_id == None:
                continue
            res[prob_id].append(arr)
        return res

def concat_data(arr):
    res = ''
    for i in arr:
        if i['id'] == 1: continue
        res += i['data'].decode('base64')
    return res

def parse(fname):
    basename = os.path.basename(fname).replace('.pcap', '')
    streams = PcapParser(fname).get_streams()
    if not os.path.exists('stream'):
        os.mkdir('stream')
    cwd = os.getcwd()+'/'
    d = {'1974':'prob1', '2525':'prob2', '2001':'prob3', '80':'prob4'}
    for prob_id,arr in streams.iteritems():
        if prob_id not in d:
            continue

        try:
            path = os.path.join('stream', prob_id)
            path2 = os.path.join('json', 'todo')
            path2 = os.path.join(d[prob_id], path2)

            if not os.path.exists(path):
                os.mkdir(path)
            if not os.path.exists(path2):
                os.mkdir(path2)

            fset = set([ i.split('_')[-1] for i in os.listdir(path) ])
            for res in arr:
                data = concat_data(res)
                md5 = hashlib.md5(data).hexdigest()
                outfname = os.path.join(path, basename + '_' + md5 + '.json')
                if (md5 + '.json') in fset:
                    logging.info('Skip %s due to same' % md5)
                    continue
                logging.info('Save Packet Stream: %s' % outfname)
                fset.add(md5 + '.json')
                f = file(outfname, 'w')
                json.dump(res, f)
                outfname2 = os.path.join(path2, basename + '_' + md5 + '.json')
                outfname = cwd+outfname
                outfname2 = cwd+outfname2
                os.symlink(outfname,outfname2)
                #f = file(fname, 'w')
                #json.dump(res, f)
        except:
            logging.warn('Error with %s' % prob_id)

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print 'no input file'
            exit(1)
        logging.info('Parse %s' % sys.argv)
        parse(sys.argv[1])
    except:
        logging.error('Parse %s error' % sys.argv)
