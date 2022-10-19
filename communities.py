from graph import undirected_graph
from networkx import find_cliques, bridges
from networkx.algorithms.community import girvan_newman

G = undirected_graph("networks")
print(len(G.nodes()))

#%%
# Detect the communities of types that were discussed:
# - Cliques
# - Homophily analysis
# - Important nodes acting as Bridges
# - Partitioning Algorithm: Girvan-Newman

# Cliques
print("Find cliques")
cliques = list(find_cliques(G))
print(cliques)

# The clique number of a graph is the size of the largest clique in the graph.
clique_number = max([len(c) for c in cliques])
print("The clique number: ", clique_number)

# The number of maximal cliques in the graph.
no_maximal_cliques = len(cliques)
print("Number of maximal cliques: ", no_maximal_cliques)

# Homophily analysis
# 1. Kies een attribute


# 2. Bereken de fractions of occurrences


# 3. Voor ieder paar van mogelijke attribute values, bereken:
#   3.1 de verwachte 'random' occurrence waarde
#   3.2 de fraction of edges die van dit type zijn


# Bridges
print(bridges(G))

# Partitioning Algorithm: Girvan-Newman
# Finds communities in a graph using the Girvan–Newman method.
print(girvan_newman(G))
