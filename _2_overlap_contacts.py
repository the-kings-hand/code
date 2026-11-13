import csv
import networkx as nx
from operator import itemgetter
from pathlib import Path

"""with open(str(Path.cwd()) + '/data/Years/1522.csv', 'r') as edgescsv:
	edgereader = csv.reader(edgescsv) 
	edges = [tuple(e) for e in edgereader][1:] 

with open(str(Path.cwd()) + '/data/full_person_list.csv','r') as nodescsv: #nodelist
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]
node_names = [n[0] for n in nodes]"""

"""G = nx.Graph()
G.add_edges_from(edges)
hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]

for i in range(1523,1542):
	print('\n' + str(i), G.number_of_nodes())
	Cromwell_neighbours = set(G.neighbors('32545'))
	Wolsey_neighbours = set(G.neighbors('3674'))
	archive = {}
	for node in G:
		archive[node] = 'none'
	def NodeLabel(neighbours, item):
		for u, v in archive.items():
			if u in neighbours:
				if v == 'none':
					archive[u] = item
				if v != 'none':
					archive[u] = str(v + ", " + item)
		return
	NodeLabel(Cromwell_neighbours, 'Cromwell')
	NodeLabel(Wolsey_neighbours, 'Wolsey')
	nx.set_node_attributes(G, archive, 'archive')
	print(i, 'Graph Size: ', len(G), 'Wolsey Contacts: ', len(Wolsey_neighbours), 'Cromwell contacts: ', len(Cromwell_neighbours), 'Overlap: ', len(Wolsey_neighbours.intersection(Cromwell_neighbours)))
	nx.write_gexf(G, str(str(i)+'_overlap.gexf'))"""

with open(str(Path.cwd()) + '/data/Years/1522.csv', 'r') as edgescsv:
	edgereader = csv.reader(edgescsv) 
	edges = [tuple(e) for e in edgereader][1:] 

with open(str(Path.cwd()) + '/data/full_person_list.csv','r') as nodescsv: #nodelist
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]

G = nx.Graph()
G.add_edges_from(edges)
hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]

for i in range(1523,1542):
	C_neighbours = set(G.neighbors('32545'))
	W_neighbours = set(G.neighbors('3674'))
	All_Nodes = {}
	for node in G:
		All_Nodes[node] = 'none'

	def NodeLabel(archive, item):
		for u, v in All_Nodes.items():
			if u in archive:
				if v == 'none':
					All_Nodes[u] = item
				if v != 'none':
					All_Nodes[u] = str(v + ", " + item)
		return

	NodeLabel(C_neighbours, 'Cromwell')
	NodeLabel(W_neighbours, 'Wolsey')
	overlap = [node for node,archive in All_Nodes.items() if archive == 'Cromwell, Wolsey']
	print(str(i-1), 'Graph Size: ', len(G), 'Overlap Contacts: ', len(overlap))
	nx.write_gexf(G, str(str(i-1)+'_overlap_contacts.gexf'))

	with open(str(str((Path.cwd())) + '/data/Years/' + str(i) + '.csv'),'r') as edgescsv: #edgelist
		edgereader = csv.reader(edgescsv) 
		edges = [tuple(e) for e in edgereader][1:]
	G.add_edges_from(edges)
