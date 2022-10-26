from typing import Tuple, Dict

import networkx as nx
from hep_ph import citation_graph, to_arxiv

#%%
G = citation_graph()


def page_rank(hits: Tuple[Dict[str, float], Dict[str, float]], balance: float = 0.5):
    assert 0 <= balance <= 1
    hubs = hits[0]
    auths = hits[1]
    inv_bal = 1 - balance
    ranks = {k: hubs[k] * balance + auths[k] * inv_bal for k in hubs.keys()}
    return sorted(ranks.items(), key=lambda x: x[1], reverse=True)


#%%
pr = page_rank(nx.hits(G))
print(to_arxiv(pr[0][0]))

