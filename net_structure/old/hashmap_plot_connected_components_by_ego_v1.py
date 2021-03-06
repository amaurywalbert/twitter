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
##		Status - Versão 1 - Script para plotar dados sobre componentes conectados
## 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Carregar os dados as propriedades do dataset
#
######################################################################################################################################################################
def prepare(source_dir):
	print("\n######################################################################\n")

	cc = {}
	n_cc = {}
	cc_normal = {}
	for i in range(1,11):
		net="n"+str(i)
		if os.path.isfile(source_dir+net+"_connected_comp.json"):
			with open(source_dir+net+"_connected_comp.json", 'r') as f:
				overview = json.load(f)
				n_cc[net] = {'media':overview['N_ConnectedComponents']['media'],'std':overview['N_ConnectedComponents']['desvio_padrao']} 
				cc[net] = {'media':overview['Len_ConnectedComponents']['media'],'std':overview['Len_ConnectedComponents']['desvio_padrao']}
				cc_normal[net] = {'media':overview['Len_ConnectedComponents_Normal']['media'],'std':overview['Len_ConnectedComponents_Normal']['desvio_padrao']}
				
	data = {}
	data['Number_Connected_Components'] = n_cc
	data['Connected_Components'] = cc
	data['Normalized_Connected_Components'] = cc_normal
	return data
	print("\n######################################################################\n")

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
	
	source_dir1 = "/home/amaury/Dropbox/net_structure_hashmap/by_ego/connected_comp/graphs_with_ego/"
					
	data1 = prepare(source_dir1)
	
	source_dir2 = "/home/amaury/Dropbox/net_structure_hashmap/by_ego/connected_comp/graphs_without_ego/"
	
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

output = "/home/amaury/Dropbox/net_structure_hashmap_statistics/by_ego/connected_comp/"

#Executa o método main
if __name__ == "__main__": main()