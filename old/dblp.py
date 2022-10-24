import networkx as nx
import ijson
import json
from tqdm import tqdm

NODE_COUNT = 4894081
JSON_FILE = "./data/dblp.v12.json"
VENUES_FILE = "../data/dblp-venues.json"
GRAPH_FILE = "../data/dblp.gml"


def load_from_json(fn=JSON_FILE):
    with open(fn, 'rb') as file:
        items = ijson.items(file, 'item')
        graph = nx.DiGraph()
        venues = {}

        for item in tqdm(items, desc='Loading graph from ' + fn, total=NODE_COUNT):
            venue = item.get('venue', dict())
            raw = venue.get('raw', 'unknown')
            venue_id = venue.get('id', raw)
            if venue_id not in venues:
                venues[venue_id] = {'n': raw, 'c': 1}
            else:
                venues[venue_id]['c'] += 1

            graph.add_node(item['id'], v=venue_id)
            graph.add_edges_from([(item['id'], other) for other in item.get('references', [])])

    for k, v in venues.items():
        venues[k]['p'] = v['c'] / NODE_COUNT

    return graph, venues


def conservative_load_from_json(fn=JSON_FILE):
    graph = nx.DiGraph()
    with open(fn, 'rb') as file:
        items = ijson.items(file, 'item')
        for item in tqdm(items, total=NODE_COUNT):
            gid = int(item['id'])
            graph.add_node(gid)
            graph.add_edges_from([(gid, int(ref)) for ref in item.get('references', [])])

    return graph


def save_venues(v, fn=VENUES_FILE):
    with open(fn, 'w') as file:
        json.dump(v, file)


def save_graph(g, fn=GRAPH_FILE):
    print(f"Saving to {fn}...")
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


def venue(node):
    venue = node.get('venue', dict())
    raw = venue.get('raw', 'unknown')
    venue_id = venue.get('id', raw)
    return venue_id
