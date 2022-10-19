import networkx as nx
import ijson
import json
from tqdm import tqdm

NODE_COUNT = 4894081
JSON_FILE = "./data/dblp.v12.json"
VENUES_FILE = "./data/dblp-venues.json"
GRAPH_FILE = "./data/dblp.gml"


def load_from_json(fn=JSON_FILE):
    file = open(JSON_FILE, 'rb')
    items = ijson.items(file, 'item')
    g = nx.DiGraph()
    venues = {}

    for item in tqdm(items, desc='Loading graph from ' + fn, total=NODE_COUNT):
        if 'venue' in item and 'id' in item['venue'] and 'raw' in item['venue']:
            if item['venue']['id'] not in venues:
                venues[item['venue']['id']] = item['venue']['raw']

        g.add_node(item['id'], v=item.get('venue', {}).get('id', -1))
        g.add_edges_from([(item['id'], other) for other in item.get('references', [])])

    file.close()
    return G, venues


def save_venues(v, fn=VENUES_FILE):
    with open(fn, 'w') as file:
        json.dump(v, file)


def save_graph(g, fn=GRAPH_FILE):
    print("Saving to {fn}...")
    nx.write_gml(g, fn)
    print("Done")


def load_venues(fn=VENUES_FILE):
    with open(fn, 'r') as file:
        v = json.load(file)
    return v


def load_graph(fn=GRAPH_FILE):
    return nx.read_gml(fn)


def load(gfn=GRAPH_FILE, vfn=VENUES_FILE):
    g = load_graph(gfn)
    v = load_venues(vfn)
    return g, v
