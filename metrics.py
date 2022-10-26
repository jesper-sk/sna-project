from hep_ph import citation_graph
from hep_ph import coauthorship_graph
import matplotlib.pyplot as plt

# G = citation_graph()

#%%
# Calculate the metrics and measures discussed:
# number of vertices, number of edges, degree distribution
# (in-degree and out degree), centrality indices, clustering
# coefficient, network diameter, density, number of
# connected components and, size of the connected
# components.

import networkx as nx

# Citations
# order = G.order()
# edges = G.number_of_edges()
# in_deg = G.in_degree()
# out_deg = G.out_degree()
# in_deg_centr = nx.in_degree_centrality(G)
# out_deg_centr = nx.out_degree_centrality(G)
# clustering = nx.clustering(G)
# density = nx.density(G)
# wccs = list(nx.weakly_connected_components(G))
# sccs = list(nx.strongly_connected_components(G))
# big_wcc = max(wccs, key=len)
# big_scc = max(sccs, key=len)
# dens_big_wcc = nx.density(nx.subgraph(G, big_wcc))
# dens_big_scc = nx.density(nx.subgraph(G, big_scc))

# Coauthorship
G_coauthor = coauthorship_graph()

order = G_coauthor.order()
edges = G_coauthor.number_of_edges()
deg = G_coauthor.degree()

counts_ccs = {}
for (_, degree) in deg:
    if degree in counts_ccs:
        counts_ccs[degree] += 1
    else:
        counts_ccs[degree] = 1

fig = plt.figure()
plt.title('')
plt.xlabel('Number of coauthors')
plt.ylabel('Number of nodes')
plt.hist(counts_ccs, bins=40)
plt.show()

ccs = nx.connected_components(G_coauthor)
print(order, edges, deg, ccs)
