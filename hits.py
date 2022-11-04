import networkx as nx
from hep_ph import citation_graph, to_arxiv


#%%
def hits_combine(G):
    hubs, auths = nx.hits(G)
    ranks = {k: hubs[k] * auths[k] for k in hubs.keys()}
    return sorted(ranks.items(), key=lambda x: x[1], reverse=True)


g = citation_graph()
hud, aud = nx.hits(g)
prd = nx.pagerank_numpy(g)

#%%

hu = sorted(hud.items(), key=lambda x: x[1], reverse=True)
au = sorted(aud.items(), key=lambda x: x[1], reverse=True)
pr = sorted(prd.items(), key=lambda x: x[1], reverse=True)

#%%

# print("Hubs")
for i, (id, hub_score) in enumerate(hu):
    if i >= 10: break
    print(f'{g.in_degree(id)}\t{g.out_degree(id)}')
    # print(f"{i+1:2d}\t{int(id):07d}\t{aud[id]:.1e}\t{hub_score:.1e}\t{prd[id]:.1e}")
print("in\tout")
# print("Authorities")
for i, (id, auth_score) in enumerate(au):
    if i >= 10: break
    print(f'{g.in_degree(id)}\t{g.out_degree(id)}')
    # print(f"{i+1:2d}\t{int(id):07d}\t{auth_score:.1e}\t{hud[id]:.1e}\t{prd[id]:.1e}")
print("in\tout")
# print("PageRank")
for i, (id, pagerank) in enumerate(pr):
    if i >= 10: break
    print(f'{g.in_degree(id)}\t{g.out_degree(id)}')
    # print(f"{i+1:2d}\t{int(id):07d}\t{aud[id]:.1e}\t{hud[id]:.1e}\t{pagerank:.1e}")