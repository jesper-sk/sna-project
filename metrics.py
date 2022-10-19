from graph import graph

G = graph()

#%%
# Calculate the metrics and measures discussed:
# number of vertices, number of edges, degree distribution
# (in-degree and out degree), centrality indices, clustering
# coefficient, network diameter, density, number of
# connected components and, size of the connected
# components.

import networkx as nx

order = G.order()
edges = G.number_of_edges()
in_deg = G.in_degree()
out_deg = G.out_degree()
in_deg_centr = nx.in_degree_centrality(G)
out_deg_centr = nx.out_degree_centrality(G)
clustering = nx.clustering(G)
# diameter = infinite (not strongly connected)
density = nx.density(G)
#connnected_components = not implemented

#%% weakly connected components
big_weak_cc = max(nx.weakly_connected_components(G), key=len)

