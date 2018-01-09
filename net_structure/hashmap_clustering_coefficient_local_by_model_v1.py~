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
##		Status - Versão 1 - Script para gerar coeficiente de clustering por ego. Nesse cálculo a média que é armazenada já é a média do modelo.
## 
##												ERRRO DE ALOCAÇÃO DE MEMÓRIA!!!!!
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def net_structure(dataset_dir,output_dir,net,IsDir, weight):
	print("\n######################################################################\n")
	if os.path.isfile(str(output_dir)+str(net)+"_clustering_coef.json"):
		print ("Arquivo já existe: "+str(output_dir)+str(net)+"_clustering_coef.json")
	else:

		print ("Dataset clustering coefficient - " +str(dataset_dir))
											
		cf = []																										# Média dos coeficientes de clusterings por rede-ego
		gcf = []																										# Média usando opção local
		n = []																										# vetor com número de vértices para cada rede-ego																									
		e = []																										# vetor com número de arestas para cada rede-ego
		i = 0

		for file in os.listdir(dataset_dir):

			i+=1 
			print (str(output_dir)+str(net)+"/"+str(file)+" - Calculando propriedades para o ego "+str(i)+": "+str(file))
			if IsDir is True:
				G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			else:
				G = snap.LoadEdgeList(snap.PUNGraph, dataset_dir+file, 0, 1)					# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
#			G.Dump()
#			time.sleep(5)

#####################################################################################		

			n.append(G.GetNodes())																		# Numero de vertices
			e.append(G.GetEdges())																		# Numero de arestas
			n_nodes = G.GetNodes()	
			n_edges = G.GetEdges()
		
#####################################################################################
			if n_edges == 0:
				a = 0
				cf.append(a)
				print ("Nenhuma aresta encontrada para a rede-ego "+str(i)+" - ("+str(file))				
			else:	
				NIdCCfH = snap.TIntFltH()
				snap.GetNodeClustCf(G, NIdCCfH)
				for item in NIdCCfH:
					cf.append(NIdCCfH[item])																# Clusterinf Coefficient
				
				print ("Calculando Clustering Coef para a rede-ego: "+str(i))
				print  				

		CF = calc.calcular_full(cf)
	
		overview = {}
		overview['ClusteringCoefficient'] = CF


		
		with open(str(output_dir)+str(net)+"_clustering_coef.json", 'w') as f:
			f.write(json.dumps(overview))
	
		with open(str(output_dir)+str(net)+"_clustering_coef.txt", 'w') as f:
			f.write("\n######################################################################\n")	
			f.write ("Clustering Coef: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CF['media'],CF['variancia'],CF['desvio_padrao']))
			f.write("\n######################################################################\n")

		print ("\n######################################################################\n")	
		print ("Clustering Coef: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CF['media'],CF['variancia'],CF['desvio_padrao']))
		print ("\n######################################################################\n")

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
	print" Script para cálculo do coeficiente de agrupamento do dataset (rede-ego)							"
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
		output_dir = "/home/amaury/Dropbox/net_structure_hashmap/by_model/clustering_coefficient_local/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		net_structure(dataset_dir,output_dir,net,isdir,weight)													# Inicia os cálculos...				
######################################################################		
######################################################################
	dataset_dir2 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_without_ego/"						############### Arquivo contendo arquivos com a lista de arestas das redes-ego
	if not os.path.isdir(dataset_dir2):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/net_structure_hashmap/by_model/clustering_coefficient_local/graphs_without_ego/"
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