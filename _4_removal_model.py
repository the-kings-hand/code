import csv
import networkx as nx
from operator import itemgetter
import statistics
import numpy
import collections
from pathlib import Path
	
with open(str(Path.cwd()) + '/data/1534-1540.csv','r') as edgescsv34: #edgelist
	edgereader34 = csv.reader(edgescsv34)
	edges34 = [tuple(e) for e in edgereader34][1:]	

with open(str(Path.cwd()) + '/data/full_person_list.csv','r') as nodescsv: #nodelist
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]
	
Graph34 = nx.DiGraph()
Graph34.add_edges_from(edges34)

hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]	
nx.set_node_attributes(Graph34, hist_name_dict, 'historical_name')

UnG34 = nx.to_undirected(Graph34)

print('Number of Cut-Points', len(list(nx.articulation_points(UnG34))))

#SOURCES PATHS
Henry_all_sources = nx.descendants(Graph34,'11844')
print('Total sources', len(Henry_all_sources))

direct_Henry_source = list(Graph34.successors('11844'))
print('Total direct sources', len(direct_Henry_source))

Henry_all_source_paths_list = []	
for node in Henry_all_sources:
	Henry_all_source_paths_list.append([p for p in nx.all_shortest_paths(Graph34, source='11844', target=node)])
Henry_all_source_paths = []
for source in Henry_all_source_paths_list:
	for path in source:
		Henry_all_source_paths.append(path)
Henry_source_paths_test = []
for path in Henry_all_source_paths:
	if len(path) >= 3 and (path[1], path[-1]) not in Henry_source_paths_test:
		Henry_source_paths_test.append((path[1], path[-1]))
print('Unique Source Paths', len(Henry_source_paths_test))

HSP_intermediary_freq = []
for path in Henry_source_paths_test:
	HSP_intermediary_freq.append(path[0])
HSP_intermediary_freq = collections.Counter(HSP_intermediary_freq).most_common()

Cromwell_all_source_paths = []
for path in Henry_source_paths_test:
		for node in path:
			if node == '32545':
				Cromwell_all_source_paths.append(path)
Target_nodes = [item[-1] for item in Cromwell_all_source_paths]
print('Target nodes', len(Target_nodes))


#TARGET PATHS
Henry_all_targets = nx.ancestors(Graph34,'11844')
print('Total targets', len(Henry_all_targets))

direct_Henry_target = list(Graph34.predecessors('11844'))
print('Total direct targets', len(direct_Henry_target))

Henry_all_target_paths_list = []	
for node in Henry_all_targets:
	Henry_all_target_paths_list.append([p for p in nx.all_shortest_paths(Graph34, source=node, target='11844')])
Henry_all_target_paths = []
for target in Henry_all_target_paths_list:
	for path in target:
		Henry_all_target_paths.append(path)
Henry_target_paths_test = []
for path in Henry_all_target_paths:
	if len(path) >= 3 and (path[0], path[-2]) not in Henry_target_paths_test:
		Henry_target_paths_test.append([path[0], path[-2]])
print('Unique Target Paths', len(Henry_target_paths_test))

HTP_intermediary_freq = []
for path in Henry_target_paths_test:
	HTP_intermediary_freq.append(path[1])
HTP_intermediary_freq = collections.Counter(HTP_intermediary_freq).most_common()

Cromwell_all_target_paths = []
for path in Henry_target_paths_test:
	for node in path:
		if node == '32545':
			Cromwell_all_target_paths.append(path)
Source_nodes = [item[0] for item in Cromwell_all_target_paths]
print('Cromwell Source nodes', len(Source_nodes))

#Cut-Point Graph HSPs
CutSub = [node for node in Graph34]
CutSub.remove('32545') 
CutGraph = Graph34.subgraph(CutSub)

Cut_HSPs= []
for node in Target_nodes:
	if nx.has_path(CutGraph, source='11844', target=node) == True:
		Cut_HSPs.append([p for p in nx.all_shortest_paths(CutGraph, source='11844', target=node)])
print('Model surviving target nodes', len(Cut_HSPs))

Cut_HSPs_dup = []
for target in Cut_HSPs:
	for path in target:
		Cut_HSPs_dup.append(path)
Cut_HSPs_path = []
for path in Cut_HSPs_dup:
	if len(path) >= 3 and (path[1], path[-1]) not in Cut_HSPs_path:
		Cut_HSPs_path.append([path[1], path[-1]])
Cut_HSP_intermediaries = []
for path in Cut_HSPs_path:
	Cut_HSP_intermediaries.append(path[0])
Cut_HSP_intermediaries = collections.Counter(Cut_HSP_intermediaries).most_common()
print('CutGraph intermediaries', Cut_HSP_intermediaries[:10])

#Cut-Point Graph HTPs
Cut_HTPs = []
for node in Source_nodes:
	if nx.has_path(CutGraph, source=node, target='11844') == True:
		Cut_HTPs.append([p for p in nx.all_shortest_paths(CutGraph, source=node, target='11844')])
print('Model surviving source nodes', len(Cut_HTPs))

Cut_HTPs_dup = []
for target in Cut_HTPs:
	for path in target:
		Cut_HTPs_dup.append(path)
Cut_HTPs_path = []
for path in Cut_HTPs_dup:
	if len(path) >= 3 and (path[0], path[-2]) not in Cut_HTPs_path:
		Cut_HTPs_path.append([path[0], path[-2]])
Cut_HTP_intermediaries = []
for path in Cut_HTPs_path:
	Cut_HTP_intermediaries.append(path[1])
Cut_HTP_intermediaries = collections.Counter(Cut_HTP_intermediaries).most_common()
print('CutGraph HTP intermediaries', Cut_HTP_intermediaries[:10])