import itertools
from hep_ph import coauthorship_graph, citation_graph
from networkx import find_cliques, bridges
import networkx as nx
from networkx.algorithms.community import girvan_newman

G = coauthorship_graph()
print(len(G.nodes()), len(G.edges()))
print(nx.average_clustering(G))
print(nx.density(G))

ccs = list(nx.connected_components(G))
largest_ccs = max(ccs, key=len)
print("Length largest cc: ", len(largest_ccs))
print("Density:", nx.density(G.subgraph(largest_ccs)))
print("Diameter:", nx.diameter(G.subgraph(largest_ccs)))

#%%
# Detect the communities of types that were discussed:
# - Cliques
# - Important nodes acting as Bridges
# - Partitioning Algorithm: Girvan-Newman

# Cliques
print("Find cliques")
cliques = list(find_cliques(G))

# Count correspondences between cliques and connected components
count = 0
for clique in cliques:
    c = set(clique)
    if c in ccs:
        count += 1
print("CCs and cliques that are the same:", count)

# The clique number of a graph is the size of the largest clique in the graph.
clique_number = max([len(c) for c in cliques])
print("The clique number: ", clique_number)

# The number of maximal cliques in the graph.
no_maximal_cliques = len(cliques)
print("Number of maximal cliques: ", no_maximal_cliques)

# Bridges
print("No bridges:", len(list(bridges(G))))

