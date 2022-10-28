import networkx as nx
from hep_ph import citation_graph, to_arxiv


#%%
def hits_combine(G):
    hubs, auths = nx.hits(G)
    ranks = {k: hubs[k] * auths[k] for k in hubs.keys()}
    return sorted(ranks.items(), key=lambda x: x[1], reverse=True)


#%%
g = citation_graph()
hu, au = nx.hits(g)
pr = hits_combine(g)
print(to_arxiv(pr[0][0]))

#%%
hu = sorted(hu.items(), key=lambda x: x[1], reverse=True)
au = sorted(au.items(), key=lambda x: x[1], reverse=True)

#%%

for i, (id, score) in enumerate(pr):
    if i >= 10:
        break
    ar = to_arxiv(id)
    print(f"{i+1}\t{id}\t{hu[id]:.3e}\t{au[id]:.3e}\t{score:.3e}\t{ar.title}")