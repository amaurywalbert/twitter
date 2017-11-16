# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
# Script auxiliar para cálculos matemáticos que deve estar no mesmo diretório deste aqui.
import plot_metrics
# Script auxiliar para gerar histogramas
import histogram
import networkx as nx
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar  propriedades estruturais das redes-ego
## 
##												ERRRO DE ALOCAÇÃO DE MEMÓRIA!!!!!
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def prepare(source_dir):
	print("\n######################################################################\n")
	
	nodes = {}
	edges = {}
	diameter = {}
	closecentr = {}
	bet_centr_nodes = {}
	bet_centr_edges = {}
	modularity = {}
	for i in range(1,11):
		net="n"+str(i)
		if os.path.isfile(source_dir+net+"_net_struct.json"):
			with open(source_dir+net+"_net_struct.json", 'r') as f:
				overview = json.load(f)
				nodes[net] = overview['Nodes']['media']
				edges[net] = overview['Edges']['media']
				diameter[net] = overview['Diameter']['media']
				closecentr[net] = overview['CloseCentr']['media']
				bet_centr_nodes[net] = overview['BetweennessCentrNodes']['media']
				bet_centr_edges[net] = overview['BetweennessCentrEdges']['media']
				modularity[net] = overview['Modularity']['media']

	data = {}
	data['Nodes'] = nodes
	data['Edges'] = edges
	data['Diameter'] = diameter
	data['Close Centrality'] = closecentr
	data['Betweenness Centrality Nodes'] = bet_centr_nodes
	data['Betweenness Centrality Edges'] = bet_centr_edges
	data['Modularity'] = modularity
	return data


######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" Script para apresentação de propriedades do dataset (rede-ego)							"
	print"																											"
	print"#################################################################################"
	print
	
	source_dir1 = "/home/amaury/Dropbox/net_structure_hashmap/graphs_with_ego/"
	
	data1 = prepare(source_dir1)
	
	source_dir2 = "/home/amaury/Dropbox/net_structure_hashmap/graphs_without_ego/"
	
	data2 = prepare(source_dir2)
	
			
	if data1 is not None and data2 is not None:
		for k,v in data1.iteritems():		
			metric = k
			plot_metrics.plot_bars_full(output,data1[k],data2[k],metric)		
				
######################################################################
######################################################################		

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/net_structure_hashmap/"
output = "/home/amaury/Dropbox/net_statistics_hashmap/"

#Executa o método main
if __name__ == "__main__": main()