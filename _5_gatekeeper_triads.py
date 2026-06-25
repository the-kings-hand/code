import csv
import networkx as nx
from operator import itemgetter
from pathlib import Path

with open(str(Path.cwd()) + '/data/Jan-July_1540.csv','r') as edgescsv: #opens the file
	edgereader = csv.reader(edgescsv) #reads the file
	edges = [tuple(e) for e in edgereader][1:] #the number one elimates the first row, with source and target
	
with open(str(Path.cwd()) + '/data/full_person_list.csv','r') as nodescsv:
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]
node_names = [n[0] for n in nodes]

G = nx.DiGraph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)

hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]	
nx.set_node_attributes(G, hist_name_dict, 'historical_name')

Gund = nx.to_undirected(G)
import networkx.algorithms.isomorphism as iso
shared_contacts = set(Gund.neighbors('11844')).intersection(set(Gund.neighbors('32545'))) #identifies where H and TC's contacts overlap (intersect)

sublibrary = []
triangletype = {}
for i in shared_contacts:
	sub = G.subgraph(['11844', '32545', i]) #making a subset of data that just includes the triads
	labels = {} #a dictionary for assigning labels
	labels['11844'] = 'H'
	labels['32545'] = 'C'
	labels[i] = 'X'
	nx.set_node_attributes(sub, labels, 'labels') #makes sure these labels work all the way through the rest of the subset of code
	nm = iso.categorical_node_match('labels', '')
	addsub = 1
	for subtype in sublibrary:
		if nx.is_isomorphic(sub, subtype, node_match=nm): #if it is the same as something else, do not make a new category
			addsub = 0
			triangletype[i] = sublibrary.index(subtype)
	if addsub == 1:
		sublibrary.append(sub)
		triangletype[i] = sublibrary.index(sub) #if it is different, add a new category 

TC_unshared_contacts = set(Gund.neighbors('32545')).difference(set(Gund.neighbors('11844')))
TC_unshared_contacts.remove('11844')
for node in TC_unshared_contacts:
    triangletype[node] = '6'

H_unshared_contacts = set(Gund.neighbors('11844')).difference(set(Gund.neighbors('32545')))
H_unshared_contacts.remove('32545')
for node in H_unshared_contacts:
    triangletype[node] = '7'

subgraph = set(Gund.neighbors('32545')).union(set(Gund.neighbors('11844')))
subgraph = G.subgraph(subgraph)
nx.set_node_attributes(subgraph, triangletype, 'triangle_type')

nx.write_gexf(subgraph, '1540_triads.gexf')