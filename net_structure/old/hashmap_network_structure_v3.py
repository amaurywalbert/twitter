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
##		Status - Versão 1 - Script para gerar propriedades estruturais dos modelos. Média por modelo (considera todos os egos...)
##					Versão 2 - Normalizei a centralidade de intermediação
##					Versão 3 - Acrescentei propriedades basicas - Vetor com nós e arestas, para que se possa plotar ver a distribuição , justificando o uso da média ou não.
## 
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
		nodes = {}																									# chave_valor para ego_id e numero de vertices
		edges = {}																									# chave_valor para ego_id e numero de arestas
		d = []																										# Média dos diametros por rede-ego
		cc = []																										# Média dos Close Centrality																				
		bc_n = []																									# média de betweenness centrality dos nós	
		bc_e = []																									# média de betweenness centrality das arestas
		degree = {}																									# chave-valor para armazenar "grau dos nós - numero de nós com este grau"
		i = 0
	
		

		for file in os.listdir(dataset_dir):
			ego_id = file.split(".edge_list")
			ego_id = long(ego_id[0])
			i+=1 
			print (str(output_dir)+str(net)+" - Calculando propriedades para o ego "+str(i)+": "+str(file))
			if IsDir is True:
				G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			else:
				G = snap.LoadEdgeList(snap.PUNGraph, dataset_dir+file, 0, 1)					# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			
#####################################################################################		
			n_nodes = G.GetNodes()
			n_edges = G.GetEdges()		
			nodes[ego_id] = n_nodes												#Dicionário ego_id = vertices
			edges[ego_id] = n_edges 
			n.append(n_nodes)																		# Numero de vértices
			e.append(n_edges)																		# Número de Arestas

#####################################################################################
			if n_edges == 0:
				a = 0
				d.append(a)
				cc.append(a)
				bc_n.append(a)
				bc_e.append(a)	
			else:
				d.append(snap.GetBfsFullDiam(G, 100, IsDir))											# get diameter of G
		
#####################################################################################
	
				Normalized = True
				for NI in G.Nodes():
					cc.append(snap.GetClosenessCentr(G, NI.GetId(), Normalized, IsDir)) #get a closeness centrality
		
#####################################################################################

			if n_edges == 0 or n_nodes < 3:
				bc_n.append(n_edges)
				bc_e.append(n_edges)	
			else:
				Nodes = snap.TIntFltH()
				Edges = snap.TIntPrFltH()
				snap.GetBetweennessCentr(G, Nodes, Edges, 1.0, IsDir)								#Betweenness centrality Nodes and Edges
				
				if IsDir is True:
					max_betweenneess = (n_nodes-1)*(n_nodes-2)
				else:
					max_betweenneess = ((n_nodes-1)*(n_nodes-2))/2
			
				for node in Nodes:
					bc_n_normalized = float(Nodes[node]) / float(max_betweenneess)
					bc_n.append(bc_n_normalized)

				for edge in Edges:
					bc_e_normalized = float(Edges[edge]) / float(max_betweenneess)
					bc_e.append(bc_e_normalized)

#####################################################################################
		
				DegToCntV = snap.TIntPrV()
				snap.GetDegCnt(G, DegToCntV)																#Grau de cada nó em cada rede-ego
				for item in DegToCntV:
					k = item.GetVal1()
					v = item.GetVal2()
					if degree.has_key(k):
						degree[k] = degree[k]+v 
					else:
						degree[k] = v

#####################################################################################

			print	n[i-1], e[i-1], d[i-1], cc[i-1], bc_n[i-1], bc_e[i-1]
			print 
#####################################################################################		
		
		
		N = calc.calcular_full(n)
		E = calc.calcular_full(e)
	
		histogram.histogram(degree,output_dir+"histogram"+"/", N['soma'],net)

		D = calc.calcular_full(d)

		CC = calc.calcular_full(cc)
	
	
		BC_N = calc.calcular_full(bc_n)
		BC_E = calc.calcular_full(bc_e)

	
		overview = {}
		overview['Nodes'] = N
		overview['Edges'] = E
		overview['Diameter'] = D
		overview['CloseCentr'] = CC
		overview['BetweennessCentrNodes'] = BC_N
		overview['BetweennessCentrEdges'] = BC_E
	
		nodes_stats = calc.calcular_full(n)
		edges_stats = calc.calcular_full(e)
		overview_basics = {'nodes':n,'nodes_stats':nodes_stats,'edges':e,'edges_stats':edges_stats}

		output_basics = output_dir+"/"+str(net)+"/"
		if not os.path.exists(output_basics):
			os.makedirs(output_basics)
				
		with open(str(output_basics)+str(net)+"_nodes.json", 'w') as f:
			f.write(json.dumps(nodes))
		with open(str(output_basics)+str(net)+"_edges.json", 'w') as f:
			f.write(json.dumps(edges))

		with open(str(output_basics)+str(net)+"_overview.json", 'w') as f:
			f.write(json.dumps(overview_basics))
			
		with open(str(output_dir)+str(net)+"_net_struct.json", 'w') as f:
			f.write(json.dumps(overview))
	
		with open(str(output_dir)+str(net)+"_net_struct.txt", 'w') as f:
			f.write("\n######################################################################\n")	
			f.write ("NET: %s -- Ego-nets: %d \n" % (net,len(n)))
			f.write ("Nodes: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (N['media'],N['variancia'],N['desvio_padrao']))
			f.write ("Edges: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (E['media'],E['variancia'],E['desvio_padrao']))
			f.write ("Diameter: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (D['media'],D['variancia'],D['desvio_padrao']))
			f.write ("CloseCentr: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CC['media'],CC['variancia'],CC['desvio_padrao']))
			f.write ("Betweenness Centr Nodes: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (BC_N['media'],BC_N['variancia'],BC_N['desvio_padrao']))
			f.write ("Betweenness Centr Edges: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (BC_E['media'],BC_E['variancia'],BC_E['desvio_padrao']))
			f.write("\n######################################################################\n")


#Average Degree - Olhar no oslom pq parece que já tem....
#Average clustering coefficient	0.5653
#Number of triangles	13082506
#Fraction of closed triangles	0.06415
#Diameter (longest shortest path)	7
#90-percentile effective diameter	4.5

#Dataset			N				E				C				K				S				A
#Twitter			125,120		2,248,406	3,140			33,569		15.54			0.39

#DATASET STATISTICS.
#N: NUMBER OF NODES,
#E: NUMBER OF EDGES,
#C: NUMBER OF COMMUNITIES,
#K: NUMBER OF NODE ATTRIBUTES,
#S: AVERAGE COMMUNITY SIZE,
#A: COMMUNITY MEMBERSHIPS PER NODE
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
		output_dir = "/home/amaury/Dropbox/net_structure_hashmap/snap/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		net_structure(dataset_dir,output_dir,net,isdir,weight)													# Inicia os cálculos...				
######################################################################		
######################################################################
	dataset_dir2 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_without_ego/"						############### Arquivo contendo arquivos com a lista de arestas das redes-ego
	if not os.path.isdir(dataset_dir2):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/net_structure_hashmap/snap/graphs_without_ego/"
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