from hep_ph import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#%%
g = coauthorship_graph()

#%%
b = list(nx.bridges(g))

#%%
c = nx.edge_betweenness_centrality(g, 500)
print("hey jochie")

#%%
b = sorted([(bi, c[bi]) for bi in b], key=lambda x: x[1], reverse=True)

#%%

for i in range(10):
    curr = b[i]
    print(f"{curr[0][0]}\t{curr[0][1]}\t{curr[1]:.3e}")
