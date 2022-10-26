from hep_ph import citation_graph, to_arxiv
from hep_ph import coauthorship_graph
import matplotlib.pyplot as plt
import networkx as nx

#%%
# Calculate the metrics and measures discussed:
# number of vertices, number of edges, degree distribution
# (in-degree and out degree), centrality indices, clustering
# coefficient, network diameter, density, number of
# connected components and, size of the connected
# components.

# Citations
G = citation_graph()

order = G.order()
edges = G.number_of_edges()
in_deg = G.in_degree()
out_deg = G.out_degree()
in_deg_centr = nx.in_degree_centrality(G)
out_deg_centr = nx.out_degree_centrality(G)
clustering = nx.clustering(G)
density = nx.density(G)
wccs = list(nx.weakly_connected_components(G))
sccs = list(nx.strongly_connected_components(G))
big_wcc = max(wccs, key=len)
big_scc = max(sccs, key=len)
dens_big_wcc = nx.density(nx.subgraph(G, big_wcc))
dens_big_scc = nx.density(nx.subgraph(G, big_scc))

# Link to paper with the most cited papers
node_id = max(out_deg_centr, key=out_deg_centr.get)
print(node_id)
print(to_arxiv("0" + str(node_id)))

# Plot the number of citations towards each paper
counts_in_deg = {}
for (_, degree) in in_deg:
    if degree in counts_in_deg:
        counts_in_deg[degree] += 1
    else:
        counts_in_deg[degree] = 1

fig = plt.figure()
plt.title('Histogram of the in-degree')
plt.xlabel('Fraction of papers that cite a paper')
plt.ylabel('Number of papers')
# plt.hist(counts_in_deg, bins=40, rwidth=0.7)
plt.hist(counts_in_deg, bins=40, rwidth=0.7, align='left')
plt.savefig('img/hist_in_degree.png')
plt.show()

# Plot the number of citations towards each paper
counts_out_deg = {}
for (_, degree) in out_deg:
    if degree in counts_out_deg:
        counts_out_deg[degree] += 1
    else:
        counts_out_deg[degree] = 1

fig = plt.figure()
plt.title('Histogram of the out-degree')
plt.xlabel('Fraction of papers that a paper cites')
plt.ylabel('Number of papers')
# plt.hist(counts_in_deg, bins=40, rwidth=0.7)
plt.hist(counts_out_deg, bins=40, rwidth=0.7, align='left')
plt.savefig('img/hist_out_degree.png')
plt.show()

# Plot the sizes of the strongly connected components
sizes_sccs = {}
for component in sccs:
    size = len(component)
    if size in sizes_sccs:
        sizes_sccs[size] += 1
    else:
        sizes_sccs[size] = 1

fig = plt.figure()
plt.title('Histogram of the sizes of strongly connected components')
plt.xlabel('The size of a strongly connected component')
plt.ylabel('Number of components')
plt.hist(sizes_sccs, bins=40, rwidth=0.7, align='left')
plt.savefig('img/hist_sccs.png')
plt.show()



# Coauthorship
# G_coauthor = coauthorship_graph()
#
# order = G_coauthor.order()
# edges = G_coauthor.number_of_edges()
# deg = G_coauthor.degree()
#
# counts_ccs = {}
# for (_, degree) in deg:
#     if degree in counts_ccs:
#         counts_ccs[degree] += 1
#     else:
#         counts_ccs[degree] = 1
#
# fig = plt.figure()
# plt.title('Histogram of the number of coauthors per author')
# plt.xlabel('Number of coauthors')
# plt.ylabel('Number of nodes')
# plt.hist(counts_ccs, bins=40)
# plt.show()
#
# ccs = nx.connected_components(G_coauthor)
# print(order, edges, deg, ccs)
