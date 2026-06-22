import csv
import networkx as nx
from operator import itemgetter
from pathlib import Path

with open(str(Path.cwd()) + '/data/1534-1540.csv','r') as edgescsv: #opens the file
	edgereader = csv.reader(edgescsv) #reads the file
	edges = [tuple(e) for e in edgereader][1:] #the number one elimates the first row, with source and target
	
with open(str(Path.cwd()) + '/data/full_person_list.csv','r') as nodescsv: #nodelist
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]
	
node_names = [n[0] for n in nodes]
hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]	


G = nx.MultiDiGraph()
G.add_nodes_from(node_names)
G.add_edges_from(edges, medium="letter", weight=1)

subnodes = []
for node in G:
	if G.degree(node) > 0:
		subnodes.append(node)
		
subgraph = G.subgraph(subnodes)

def sub_set(graph_name):
	neighbour_dict = {}
	for node in set(graph_name.successors('32545')).difference(set(graph_name.successors('11844'))):
		neighbour_dict[node] = 'TC'
	for node in set(graph_name.successors('11844')).difference(set(graph_name.successors('32545'))):
		neighbour_dict[node] = 'H'
	for node in set(graph_name.successors('32545')).intersection(set(graph_name.successors('11844'))):
		neighbour_dict[node] = 'both'
	return neighbour_dict

und = nx.to_undirected(subgraph)
H_TC_sub = set(und.neighbors('11844')).union(set(und.neighbors('32545')))

def flatten_graph(x):
	graph = nx.DiGraph()
	for u,v,data in x.edges(data=True):
		w = data['weight'] if 'weight' in data else 1.0
		if graph.has_edge(u,v):
			graph[u][v]['weight'] += w
		else:
			graph.add_edge(u, v, weight=w)
	return graph

MG0 = nx.MultiDiGraph(subgraph)
Graph0 = flatten_graph(MG0)

MG1 = nx.MultiDiGraph(subgraph)
MG1.add_edge('32545', '11844', weight=132, medium="reference")
MG1.add_edge('11844', '32545', weight=0, medium="reference") #as set, this places all references directed towards Henry VIII, giving him additional power in the network; changing the weight of each of these edges changes the direction in whaich the references are 'given'
nx.write_gexf(MG1, 'references_graph.gexf')
Graph1 = flatten_graph(MG1)
for a,b in nx.eigenvector_centrality(Graph1, weight='weight').items():
	if a == '32545':
		print('Thomas Cromwell eigenvector score', a, b)
	if a == '11844':
		print('Henry VIII eigenvector score', a, b)

#a test graph, if all edges (and letters) written by Henry VIII were reattributed to Thomas Cromwell
testgraph = []
for u,v in MG0.edges():
	if u == '11844' and v != '32545':
		testgraph.append(['32545', v])
	else:
		testgraph.append([u,v])
MG2 = nx.MultiDiGraph()
MG2.add_edges_from(testgraph, medium='letter', weight=1)

testgraph = flatten_graph(MG2)
nx.write_gexf(testgraph, 'replace_author.gexf')
graph_sub = testgraph.subgraph(H_TC_sub)
nx.set_node_attributes(graph_sub, sub_set(graph_sub), 'Neighbour')
nx.write_gexf(graph_sub, 'testgraph_sub.gexf')

for u,v in testgraph.edges():
	if [u,v] not in Graph0.edges():
		print(v, hist_name_dict[v]) #list of correspondents new to Thomas Cromwell's contacts if letters written by Henry VIII were reattributed

#a test graph, if all edges (and letters) written by Henry VIII, were considered jointly authored by Henry VIII and Thomas Cromwell
testgraph2 = []
for u,v in MG0.edges():
	if u == '11844' and v != '32545':
		testgraph2.append(['11844', v])
		testgraph2.append(['32545', v])
	else:
		testgraph2.append([u,v])
MG3 = nx.MultiDiGraph()
MG3.add_edges_from(testgraph2, medium='letter', weight=1)

testgraph2 = flatten_graph(MG3)
nx.write_gexf(testgraph2, 'shared_author.gexf')
graph_sub = testgraph2.subgraph(H_TC_sub)
nx.set_node_attributes(graph_sub, sub_set(graph_sub), 'Neighbour')
nx.write_gexf(graph_sub, 'testgraph2_sub.gexf')

eigen = nx.eigenvector_centrality(testgraph2, weight='weight')
for node,score in eigen.items():
	if node == '11844':
		print(node,score)

#
def name_eigen(graph_name):
	eigen = nx.eigenvector_centrality(graph_name, weight='weight')
	for node, score in eigen.items():
		if node == '11844':
			print('Henry VIII eigenvector score: ', score)
		if node == '32545':
			print('Thomas Cromwell eigenvector score: ', score)
			

print('ORGINAL')			
name_eigen(Graph0)
print('SHARED')
name_eigen(testgraph2)
print('REPLACE')
name_eigen(testgraph)
