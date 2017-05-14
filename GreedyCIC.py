from __future__ import division
from copy import deepcopy
import random
from priorityQueue import PriorityQueue as PQ
import networkx as nx
from runIAC import avgIAC
from PageRankCentr import PageRank
from ClosenessCentr import Closeness
from DegreeCentr import Degree
from EccentricCentr import Eccentric


def findCCs(G, Ep):
    # remove blocked edges from graph G
    E = deepcopy(G)
    edge_rem = [e for e in E.edges() if random.random() < (1-Ep[e[0], e[1]])]
    E.remove_edges_from(edge_rem)

    # initialize CC
    CCs = dict() # each component is reflection of the number of a component to its members
    explored = dict(zip(E.nodes(), [False]*len(E)))
    c = -1
    # perform BFS to discover CC
    for node in E:
        if not explored[node]:
            c += 1
            explored[node] = True
            CCs[c] = [node]
            component = E[node].keys()
            for neighbor in component:
                if not explored[neighbor]:
                    explored[neighbor] = True
                    CCs[c].append(neighbor)
                    component.extend(E[neighbor].keys())
    return CCs

def GreedyCIC (G, k, Ep, R = 200):

    S = []
    for i in range(k):
        print i
        # time2k = time.time()
        scores = {v: 0 for v in G}
        for j in range(R):
            # print j,
            CCs = findCCs(G, Ep)
            for CC in CCs:
                for v in S:
                    if v == (CC):
                        break
                else: # in case CC doesn't have node from S
                    scores[CC] += len(CCs[CC])
        for v in G.node:
            if v in S:
                ba = 0
            else:
                scores[v] = float(scores[v])/R
        max_v, max_score = max(scores.iteritems(), key = lambda (dk, dv): dv)
        S.append(max_v)
        # print time.time() - time2k
    return S

if __name__ == "__main__":
    import time
    start = time.time()

    G = nx.read_gpickle("Graph/MIT.gpickle")
    print 'Read graph G'
    print time.time() - start

    d = "Graphdata/MIT.txt"

    EdgePara = Eccentric(d, 0.1)

    S = GreedyCIC(G, 10, EdgePara)
    print S