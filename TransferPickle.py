from copy import deepcopy
import networkx as nx
import re


f = open("epinions.txt")
s = f.read()
s1 = re.split('\n', s)
G = nx.Graph()

a = re.split(' ', s1[0])

for i in range(0, int(a[0])):
	G.add_node(i)

for i in range(1, int(a[1]) + 1):
	b = re.split(' ', s1[i])
	G.add_edge(int(b[0]),int(b[1]))
	G[int(b[0])][int(b[1])]['weight'] = 1

nx.write_gpickle(G,"epinions.gpickle")

# G1 = nx.read_gpickle("graphs/fb.gpickle")
# print G1[0][200]['weight']