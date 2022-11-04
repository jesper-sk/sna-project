from operator import itemgetter
import numpy as np
from hep_ph import citation_graph
import matplotlib.pyplot as plt
import networkx as nx

G = citation_graph()

#########################################3
# Egocentric network stuff
max_hub = 9909232
max_auth = 9811291
twice = 9803315
ego = twice
egograph = nx.ego_graph(G, str(ego), radius=1.5)

# #####################################
# Draw graph with own colors and sizes
colors = ['#80032F' if node == str(ego) else '#1f78b4' for node in egograph.nodes()]
nx.draw_networkx_nodes(egograph,
                       pos=nx.kamada_kawai_layout(egograph),
                       node_color=colors,
                       edgecolors=['#000000'] * len(egograph.nodes()))

colors_edges = ['#000000' if edge[0] == str(ego) or edge[1] == str(ego) else '#888888' for edge in egograph.edges()]
style_edges = ['solid' if edge[0] == str(ego) or edge[1] == str(ego) else 'dashed' for edge in egograph.edges()]
nx.draw_networkx_edges(egograph,
                       pos=nx.kamada_kawai_layout(egograph),
                       edge_color=colors_edges,
                       style=style_edges)
plt.savefig('img/egograph_' + str(ego) + '.png')
plt.show()

##############################################
# Standard Kamada-Kawai force-directed layout
fig = plt.figure()
nx.draw_kamada_kawai(egograph)

#################################################
# Draw egograph
seed = 20532

node_and_degree = G.degree()
(largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]

# Create ego graph of main hub
hub_ego = nx.ego_graph(G, largest_hub, radius=2)

# Draw graph
pos = nx.spring_layout(hub_ego, seed=seed)  # Seed layout for reproducibility
nx.draw(hub_ego, pos, node_color="b", node_size=50, with_labels=False)

# Draw ego as large and red
options = {"node_size": 300, "node_color": "r"}
nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], **options)

#################################################
# Eigenvector centralities
eigen = nx.eigenvector_centrality(G)
print(eigen)
ego_eigen = dict((k, eigen[k]) for k in egograph.nodes())

colors = ['#80032F' if node == str(ego) else '#1f78b4' for node in egograph.nodes()]
sizes = np.array(list(ego_eigen.values()))
print(sizes)
sizes *= 50000

nx.draw_networkx_nodes(egograph,
                       pos=nx.kamada_kawai_layout(egograph),
                       node_color=colors,
                       node_size=sizes,
                       edgecolors=['#000000'] * len(egograph.nodes()))

colors_edges = ['#000000' if edge[0] == str(ego) or edge[1] == str(ego) else '#888888' for edge in egograph.edges()]
style_edges = ['solid' if edge[0] == str(ego) or edge[1] == str(ego) else 'dashed' for edge in egograph.edges()]
nx.draw_networkx_edges(egograph,
                       pos=nx.kamada_kawai_layout(egograph),
                       edge_color=colors_edges,
                       style=style_edges)
plt.savefig('img/egograph_eigen_' + str(ego) + '.png')
plt.show()

######################################################33
# 77 highest eigenvector centralities
highest_eigen_nodes = [node for node, value in eigen.items() if value > 0.05]

# Create subgraph
subgraph = nx.DiGraph()
for node in highest_eigen_nodes:
    subgraph.add_node(node)

for edge in G.edges():
    if edge[0] in highest_eigen_nodes and edge[1] in highest_eigen_nodes:
        subgraph.add_edge(edge[0], edge[1])

# Plot result
ego_eigen = dict((k, eigen[k]) for k in subgraph.nodes())

colors = ['#80032F' if node == str(ego) else '#1f78b4' for node in subgraph.nodes()]
sizes = np.array(list(ego_eigen.values()))
sizes *= 3000

nx.draw_networkx_nodes(subgraph,
                       pos=nx.kamada_kawai_layout(subgraph),
                       node_color=colors,
                       node_size=sizes,
                       edgecolors=['#000000'] * len(subgraph.nodes()))

colors_edges = ['#888888' for _ in subgraph.edges()]
style_edges = ['solid' for _ in subgraph.edges()]
nx.draw_networkx_edges(subgraph,
                       pos=nx.kamada_kawai_layout(subgraph),
                       edge_color=colors_edges,
                       style=style_edges)
plt.savefig('img/egograph_eigen_highest_' + str(ego) + '.png')
plt.show()

#########################################################
# Hubs and authorities
hubs, auths = nx.hits(G)
num = 10
best_hubs = dict(sorted(hubs.items(), key=lambda x: x[1], reverse=True)[:num])
best_auths = dict(sorted(auths.items(), key=lambda x: x[1], reverse=True)[:num])
hubs_and_auths = best_hubs | best_auths
colors = ['#555555'] * num + ['#888888'] * num
labels = {key: ('a' if index / 10 > 0.9 else 'h') + str(index % 10 + 1) for index, (key, value) in enumerate(hubs_and_auths.items())}
print(labels)

# Create subgraph
subgraph = nx.DiGraph()
for node, _ in hubs_and_auths.items():
    subgraph.add_node(node)

for edge in G.edges():
    if edge[0] in hubs_and_auths.keys() and edge[1] in hubs_and_auths.keys():
        subgraph.add_edge(edge[0], edge[1])

# Plot result
nx.draw_networkx_nodes(subgraph,
                       pos=nx.kamada_kawai_layout(subgraph),
                       node_color=colors,
                       edgecolors=['#000000'] * len(subgraph.nodes()))

colors_edges = ['#888888' for _ in subgraph.edges()]
style_edges = ['solid' for _ in subgraph.edges()]
nx.draw_networkx_edges(subgraph,
                       pos=nx.kamada_kawai_layout(subgraph),
                       edge_color=colors_edges,
                       style=style_edges)
nx.draw_networkx_labels(subgraph,
                        pos=nx.kamada_kawai_layout(subgraph),
                        labels=labels,
                        font_size=8,
                        font_color='#FFFFFF')
plt.savefig('img/graph_hubs_and_auths.png')
plt.show()

############################################################
# Clustering coefficients
def plot_egograph(graph, ego, value_type, node_values, colors=None, labels=None):
    if colors is None:
        colors = ['#80032F' if node == str(ego) else '#1f78b4' for node in graph.nodes()]

    sizes = np.array(list(node_values.values()))
    sizes *= 800 / max(sizes)

    nx.draw_networkx_nodes(graph,
                           pos=nx.kamada_kawai_layout(graph),
                           node_color=colors,
                           node_size=sizes,
                           edgecolors=['#000000'] * len(graph.nodes()))

    colors_edges = ['#000000' if edge[0] == str(ego) or edge[1] == str(ego) else '#888888' for edge in graph.edges()]
    style_edges = ['solid' if edge[0] == str(ego) or edge[1] == str(ego) else 'dashed' for edge in graph.edges()]
    nx.draw_networkx_edges(graph,
                           pos=nx.kamada_kawai_layout(graph),
                           edge_color=colors_edges,
                           style=style_edges)

    if labels is not None:
        nx.draw_networkx_labels(subgraph,
                                pos=nx.kamada_kawai_layout(subgraph),
                                labels=labels,
                                font_size=8,
                                font_color='#FFFFFF')

    plt.savefig('img/egograph_' + value_type + "_" + str(ego) + '.png')
    plt.show()


clustering_coefs = nx.clustering(G)

max_hub = 9909232
max_auth = 9811291

ego = 9909232
egograph = nx.ego_graph(G, str(ego), radius=1.5)
ego_coefs = dict((k, clustering_coefs[k]) for k in egograph.nodes())

plot_egograph(egograph, ego, 'clustering', ego_coefs)

###########################################################
# Clustering with hubs and authorities
hubs, auths = nx.hits(G)
num = 10
best_hubs = dict(sorted(hubs.items(), key=lambda x: x[1], reverse=True)[:num])
best_auths = dict(sorted(auths.items(), key=lambda x: x[1], reverse=True)[:num])
hubs_and_auths = best_hubs | best_auths

# Create subgraph
subgraph = nx.DiGraph()
for node, _ in hubs_and_auths.items():
    subgraph.add_node(node)

for edge in G.edges():
    if edge[0] in hubs_and_auths.keys() and edge[1] in hubs_and_auths.keys():
        subgraph.add_edge(edge[0], edge[1])

# Compute parameters
colors = ['#555555'] * num + ['#888888'] * num
labels = {key: ('a' if index / 10 > 0.9 else 'h') + str(index % 10 + 1) for index, (key, value) in enumerate(hubs_and_auths.items())}
ha_coefs = dict((k, clustering_coefs[k]) for k in subgraph.nodes())

plot_egograph(subgraph, 0, 'clustering', ha_coefs, colors=colors, labels=labels)

