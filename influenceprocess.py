import networkx as nx
import random
from PageRankCentr import PageRank
from ClosenessCentr import Closeness
from DegreeCentr import Degree
from EccentricCentr import Eccentric
from NewDiscount import NewDiscount
from GreedyCIC import GreedyCIC
from degreeDiscount import degreeDiscountIC
from GeneralParameter import General
from newGreedyIC import newGreedyIC

def influence(G, S, Ep):
	F = []

	F += S

	for s in S:
		for i in range(0, len(G.neighbors(s))):
			if G.neighbors(s)[i] not in F:	
				if random.random() > (1 - Ep[s, G.neighbors(s)[i]]):
					F.append(G.neighbors(s)[i])
				else:
					continue
	return F

if __name__ == "__main__":
	G = nx.read_gpickle("Graph/MIT.gpickle")
	d = "Graphdata/MIT.txt"

	EdgePara1 = Degree(d, 0.1)
	# EdgePara2 = PageRank(d, 0.01)
	# EdgePara3 = Eccentric(d, 0.01)
	# EdgePara4 = Closeness(d, 0.01)
	# EdgePara = General(d, 1)
	S1 = NewDiscount(G, 10, EdgePara1)
	# S2 = NewDiscount(G, 10, EdgePara2)
	# S3 = NewDiscount(G, 10, EdgePara3)
	# S4 = NewDiscount(G, 10, EdgePara4)
	# S5 = degreeDiscountIC(G, 10, 1)
	# S6 = newGreedyIC(G, 10, 1)
	# S7 = GreedyCIC(G, 10, EdgePara1)
	# S8 = GreedyCIC(G, 10, EdgePara2)
	# S9 = GreedyCIC(G, 10, EdgePara3)
	# S10 = GreedyCIC(G, 10, EdgePara4)


	F1 = []
	F2 = []
	F3 = []
	F4 = []
	F5 = []
	F6 = []
	F7 = []
	F8 = []
	F9 = []
	F10 = []

	for i in range(0, 1000):
		F = influence(G, S1, EdgePara1)
		F1.append(len(F))
	print float(sum(F1)/len(F1))

	# for i in range(0, 1000):
	# 	F = influence(G, S2, EdgePara2)
	# 	F2.append(len(F))
	# print float(sum(F2)/len(F2))

	# for i in range(0, 1000):
	# 	F = influence(G, S3, EdgePara3)
	# 	F3.append(len(F))
	# print float(sum(F3)/len(F3))

	# for i in range(0, 1000):
	# 	F = influence(G, S4, EdgePara4)
	# 	F4.append(len(F))
	# print float(sum(F4)/len(F4))
	
	# for i in range(0, 1000):
	# 	F = influence(G, S5, EdgePara)
	# 	F5.append(len(F))
	# print float(sum(F5)/len(F5))

	# for i in range(0, 1000):
	# 	F = influence(G, S6, EdgePara)
	# 	F6.append(len(F))
	# print float(sum(F6)/len(F6))

	# for i in range(0, 1000):
	# 	F = influence(G, S7, EdgePara1)
	# 	F7.append(len(F))
	# print float(sum(F7)/len(F7))

	# for i in range(0, 1000):
	# 	F = influence(G, S8, EdgePara2)
	# 	F8.append(len(F))
	# print float(sum(F8)/len(F8))

	# for i in range(0, 1000):
	# 	F = influence(G, S9, EdgePara3)
	# 	F9.append(len(F))
	# print float(sum(F9)/len(F9))

	# for i in range(0, 1000):
	# 	F = influence(G, S10, EdgePara4)
	# 	F10.append(len(F))
	# print float(sum(F10)/len(F10))
	