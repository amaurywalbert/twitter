# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
# Script auxiliar para cálculos matemáticos que deve estar no mesmo diretório deste aqui.
import calc
# Script auxiliar para gerar histogramas
import histogram
import networkx as nx
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para gerar propriedades estruturais das redes-ego
## 
##												v2 - Normalizei a centralidade de intermediação;
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def net_structure(dataset_dir,output_dir,net,IsDir, weight):
	print("\n######################################################################\n")
	if os.path.isfile(str(output_dir)+str(net)+"_net_struct.json"):
		print ("Arquivo já existe: "+str(output_dir)+str(net)+"_net_struct.json")
	else:

		print ("Dataset network structure - " +str(dataset_dir))
		n = []																										# Média dos nós por rede-ego
		e = []																										# Média das arestas por rede-ego	

		bc_n = []																									# média de betweenness centrality dos nós	
		bc_e = []																									# média de betweenness centrality das arestas

		i = 0


		for file in os.listdir(dataset_dir):
			i+=1 
			print (str(output_dir)+str(net)+" - Calculando propriedades para o ego "+str(i)+": "+str(file))
			if IsDir is True:
				G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			else:
				G = snap.LoadEdgeList(snap.PUNGraph, dataset_dir+file, 0, 1)					# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			
#####################################################################################		

			n.append(G.GetNodes())																		# Numero de vertices
			e.append(G.GetEdges())																		# Numero de arestas
			n_nodes = G.GetNodes()	
			n_edges = G.GetEdges()
	
#####################################################################################
			if n_edges == 0 or n_nodes < 3:
				bc_n.append(n_edges)
				bc_e.append(n_edges)	
			else:
				Nodes = snap.TIntFltH()
				Edges = snap.TIntPrFltH()
				snap.GetBetweennessCentr(G, Nodes, Edges, 1.0, IsDir)								#Betweenness centrality Nodes and Edges
				_bc_n = []
				_bc_e = []
				if IsDir is True:
					max_betweenneess = (n_nodes-1)*(n_nodes-2)
				else:
					max_betweenneess = ((n_nodes-1)*(n_nodes-2))/2
			
				for node in Nodes:
					bc_n_normalized = float(Nodes[node]) / float(max_betweenneess)
					_bc_n.append(bc_n_normalized)

				for edge in Edges:
					bc_e_normalized = float(Edges[edge]) / float(max_betweenneess)
					_bc_e.append(bc_e_normalized)
				result = calc.calcular(_bc_n)
				bc_n.append(result['media'])
				result = calc.calcular(_bc_e)
				bc_e.append(result['media'])	

#####################################################################################

	
		BC_N = calc.calcular_full(bc_n)
		BC_E = calc.calcular_full(bc_e)

	
		overview = {}
	
		overview['BetweennessCentrNodes'] = BC_N
		overview['BetweennessCentrEdges'] = BC_E

	
		with open(str(output_dir)+str(net)+"_net_struct.json", 'w') as f:
			f.write(json.dumps(overview))
	
		with open(str(output_dir)+str(net)+"_net_struct.txt", 'w') as f:
			f.write("\n######################################################################\n")
			f.write ("Betweenness Centr Nodes: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (BC_N['media'],BC_N['variancia'],BC_N['desvio_padrao']))
			f.write ("Betweenness Centr Edges: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (BC_E['media'],BC_E['variancia'],BC_E['desvio_padrao']))
			f.write("\n######################################################################\n")


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
	print"  1 - Follow"
	print"  9 - Follwowers"
	print"  2 - Retweets"
	print"  3 - Likes"
	print"  4 - Mentions"
	
	print " "
	print"  5 - Co-Follow"
	print" 10 - Co-Followers"				
	print"  6 - Co-Retweets"
	print"  7 - Co-Likes"
	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))


	if op in (5,6,7,8,10):																						# Testar se é um grafo direcionado ou não
		isdir = False
	elif op in (1,2,3,4,9):
		isdir = True 
	else:
		print("Opção inválida! Saindo...")
		sys.exit()

	if op == 1 or op == 9:																						# Testar se é um grafo direcionado ou não
		weight = False
	else:
		weight = True
######################################################################
	
	net = "n"+str(op)	

######################################################################		
######################################################################
	dataset_dir = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_with_ego/"								############### Arquivo contendo arquivos com a lista de arestas das redes-ego

	if not os.path.isdir(dataset_dir):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir))
	else:
		output_dir = "/home/amaury/Dropbox/net_structure_hashmap/snap_v2/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		net_structure(dataset_dir,output_dir,net,isdir,weight)													# Inicia os cálculos...				
######################################################################		
######################################################################
	dataset_dir2 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_without_ego/"						############### Arquivo contendo arquivos com a lista de arestas das redes-ego
	if not os.path.isdir(dataset_dir2):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/net_structure_hashmap/snap_v2/graphs_without_ego/"
		if not os.path.exists(output_dir2):
			os.makedirs(output_dir2)
		net_structure(dataset_dir2,output_dir2,net,isdir,weight)												# Inicia os cálculos...	
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


#Executa o método main
if __name__ == "__main__": main()