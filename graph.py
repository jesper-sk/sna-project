import networkx as nx
FILE = "./data/citation.edgelist.txt"


def graph():
    with open(FILE, 'r') as file:
        txt = file.readlines()
    edge_data = [list(map(int, e.strip().split('\t'))) for e in txt]
    node_data = {e[0] for e in edge_data}.union({e[1] for e in edge_data})

    G = nx.DiGraph()
    G.add_nodes_from(node_data)
    G.add_edges_from(edge_data)

    return G

