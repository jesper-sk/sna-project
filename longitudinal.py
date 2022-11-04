# %% Imports
import json
from hep_ph import *
import os, time
from pathlib import Path
from tqdm import tqdm
from dateutil.parser import parse
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

PUB_DATA_FILE = './data/pub.csv'


# %%
def scrape_arxiv_data(graph, wait: int = 3, start_at: int = 0, write_thresh: int = 15, keep_trying: bool = False):
    waits = [0, 1, 5, 10, 30]
    path = Path(PUB_DATA_FILE)
    if start_at == 0 and path.exists():
        os.remove(path)
        with path.open('w') as file:
            file.write("idx|::|node_id|::|title|::|authors|::|date|::|arxiv_uri\n")
    lines = []
    for i, node in enumerate(graph.nodes):
        if i < start_at:
            continue
        print(f"{i:6d} {node}")
        success = False
        trial = 0
        while keep_trying or trial < len(waits):
            if success:
                break
            wait = waits[trial] if not keep_trying else waits[-1] * 4
            if wait:
                print('waiting %s seconds...' % wait)
                time.sleep(wait)
            try:
                r = to_arxiv(node)
                lines.append(
                    f"{i}|::|{node}|::|{r.title}|::|{';'.join(map(str, r.authors))}|::|{r.published.isoformat()}|::|{r.entry_id}\n")
                success = True
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(e)
                trial += 1

        if not success:
            with open('./data/pub.log', 'a') as file:
                file.write('Failed to extract %s!\n' % node)

        if i % write_thresh == 0:
            with path.open('a') as file:
                file.writelines(lines)

        time.sleep(wait)


graph = citation_graph()
scrape_arxiv_data(graph)

# #%%
#
# all = []
# with open('./data/arxiv-metadata-oai-snapshot.json', 'rb') as file:
#     for line in tqdm(file.readlines()):
#         all.append(json.loads(line))
#
# #%%
# relevant = []
# for entry in all:
#     id = all

# %%


def get_dates():
    DATE_FILE = './data/cit-HepPh-dates.txt'
    dates = {}
    with open(DATE_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            offset = 2 if line.startswith('11') else 0
            spl = line.split('\t')
            id = spl[0][offset:]
            date = parse(spl[1])
            dates[id] = date
    return dates


# %%
g = citation_graph()
dates = get_dates()


#%%
for node in tqdm(g.nodes):
    g.add_node(node, date=dates.get(f"{int(node):07d}"))


#%%
def get_cit_per_year(g, ids = None, ppy=4):
    years = []
    ids = ids or list(g.nodes)
    for id in ids:
        date = g.nodes[id]['date']
        if not date:
            continue
        for neigh in g.predecessors(id):
            ndate = g.nodes[neigh]['date']
            if not ndate:
                continue
            ts = ndate - date
            quarters = ts.days // (365 // ppy)
            years.append(quarters / ppy)

    return [year for year in years if year >= 0]


def plot_cit_per_year(years, ppy=4):
    plt.figure()
    plt.xlabel("Years since publication")
    plt.ylabel("Total number of citations")
    plt.xticks(range(11))
    plt.yticks(np.arange(0, 9001, 1000))
    plt.hist(years, bins=int(ppy * 10), linewidth=1, edgecolor='black')
    plt.savefig("./img/longitudinalt.pdf", bbox_inches='tight', pad_inches=0)
    plt.show()

#%%
plt.savefig('img/big-pub-citations.pdf', bbox_inches='tight', pad_inches=0)