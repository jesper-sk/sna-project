import networkx as nx
from tqdm import tqdm
from hep_ph import *


def get_cliques(g):
    return [tuple(c) for c in tqdm(nx.find_cliques_recursive(g), desc='Getting cliques')]


def get_best_cliques(g, c):
    best_cliques = set()
    for node in tqdm(g.nodes, desc="Getting best"):
        relevant = [clique for clique in c if node in clique]
        if not relevant:
            continue
        best = max(relevant, key=len)
        best_cliques.add(best)
    return list(best_cliques)


def clique_graph(g, c):
    res = nx.Graph()
    res.add_nodes_from([(idx, dict(nodes=set(nodes), size=len(nodes))) for idx, nodes in enumerate(c)])
    for i in res.nodes:
        for j in res.nodes:
            if i == j:
                continue
            if len(res.nodes[i]['nodes'].intersection(res.nodes[j]['nodes'])) > 0:
                res.add_edge(i, j)
    return res


G = citation_graph()
print(get_cliques(G))
