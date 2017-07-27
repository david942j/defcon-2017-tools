import base64
import json
from scapy.all import *
from collections import defaultdict

class PcapParser(object):
    def __init__(self, filename):
        self.data = self._parse(filename)

    def _parse(self, filename):
        h = defaultdict(list)
        pcap = rdpcap(filename)
        s = pcap.sessions()
        for k, v in s.iteritems():
            if v[0].ack == 0:
                h[v[0].seq+1].append(v)
            else:
                h[v[0].ack].append(v)
        res = []
        for v in h.values():
            d = [ (0, x) for x in v[0] ]
            d += [ (1, x) for x in v[1] ]
            d = sorted(d, key=lambda x: x[1].time)
            res.append(d)
        return res

    def get_streams(self):
        return self.data

if __name__ == '__main__':
    streams = PcapParser('hello.pcap').get_streams()
    for i in streams:
        counter = [0, 0]
        res = []
        for a,b in i:
            val = base64.b64encode(str(b[Raw])) if Raw in b else ''
            res.append({ 'id': a, 'counter': counter[a], 'timestamp': b.time, 'data': val })
            counter[a] += 1
        fname = 'pcap_' + str(i[1][1].getlayer('TCP').sport) + '_' + str(int(i[1][1].time)) + '.json'
        fname = os.path.join('stream', fname)
        print 'Save Packet Stream:',fname
        f = file(fname, 'w')
        json.dump(res, f)
