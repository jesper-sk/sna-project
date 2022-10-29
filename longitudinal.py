#%% Imports
import json

from hep_ph import *
import os, time
from pathlib import Path
import ijson
from tqdm import tqdm

PUB_DATA_FILE = './data/pub.csv'

#%%

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


if __name__ == '__main__':
    scrape_arxiv_data(citation_graph(), 2, 676)

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
