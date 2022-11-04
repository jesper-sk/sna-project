import itertools as it
from functools import partial

import networkx as nx
from networkx.algorithms.community import girvan_newman

from hep_ph import citation_graph
#%%
G = citation_graph()
print(filter())
SG = nx.subgraph(G, max(nx.strongly_connected_components(G), key=len))
print(SG)
#%%


def estimated_betweenness_centrality(G, k=1000):
    return max(nx.betweenness_centrality(G, k=k), key=len)


def estimated_gn(G, k=1000):
    return girvan_newman(G, most_valuable_edge=partial(estimated_betweenness_centrality, k=k))


def estimated_gn_until(G, k=1000, lim=1000):
    gn = estimated_gn(G, k)
    tw = it.takewhile(lambda x: len(x) <= lim, gn)
    return [sorted(c) for c in tw]


#%%
