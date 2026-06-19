import csv
import networkx as nx
from operator import itemgetter
import statistics
import numpy
import collections
	
with open('1534-1540.csv','r') as edgescsv34: #edgelist
	edgereader34 = csv.reader(edgescsv34)
	edges34 = [tuple(e) for e in edgereader34][1:]	
	
with open('1540-1547.csv','r') as edgescsv47: #edgelist
	edgereader47 = csv.reader(edgescsv47) 
	edges47 = [tuple(e) for e in edgereader47][1:] 

with open('full_person_list.csv','r') as nodescsv: #nodelist
	nodereader = csv.reader(nodescsv)
	nodes = [n for n in nodereader][1:]
	
node_names = [n[0] for n in nodes]

G34 = nx.DiGraph()
G34.add_nodes_from(node_names)
G34.add_edges_from(edges34)

G47 = nx.DiGraph()
G47.add_nodes_from(node_names)
G47.add_edges_from(edges47)

hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]	
nx.set_node_attributes(G34, hist_name_dict, 'historical_name')
nx.set_node_attributes(G47, hist_name_dict, 'historical_name')

sublibrary47 = []
for node in G47:
	sublibrary47.append(node)
sublibrary47.remove('32545')
for node in sublibrary47:
	if G47.degree(node) < 1:
		sublibrary47.remove(node)
		
sublibrary34 = []
for node in G34:
	if G34.degree(node) >= 1:
		sublibrary34.append(node)

UnG47 = nx.to_undirected(G47)
Graph47 = G47.subgraph(sublibrary47)
UnGraph47 = nx.to_undirected(Graph47)

UnG34 = nx.to_undirected(G34)
Graph34 = G34.subgraph(sublibrary34)
UnGraph34 = nx.to_undirected(Graph34)

print('Number of Cut-Points 34-40', len(list(nx.articulation_points(UnGraph34))))
print('Number of Cut-Points 40-47', len(list(nx.articulation_points(UnGraph47))))

Henry_source_path = nx.single_source_shortest_path(Graph47, '11844') 
Henry_target_path = nx.single_target_shortest_path(Graph47, '11844')

#HSPs	
Henry_all_sources = []
for node in Graph47:
	if nx.has_path(Graph47, source='11844', target=node) == True:
		Henry_all_sources.append(node)
	else:
		continue
print('Total sources 47', len(Henry_all_sources))
direct_Henry_source = []
for node in Henry_all_sources:
	if nx.shortest_path_length(Graph47, source='11844', target=node) == 1:
		direct_Henry_source.append(node)
print('Paths direct from Henry to target Node', len(direct_Henry_source))

Henry_all_source_paths_list = []	
for node in Henry_all_sources:
	Henry_all_source_paths_list.append([p for p in nx.all_shortest_paths(Graph47, source='11844', target=node)])
Henry_all_source_paths = []
for source in Henry_all_source_paths_list:
	for path in source:
		Henry_all_source_paths.append(path)
print('Henry all source paths (duplicates)', len(Henry_all_source_paths))

Henry_source_paths_test = []
for path in Henry_all_source_paths:
	if len(path) >= 3 and (path[1], path[-1]) not in Henry_source_paths_test:
		Henry_source_paths_test.append((path[1], path[-1]))
print('Henry all source paths (intermediary no duplicates)', len(Henry_source_paths_test))
print('Total non-duplicate paths:', (len(direct_Henry_source))+(len(Henry_source_paths_test)))

HSP_intermediary_freq = []
for path in Henry_source_paths_test:
	HSP_intermediary_freq.append(path[0])
HSP_intermediary_freq = collections.Counter(HSP_intermediary_freq).most_common()
print('Henry Source Paths Intermediaries', HSP_intermediary_freq[:10])

#HTPs
Henry_all_targets = []
for node in Graph47:
	if nx.has_path(Graph47, source=node, target='11844') == True:
		Henry_all_targets.append(node)
	else:
		continue
print('Total targets 47', len(Henry_all_targets))
direct_Henry_target = []
for node in Henry_all_targets:
	if nx.shortest_path_length(Graph47, source=node, target='11844') == 1:
		direct_Henry_target.append(node)
print('Paths direct from source Node to Henry', len(direct_Henry_target))

Henry_all_target_paths_list = []	
for node in Henry_all_targets:
	Henry_all_target_paths_list.append([p for p in nx.all_shortest_paths(Graph47, source=node, target='11844')])
Henry_all_target_paths = []
for target in Henry_all_target_paths_list:
	for path in target:
		Henry_all_target_paths.append(path)
		
print('Henry all target paths (duplicates)', len(Henry_all_target_paths))
Henry_target_paths_test = []
for path in Henry_all_target_paths:
	if len(path) >= 3 and (path[0], path[-2]) not in Henry_target_paths_test:
		Henry_target_paths_test.append([path[0], path[-2]])
print('Henry all target paths (intermediary no duplicates)', len(Henry_target_paths_test))
print('Total non-duplicate paths:', (len(direct_Henry_target))+(len(Henry_target_paths_test)))

HTP_intermediary_freq = []
for path in Henry_target_paths_test:
	HTP_intermediary_freq.append(path[1])
HTP_intermediary_freq = collections.Counter(HTP_intermediary_freq).most_common()
print('Henry Target Paths Intermediaries', HTP_intermediary_freq[:10])

#SOURCES PATHS 34
Henry_all_sources_34 = []
for node in Graph34:
	if nx.has_path(Graph34, source='11844', target=node) == True:
		Henry_all_sources_34.append(node)
	else:
		continue
print('Total sources 34', len(Henry_all_sources_34))
direct_Henry_source_34 = []
for node in Henry_all_sources_34:
	if nx.shortest_path_length(Graph34, source='11844', target=node) == 1:
		direct_Henry_source_34.append(node)
print('Total direct sources', len(direct_Henry_source_34))
Henry_all_source_paths_list_34 = []	
for node in Henry_all_sources_34:
	Henry_all_source_paths_list_34.append([p for p in nx.all_shortest_paths(Graph34, source='11844', target=node)])
Henry_all_source_paths_34 = []
for source in Henry_all_source_paths_list_34:
	for path in source:
		Henry_all_source_paths_34.append(path)
Henry_source_paths_test_34 = []
for path in Henry_all_source_paths_34:
	if len(path) >= 3 and (path[1], path[-1]) not in Henry_source_paths_test_34:
		Henry_source_paths_test_34.append((path[1], path[-1]))
print('Unique Source Paths 34', len(Henry_source_paths_test_34))
HSP_intermediary_freq_34 = []
for path in Henry_source_paths_test_34:
	HSP_intermediary_freq_34.append(path[0])
HSP_intermediary_freq_34 = collections.Counter(HSP_intermediary_freq_34).most_common()

Cromwell_all_source_paths = []
for path in Henry_source_paths_test_34:
		for node in path:
			if node == '32545':
				Cromwell_all_source_paths.append(path)
Target_nodes = [item[-1] for item in Cromwell_all_source_paths]
print('Target nodes', len(Target_nodes))


#TARGET PATHS
Henry_all_targets_34 = []
for node in Graph34:
	if nx.has_path(Graph34, source=node, target='11844') == True:
		Henry_all_targets_34.append(node)
	else:
		continue
print('Total targets 34', len(Henry_all_targets_34))
direct_Henry_target_34 = []
for node in Henry_all_targets_34:
	if nx.shortest_path_length(Graph34, source=node, target='11844') == 1:
		direct_Henry_target_34.append(node)
print('Total direct targets', len(direct_Henry_target_34))
Henry_all_target_paths_list_34 = []	
for node in Henry_all_targets_34:
	Henry_all_target_paths_list_34.append([p for p in nx.all_shortest_paths(Graph34, source=node, target='11844')])
Henry_all_target_paths_34 = []
for target in Henry_all_target_paths_list_34:
	for path in target:
		Henry_all_target_paths_34.append(path)
Henry_target_paths_test_34 = []
for path in Henry_all_target_paths_34:
	if len(path) >= 3 and (path[0], path[-2]) not in Henry_target_paths_test_34:
		Henry_target_paths_test_34.append([path[0], path[-2]])
print('Unique Target Paths 34', len(Henry_target_paths_test_34))
HTP_intermediary_freq_34 = []
for path in Henry_target_paths_test_34:
	HTP_intermediary_freq_34.append(path[1])
HTP_intermediary_freq_34 = collections.Counter(HTP_intermediary_freq).most_common()

Cromwell_all_target_paths = []
for path in Henry_target_paths_test_34:
	for node in path:
		if node == '32545':
			Cromwell_all_target_paths.append(path)
Source_nodes = [item[0] for item in Cromwell_all_target_paths]
print('Cromwell Source nodes', len(Source_nodes))

#Cut-Point Graph HSPs
CutSub = []
for node in Graph34:
	if Graph34.degree(node) >= 1:
		CutSub.append(node)
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

Surviving_HSPs, Lost_HSPs, Dead_HSPs = [], [], []
for node in Target_nodes:
	if node in Graph47 and nx.has_path(Graph47, source='11844', target=node) == True:
		Surviving_HSPs.append(node)
	if node in Graph47 and nx.has_path(Graph47, source='11844', target=node) == False:
		Lost_HSPs.append(node)
	elif node not in Graph47:
		Dead_HSPs.append(node)
print('Surviving HSPs', len(Surviving_HSPs), '\nLost HSPs', len(Lost_HSPs), '\nNot in 47', len(Dead_HSPs))

Surprise_Survive_HSPs, Surprise_Lost_HSPs, Surprise_Dead_HSPs = [], [], []
for node in Surviving_HSPs:
	if nx.has_path(CutGraph, source='11844', target=node) == False:
		Surprise_Survive_HSPs.append(node)
for node in Lost_HSPs:
	if nx.has_path(CutGraph, source='11844', target=node) == True:
		Surprise_Lost_HSPs.append(node)
for node in Dead_HSPs:
	if nx.has_path(CutGraph, source='11844', target=node) == True:
		Surprise_Dead_HSPs.append(node)
print('Surprise Surviving HSPs', len(Surprise_Survive_HSPs), '\nSurprise Lost HSPs', len(Surprise_Lost_HSPs), '\nSurprise Not in 47', len(Surprise_Dead_HSPs))

direct_HSP = []
for node in Surviving_HSPs:
	if nx.shortest_path_length(Graph47, source='11844', target=node) == 1:
		direct_HSP.append(node)
print('HSPs to Direct', len(direct_HSP))
surviving_HSPs_list = []	
for node in Surviving_HSPs:
	surviving_HSPs_list.append([p for p in nx.all_shortest_paths(Graph47, source='11844', target=node)])
surviving_HSPs_paths = []
for target in surviving_HSPs_list:
	for path in target:
		surviving_HSPs_paths.append(path)
surviving_HSPs_paths_test = []
for path in surviving_HSPs_paths:
	if len(path) >= 3 and (path[1], path[-1]) not in surviving_HSPs_paths_test:
		surviving_HSPs_paths_test.append([path[1], path[-1]])
surviving_HSP_intermediary_freq = []
for path in surviving_HSPs_paths_test:
	surviving_HSP_intermediary_freq.append(path[0])
surviving_HSP_intermediary_freq = collections.Counter(surviving_HSP_intermediary_freq).most_common()
print('Surviving Henry Source Paths Intermediaries', surviving_HSP_intermediary_freq[:10])

Surprise_Survive_HSP_Intermediary_Freq = []
for path in surviving_HSPs_paths_test:
	if path[1] in Surprise_Survive_HSPs:
		Surprise_Survive_HSP_Intermediary_Freq.append(path[0])
Surprise_Survive_HSP_Intermediary_Freq = collections.Counter(Surprise_Survive_HSP_Intermediary_Freq).most_common()
print('Surprise Survive HSP Intermediaries', Surprise_Survive_HSP_Intermediary_Freq)

Surviving_Paths_HSPs = []
for path in Cut_HSPs_path:
	if path in surviving_HSPs_paths_test:
		Surviving_Paths_HSPs.append(path)
print('Surviving HSP paths', Surviving_Paths_HSPs)

New_Node_Intermediaries_HSP = []
for path in Henry_source_paths_test:
	if path[1] not in Graph34:
		New_Node_Intermediaries_HSP.append(path[0])
New_Node_Intermediaries_HSP = collections.Counter(New_Node_Intermediaries_HSP).most_common()
print('New Node Intermediaries', New_Node_Intermediaries_HSP[:10])

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

Surviving_HTPs, Lost_HTPs, Dead_HTPs = [], [], []
for node in Source_nodes:
	if node in Graph47 and nx.has_path(Graph47, source=node, target='11844') == True:
		Surviving_HTPs.append(node)
	if node in Graph47 and nx.has_path(Graph47, source=node, target='11844') == False:
		Lost_HTPs.append(node)
	elif node not in Graph47:
		Dead_HTPs.append(node)
print('\nSurviving HTPs', len(Surviving_HTPs), '\nLost HTPs', len(Lost_HTPs), '\nNot in 47', len(Dead_HTPs))

Surprise_Survive_HTPs, Surprise_Lost_HTPs, Surprise_Dead_HTPs = [], [], []
for node in Surviving_HTPs:
	if nx.has_path(CutGraph, source=node, target='11844') == False:
		Surprise_Survive_HTPs.append(node)
for node in Lost_HTPs:
	if nx.has_path(CutGraph, source=node, target='11844') == True:
		Surprise_Lost_HTPs.append(node)
for node in Dead_HTPs:
	if nx.has_path(CutGraph, source=node, target='11844') == True:
		Surprise_Dead_HTPs.append(node)
print('Surprise Surviving HTPs', len(Surprise_Survive_HTPs), '\nSurprise Lost HTPs', len(Surprise_Lost_HTPs), '\nSurprise Not in 47', len(Surprise_Dead_HTPs))

direct_HTP = []
for node in Surviving_HTPs:
	if nx.shortest_path_length(Graph47, source=node, target='11844') == 1:
		direct_HTP.append(node)
print('HTPs to Direct', len(direct_HTP))
surviving_HTPs_list = []	
for node in Surviving_HTPs:
	surviving_HTPs_list.append([p for p in nx.all_shortest_paths(Graph47, source=node, target='11844')])
surviving_HTPs_paths = []
for target in surviving_HTPs_list:
	for path in target:
		surviving_HTPs_paths.append(path)
surviving_HTPs_paths_test = []
for path in surviving_HTPs_paths:
	if len(path) >= 3 and (path[0], path[-2]) not in surviving_HTPs_paths_test:
		surviving_HTPs_paths_test.append([path[0], path[-2]])
surviving_HTP_intermediary_freq = []
for path in surviving_HTPs_paths_test:
	surviving_HTP_intermediary_freq.append(path[1])
surviving_HTP_intermediary_freq = collections.Counter(surviving_HTP_intermediary_freq).most_common()
print('Surviving Henry Target Paths Intermediaries', surviving_HTP_intermediary_freq[:10])

Surprise_Survive_HTP_Intermediary_Freq = []
for path in surviving_HTPs_paths_test:
	if path[0] in Surprise_Survive_HTPs:
		Surprise_Survive_HTP_Intermediary_Freq.append(path[1])
Surprise_Survive_HTP_Intermediary_Freq = collections.Counter(Surprise_Survive_HTP_Intermediary_Freq).most_common()
print('Surprise Survive HTP Intermediaries', Surprise_Survive_HTP_Intermediary_Freq)

Surviving_Paths_HTPs = []
for path in Cut_HTPs_path:
	if path in surviving_HTPs_paths_test:
		Surviving_Paths_HTPs.append(path)
print('Surviving HTP paths', Surviving_Paths_HTPs)

New_Node_Intermediaries_HTP = []
for path in Henry_target_paths_test:
	if path[0] not in Graph34:
		New_Node_Intermediaries_HTP.append(path[1])
New_Node_Intermediaries_HTP = collections.Counter(New_Node_Intermediaries_HTP).most_common()
print('New Node Intermediaries', New_Node_Intermediaries_HTP[:10])