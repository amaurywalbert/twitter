# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
from math import*
# Script auxiliar para cálculos matemáticos que deve estar no mesmo diretório deste aqui.
import calc
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para gerar propriedades estruturais das redes-ego - Média dos nós e arestas de cada uma das 500 redes em cada modelo
## 
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def net_structure(dataset_dir,output_dir,net,IsDir, weight):
	print("\n######################################################################\n")
	print ("Dataset network structure - " +str(dataset_dir))
	n = []																										# Média dos nós por rede-ego
	e = []																										# Média das arestas por rede-ego	
	i = 0

	if os.path.isfile(str(output_dir)+str(net)+"_net_struct_basics.json"):
		print ("Arquivo já existe! "+str(output_dir)+str(net)+"_net_struct_basics.json")
	else:	
		for file in os.listdir(dataset_dir):
			i+=1 
			print (str(output_dir)+str(net)+" - Calculando propriedades para o ego "+str(i)+": "+str(file))
			if IsDir is True:
				G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			else:
				G = snap.LoadEdgeList(snap.PUNGraph, dataset_dir+file, 0, 1)					# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
			
#####################################################################################		

			n.append(G.GetNodes())																		# Numero de vértices
			e.append(G.GetEdges())																		# Numero de arestas
			nodes_stats = calc.calcular_full(n)
			edges_stats = calc.calcular_full(e)
			overview_basics = {'nodes':n,'nodes_stats':nodes_stats,'edges':e,'edges_statis':edges_stats}
	
#####################################################################################
	
		with open(str(output_dir)+str(net)+"_net_struct_basics.json", 'w') as f:
			f.write(json.dumps(overview_basics))
	
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