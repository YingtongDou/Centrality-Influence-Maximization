''' Implements greedy heuristic for IC model [1]

[1] -- Wei Chen et al. Efficient Influence Maximization in Social Networks (Algorithm 2)
'''
from __future__ import division
from copy import deepcopy # copy graph object
import random
from priorityQueue import PriorityQueue as PQ
import networkx as nx
from runIAC import avgIAC
import matplotlib.pyplot as plt
import time


def findCCs(G, Ep):
    # remove blocked edges from graph G
    E = deepcopy(G)
    edge_rem = [e for e in E.edges() if random.random() < (1-Ep)]
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

def newGreedyIC (G, k, Ep, R = 200):

    S = []
    for i in range(k):
        # print i
        time2k = time.time()
        scores = {v: 0 for v in G}
        for j in range(R):
            # print j,
            CCs = findCCs(G, Ep)
            # print CCs
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
        # print scores
        max_v, max_score = max(scores.iteritems(), key = lambda (dk, dv): dv)
        S.append(max_v)
        # print S
        # print time.time() - time2k
    return S