import snap
import re

def PageRank(d, e):
    f = open(d)
    s = f.read()
    s1 = re.split('\n', s)
    G1 = snap.PNGraph.New() 
    PRankH = snap.TIntFltH()

    a = re.split(' ', s1[0])

    for i in range(0, int(a[0])):
	   G1.AddNode(i)

    for i in range(1, int(a[1]) + 1):
	   b = re.split(' ', s1[i])
	   b0 = re.sub("\D", "", b[0])
	   b1 = re.sub("\D", "", b[1])
	   G1.AddEdge(int(b0), int(b1))

    snap.GetPageRank(G1, PRankH)


    EdgePara = dict()

    for i in range(1, int(a[1]) +1):
	   c = re.split(' ', s1[i])
	   if PRankH[int(c[0])] == 0 and PRankH[int(c[1])] ==0:
		  EdgePara[(int(c[0]), int(c[1]))] == 0
		  EdgePara[(int(c[1]), int(c[0]))] == 0
	   else:
		  EdgePara[(int(c[0]), int(c[1]))] = e * PRankH[int(c[0])] / (PRankH[int(c[0])] + PRankH[int(c[1])])
		  EdgePara[(int(c[1]), int(c[0]))] = e * PRankH[int(c[1])] / (PRankH[int(c[0])] + PRankH[int(c[1])])

    return EdgePara      