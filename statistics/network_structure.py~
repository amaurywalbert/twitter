# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
# Script auxiliar para cálculos matemáticos que deve estar no mesmo diretório deste aqui.
import calc
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para gerar propriedades estruturais das redes-ego
## 
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def statistics(dataset_dir,output_dir,net,IsDir):
	print("\n######################################################################\n")
	print ("Dataset statistics - " +str(dataset_dir))
	n = []																										# Média dos nós por rede-ego
	e = []																										# Média das arestas por rede-ego	
	d = []																										# Média dos diametros por rede-ego
	cc = []																										# Média dos coeficientes de clusterings por rede-ego
	bc_n = []																									# média de betweenness centrality dos nós	
	bc_e = []																									# média de betweenness centrality das arestas
	
	i = 0
	for file in os.listdir(dataset_dir):
		i+=1 
		print ("Calculando propriedades para o ego %d..." % (i))
		
		G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)							   # load from a text file
		n.append(G.GetNodes())																				# Numero de vertices
		e.append(G.GetEdges())																				# Numero de arestas
		d.append(snap.GetBfsFullDiam(G, 100, IsDir))													# get diameter of G
#		cc.append(snap.GetClustCf(G))																		# clustering coefficient of G											

		Nodes = snap.TIntFltH()
		Edges = snap.TIntPrFltH()
		snap.GetBetweennessCentr(G, Nodes, Edges, 1.0, IsDir)
		_bc_n = []
		_bc_e = []
		for node in Nodes:
			_bc_n.append(Nodes[node])
		for edge in Edges:
			_bc_e.append(Edges[edge])
		result = calc.calcular(_bc_n)
		bc_n.append(result['media'])
		result = calc.calcular(_bc_e)
		bc_e.append(result['media'])	


#####################################################################################			
	
	N = calc.calcular_full(n)
	E = calc.calcular_full(e)
	D = calc.calcular_full(d)
	BC_N = calc.calcular_full(bc_n)
	BC_E = calc.calcular_full(bc_e)
#	CC = calc.calcular_full(cc)

	overview = {}
	overview['Nodes'] = N
	overview['Edges'] = E
	overview['Diameter'] = D
	overview['BetweennessCentrNodes'] = BC_N
	overview['BetweennessCentrEdges'] = BC_E
#	overview['ClusteringCoefficient'] = CC
	
	with open(output_dir+"properties.json") as f:
		f.write(json.dumps(overview))
		
		
	print("\n######################################################################\n")	
	print ("NET: %s -- Egos-net: %d" % (net,len(n)))
	print ("Nodes: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (N['media'],N['variancia'],N['desvio_padrao']))
	print ("Edges: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (E['media'],E['variancia'],E['desvio_padrao']))
	print ("Diameter: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (D['media'],D['variancia'],D['desvio_padrao']))
	print ("Betweenness Centr Nodes: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (BC_N['media'],BC_N['variancia'],BC_N['desvio_padrao']))
	print ("Betweenness Centr Edges: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (BC_E['media'],BC_E['variancia'],BC_E['desvio_padrao']))
#	print ("Clustering Coefficient: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (CC['media'],CC['variancia'],CC['desvio_padrao']))
	print("\n######################################################################\n")





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
	print"  3 - Mentions"
	
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
	else:
		isdir = True

	net = "n"+str(op)	

######################################################################		
######################################################################
	dataset_dir = "/home/amaury/graphs/"+str(net)+"/graphs_with_ego/"								############### Arquivo contendo arquivos com a lista de arestas das redes-ego

	if not os.path.isdir(dataset_dir):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir))
	else:
		output_dir = "/home/amaury/Dropbox/properties/"+str(net)+"/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		statistics(dataset_dir,output_dir,net,isdir)														# Inicia os cálculos...				
######################################################################		
######################################################################
#	dataset_dir2 = "/home/amaury/graphs/"+str(net)+"/graphs_without_ego/"						############### Arquivo contendo arquivos com a lista de arestas das redes-ego
#	if not os.path.isdir(dataset_dir2):
#		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
#	else:
#		output_dir2 = "/home/amaury/Dropbox/properties/"+str(net)+"/graphs_with_ego/"
#		if not os.path.exists(output_dir):
#			os.makedirs(output_dir)
#		statistics(dataset_dir2,output_dir2,net,isdir)													# Inicia os cálculos...	
######################################################################
######################################################################		

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

############################################
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################



######################################################################################################################


#Executa o método main
if __name__ == "__main__": main()