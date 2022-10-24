import arxiv
import networkx as nx

EDGE_FILE = './data/Cit-HepPh.txt'
DATE_FILE = './data/cit-HepPh-dates.txt'
ARXIV_ARCHIVE = 'hep-ph/'


def graph(fn: str = EDGE_FILE):
    return nx.read_edgelist(fn, create_using=nx.DiGraph())


def to_arxiv(node_id: str):
    return next(arxiv.Search(id_list=[ARXIV_ARCHIVE + node_id]).results())
