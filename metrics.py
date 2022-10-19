from graph import graph

G = graph()

#%%
# Calculate the metrics and measures discussed:
# number of vertices, number of edges, degree distribution
# (in-degree and out degree), centrality indices, clustering
# coefficient, network diameter, density, number of
# connected components and, size of the connected
# components.

in_deg = G.in_degree()
out_deg = G.out_degree()
