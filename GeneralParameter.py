import snap
import re

def General(d, e):
    f = open(d)
    s = f.read()
    s1 = re.split('\n', s)
    G1 = snap.PNGraph.New() 

    a = re.split(' ', s1[0])

    for i in range(0, int(a[0])):
	   G1.AddNode(i)

    for i in range(1, int(a[1]) + 1):
	   b = re.split(' ', s1[i])
	   G1.AddEdge(int(b[0]), int(b[1]))

    EdgePara = dict()

    for i in range(1, int(a[1]) +1):

		c = re.split(' ', s1[i])
		EdgePara[(int(c[0]), int(c[1]))] = e
		EdgePara[(int(c[1]), int(c[0]))] = e

    return EdgePara      