import csv
import networkx as nx
from operator import itemgetter
import statistics
import numpy
import collections
from pathlib import Path
import io
import sys
if __name__ == "__main__":
	text_trap = io.StringIO()
	sys.stdout = text_trap
from _4_Cromwell_model import *
sys.stdout = sys.__stdout__


with open(str(Path.cwd()) + '/data/1540-1547.csv','r') as edgescsv47: #edgelist
	edgereader47 = csv.reader(edgescsv47) 
	edges47 = [tuple(e) for e in edgereader47][1:] 

Graph47 = nx.DiGraph()
Graph47.add_edges_from(edges47)
Graph47.remove_node('32545')


hist_name_dict = {}
for node in nodes:
	hist_name_dict[node[0]] = node[1]	
nx.set_node_attributes(Graph47, hist_name_dict, 'historical_name')

#HSPs

HSP_47 = nx.descendants(Graph47, '11844')
print('Total Henry Targets 1540-1547 ', len(HSP_47))

Henry_all_sources_paths_list_47 = []	
for node in HSP_47:
	Henry_all_sources_paths_list_47.append([p for p in nx.all_shortest_paths(Graph47, source='11844', target=node) if len(p) >= 3])
Henry_all_sources_paths_47 = []
for source in Henry_all_sources_paths_list_47:
	for path in source:
		Henry_all_sources_paths_47.append(path)		
Henry_sources_paths_test_47 = []
for path in Henry_all_sources_paths_47:
	if (path[1], path[-1]) not in Henry_sources_paths_test_47:
		Henry_sources_paths_test_47.append([path[1], path[-1]])

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

direct_HSP_47 = list(Graph47.successors('11844'))
print('Direct HSPs 47', len(direct_HSP_47))
print('New Direct HTPS', len([n for n in direct_HSP_47 if n not in direct_Henry_source]))

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
for path in Henry_sources_paths_test_47:
	if path[1] not in Graph34:
		New_Node_Intermediaries_HSP.append(path[0])
New_Node_Intermediaries_HSP = collections.Counter(New_Node_Intermediaries_HSP).most_common()
print('New Node Intermediaries', New_Node_Intermediaries_HSP[:10])


#HTPs

HTP_47 = nx.ancestors(Graph47, '11844')
print('Total Henry sources 1540-1547 ', len(HTP_47))

Henry_all_target_paths_list_47 = []	
for node in HTP_47:
	Henry_all_target_paths_list_47.append([p for p in nx.all_shortest_paths(Graph47, source=node, target='11844') if len(p) >= 3])
Henry_all_target_paths_47 = []
for target in Henry_all_target_paths_list_47:
	for path in target:
		Henry_all_target_paths_47.append(path)		
Henry_target_paths_test_47 = []
for path in Henry_all_target_paths_47:
	if (path[0], path[-2]) not in Henry_target_paths_test_47:
		Henry_target_paths_test_47.append([path[0], path[-2]])

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

direct_HTP_47 = list(Graph47.predecessors('11844'))
print('Direct HTPs 47', len(direct_HTP_47))
print('New Direct HTPS', len([n for n in direct_HTP_47 if n not in direct_Henry_target]))

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
for path in Henry_target_paths_test_47:
	if path[0] not in Graph34:
		New_Node_Intermediaries_HTP.append(path[1])
New_Node_Intermediaries_HTP = collections.Counter(New_Node_Intermediaries_HTP).most_common()
print('New Node Intermediaries', New_Node_Intermediaries_HTP[:10])