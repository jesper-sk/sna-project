import arxiv
import networkx as nx

EDGE_FILE = './data/Cit-HepPh.txt'
DATE_FILE = './data/cit-HepPh-dates.txt'
COAUTH_FILE = './data/CA-HepPh.txt'
ARXIV_ARCHIVE = 'hep-ph/'


def citation_graph(fn: str = EDGE_FILE):
    return nx.read_edgelist(fn, create_using=nx.DiGraph())


def coauthorship_graph(fn: str = COAUTH_FILE):
    return nx.read_edgelist(fn, create_using=nx.Graph())


def to_arxiv(node_id: str):
    return next(arxiv.Search(id_list=[ARXIV_ARCHIVE + node_id]).results())
