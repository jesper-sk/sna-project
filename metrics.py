from hep_ph import citation_graph, to_arxiv, coauthorship_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def histogram(name, bins, xlabel, counts, ylabel='Occurrence', log=False):
    fig = plt.figure()
    plt.title('Histogram of ' + name)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.hist(counts, bins=bins, rwidth=0.7, align='left', log=log)
    plt.savefig('img/coath_' + name + '.png')
    plt.show()

# #%%
# # Calculate the metrics and measures discussed:
# # number of vertices, number of edges, degree distribution
# # (in-degree and out degree), centrality indices, clustering
# # coefficient, network diameter, density, number of
# # connected components and, size of the connected
# # components.
#
# # Citations
# G = citation_graph()
# order = G.order()
# edges = G.number_of_edges()
# in_deg = G.in_degree()
# out_deg = G.out_degree()
# in_deg_centr = nx.in_degree_centrality(G)
# out_deg_centr = nx.out_degree_centrality(G)
# clustering = nx.clustering(G)
# mean_clustering_coef = sum(clustering.values()) / len(clustering)
# print(mean_clustering_coef)
# density = nx.density(G)
# print(density)
#
# # Components
# wccs = list(nx.weakly_connected_components(G))
# sccs = list(nx.strongly_connected_components(G))
# big_wcc = max(wccs, key=len)
# big_scc = max(sccs, key=len)
# dens_big_wcc = nx.density(nx.subgraph(G, big_wcc))
# dens_big_scc = nx.density(nx.subgraph(G, big_scc))
#
# # Plot in- and out-degree
# counts_in_deg = {}
# for (_, degree) in in_deg:
#     if degree in counts_in_deg:
#         counts_in_deg[degree] += 1
#     else:
#         counts_in_deg[degree] = 1
#
# counts_out_deg = {}
# for (_, degree) in out_deg:
#     if degree in counts_out_deg:
#         counts_out_deg[degree] += 1
#     else:
#         counts_out_deg[degree] = 1
#
# fig = plt.figure()
# plt.title('Histogram of the in- and out-degrees')
# plt.xlabel('Degree')
# plt.ylabel('Number of papers')
# max_value = max(max(counts_in_deg.values()), max(counts_out_deg.values()))
# plt.hist(list(counts_in_deg.values()), bins=40, rwidth=0.5, align='left', label='In-degree', range=(0, max_value))
# plt.hist(list(counts_out_deg.values()), bins=40, rwidth=0.5, align='mid', label="Out-degree", range=(0, max_value))
# plt.legend()
# plt.savefig('img/hist_inout_degree.png')
# plt.show()
#
# log_counts_in = {k: np.log(np.log(val)) for k, val in counts_in_deg.items()}
# log_counts_out = {k: np.log(np.log(val)) for k, val in counts_out_deg.items()}
# fig = plt.figure()
# plt.title('Histogram of the logarithmic in- and out-degrees')
# plt.xlabel('Degree')
# plt.ylabel('Log(Log(Number of papers))')
# max_value = max(max(log_counts_in.values()), max(log_counts_out.values()))
# plt.hist(list(log_counts_in.values()), bins=40, rwidth=0.5, align='left', label='In-degree', range=(0, max_value))
# plt.hist(list(log_counts_out.values()), bins=40, rwidth=0.5, align='mid', label="Out-degree", range=(0, max_value))
# plt.legend()
# plt.savefig('img/hist_loglog_inout_degree.png')
# plt.show()

################################################
# Coauthorship
G_coauthor = coauthorship_graph()

# order = G_coauthor.order()
# edges = G_coauthor.number_of_edges()
# deg = G_coauthor.degree()
#
# # Degree centralities
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
# plt.ylabel('Number of authors')
# plt.hist(counts_ccs.values(), bins=40, rwidth=0.7)
# plt.savefig('img/hist_degree.png')
# plt.show()
#
# fig = plt.figure()
# plt.title('Histogram of the logarithmic number of coauthors per author')
# plt.xlabel('Number of coauthors')
# plt.ylabel('Log(Number of authors)')
# plt.hist(counts_ccs.values(), bins=40, rwidth=0.7, log=True)
# plt.savefig('img/hist_log_degree.png')
# plt.show()

# Eigenvector centralities
eigen = nx.eigenvector_centrality(G_coauthor)
print(min(eigen.values()), max(eigen.values()))
th = 0
values = list(filter(lambda val: val > th, eigen.values()))

nr_bins = 200
histogram('logarithmic eigenvector centrality',
          nr_bins,
          'Eigenvector centrality',
          values,
          ylabel="Log(Occurrence)",
          log=True)
