from priorityQueue import PriorityQueue as PQ # priority queue
import networkx as nx
from PageRankCentr import PageRank
from ClosenessCentr import Closeness
from DegreeCentr import Degree
from EccentricCentr import Eccentric

def NewDiscount(G, k, p):

    S = []
    dd = PQ() # degree discount
    t = dict() # number of adjacent vertices that are in S
    d = dict() # degree of each vertex

    # initialize degree discount
    for u in G.nodes():
        d[u] = sum([G[u][v]['weight'] for v in G[u]]) # each edge adds degree 1
        d[u] = len(G[u]) # each neighbor adds degree 1
        dd.add_task(u, -d[u]) # add degree of each node
        t[u] = 0

    # add vertices to S greedily
    for i in range(k):
        u, priority = dd.pop_item() # extract node with maximal degree discount
        S.append(u)
        for v in G[u]:
            if v not in S:
                t[v] += G[u][v]['weight'] # increase number of selected neighbors
                priority = d[v] - 2*t[v] - (d[v] - t[v])*t[v]*p[u, v] # discount of degree
                dd.add_task(v, -priority)
    return S

if __name__ == "__main__":
    import time
    start = time.time()

    G = nx.read_gpickle("Graph/retweet.gpickle")
    print 'Read graph G'
    print time.time() - start

    d = "Graphdata/retweet.txt"

    EdgePara = Degree(d, 1)

    S = NewDiscount(G, 20, EdgePara)
    print S
    print time.time() - start

