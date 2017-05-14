# if "__name__" == "__main__":

import snap
import re


f = open("Graphdata/retweet.txt")
s = f.read()
s1 = re.split('\n', s)
G1 = snap.PUNGraph.New()

a = re.split(' ', s1[0])

for i in range(0, int(a[0])):
	G1.AddNode(i)

for i in range(1, int(a[1]) + 1):
	b = re.split(' ', s1[i])
	G1.AddEdge(int(b[0]), int(b[1]))

DegCentr = dict()

for NI in G1.Nodes():
	DegCentr[NI.GetId()] = snap.GetDegreeCentr(G1, NI.GetId())
	# print "node: %d centrality: %f" % (NI.GetId(), DegCentr)

# print DegCentr[15232]
EdgePara = dict()

for i in range(1, int(a[1]) +1):
	c = re.split(' ', s1[i])
	EdgePara[(int(c[0]), int(c[1]))] = DegCentr[int(c[0])] / (DegCentr[int(c[0])] + DegCentr[int(c[1])])
	EdgePara[(int(c[1]), int(c[0]))] = DegCentr[int(c[1])] / (DegCentr[int(c[0])] + DegCentr[int(c[1])])

snap.DrawGViz(G1, snap.gvlNeato, "graph_undirected.png", "graph 2", True)