import snap
import re

def Closeness(d, e):
    f = open(d)
    s = f.read()
    s1 = re.split('\n', s)
    G1 = snap.PUNGraph.New()

    a = re.split(' ', s1[0])

    for i in range(0, int(a[0])):
	   G1.AddNode(i)

    for i in range(1, int(a[1]) + 1):
	   b = re.split(' ', s1[i])
	   G1.AddEdge(int(b[0]), int(b[1]))

    CloseCentr = dict()

    for NI in G1.Nodes():
	   CloseCentr[NI.GetId()] = snap.GetClosenessCentr(G1, NI.GetId())
	   # print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

    EdgePara = dict()

    for i in range(1, int(a[1]) +1):
	   c = re.split(' ', s1[i])
	   if CloseCentr[int(c[0])] == 0 and CloseCentr[int(c[1])] == 0:
		  EdgePara[(int(c[0]), int(c[1]))] = 0
		  EdgePara[(int(c[1]), int(c[0]))] = 0
	   else:
		  EdgePara[(int(c[0]), int(c[1]))] = e * CloseCentr[int(c[0])] / (CloseCentr[int(c[0])] + CloseCentr[int(c[1])])
		  EdgePara[(int(c[1]), int(c[0]))] = e * CloseCentr[int(c[1])] / (CloseCentr[int(c[0])] + CloseCentr[int(c[1])])

    return EdgePara