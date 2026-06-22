import csv
import networkx as nx
from operator import itemgetter
from pathlib import Path

with open(str(Path.cwd()) + '/data/Years/1522.csv', 'r') as edgescsv:
	edgereader = csv.reader(edgescsv) 
	edges = [tuple(e) for e in edgereader][1:] 

with open(str(Path.cwd()) + '/data/full_person_list.csv','r') as nodescsv: #nodelist
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]
node_names = [n[0] for n in nodes]

G = nx.Graph()
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
	nx.write_gexf(G, str(str(i)+'_overlap.gexf'))
	with open(str(str((Path.cwd()).parent) + '/data/Years/' + str(i) + '.csv'),'r') as edgescsv: #edgelist
		edgereader = csv.reader(edgescsv) 
		edges = [tuple(e) for e in edgereader][1:]
	update = nx.Graph()
	update.add_edges_from(edges)
	if '32545' in update:
		update_neighbours = set(update.neighbors('32545'))
		nx.set_node_attributes(G, hist_name_dict, 'historical_name')
		nx.set_node_attributes(update, hist_name_dict, 'historical_name')
		overlap = [] 
		for node in Cromwell_neighbours:
			if node in update_neighbours:
				overlap.append(hist_name_dict[node])
		print(len(update_neighbours), len(overlap), overlap)
	else:
		print('no edges')
	G.add_edges_from(edges)
