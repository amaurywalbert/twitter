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
##		Status - Versão 1 - Script para verificar por componentes conectados. NA VERSÂO "BY MODEL" consideramos a média de todo o modelo, e não fazemos média por ego.
## 
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def net_structure(dataset_dir,output_dir,net,IsDir, weight):
	print("\n######################################################################\n")
	if os.path.isfile(str(output_dir)+str(net)+"_connected_comp.json"):
		print ("Arquivo já existe: "+str(output_dir)+str(net)+"_connected_comp.json")
	else:

		print ("Componentes conectados - " +str(dataset_dir))
											
		cc = []																										# Vetor com tamanho de todos os componentes conectados por modelo
		cc_normal = []																								# Vetor com tamanho de todos os componentes conectados por modelo - Cada tamanho é normalizado pelo número de vértices da rede em que está o componente.
		n_cc = 0																										# Número de componentes conectados por modelo
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

			n_nodes = G.GetNodes()												# Número de vértices
			n_edges = G.GetEdges()												# Número de arestas
		
#####################################################################################
			if n_edges == 0:
				a = 0
				cc.append(a)
				cc_normal.append(a)
				n_cc.append(a)
				print ("Nenhuma aresta encontrada para a rede-ego "+str(i)+" - ("+str(file))				
			else:
				Components = snap.TCnComV()
				snap.GetWccs(G, Components)
				for CnCom in Components:
					cc.append(CnCom.Len())
					b = float(CnCom.Len())/float(n_nodes)
					cc_normal.append(b)
					n_cc+=1			

		AVG_CC = float(n_cc)/float(i)						# Número de componentes conectados dividido pelo número de egos, pra saber a média de componentes conectados por ego.
		CC = calc.calcular_full(cc)
		CC_NORMAL = calc.calcular_full(cc_normal)			
	
		overview = {}
		overview['Len_ConnectedComponents'] = CC
		overview['Len_ConnectedComponents_Normal'] = CC_NORMAL
		overview['AVG_ConnectedComponents'] = AVG_CC


		
		with open(str(output_dir)+str(net)+"_connected_comp.json", 'w') as f:
			f.write(json.dumps(overview))
	
		with open(str(output_dir)+str(net)+"_connected_comp.txt", 'w') as f:
			f.write("\n######################################################################\n")	
			f.write ("AVG_Connected_Comp: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (AVG_CC['media'],AVG_CC['variancia'],AVG_CC['desvio_padrao']))			
			f.write ("Length_Connected_Comp: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CC['media'],CC['variancia'],CC['desvio_padrao']))
			f.write ("Length_Connected_Comp_Normalized: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CC_NORMAL['media'],CC_NORMAL['variancia'],CC_NORMAL['desvio_padrao']))
			f.write("\n######################################################################\n")

		print ("\n######################################################################\n")	
		print ("AVG_Connected_Comp: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (AVG_CC['media'],AVG_CC['variancia'],AVG_CC['desvio_padrao']))
		print ("Length_Connected_Comp: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CC['media'],CC['variancia'],CC['desvio_padrao']))
		print ("Length_Connected_Comp_Normalized: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f \n"% (CC_NORMAL['media'],CC_NORMAL['variancia'],CC_NORMAL['desvio_padrao']))
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
		output_dir = "/home/amaury/Dropbox/net_structure_hashmap/by_model/connected_comp/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		net_structure(dataset_dir,output_dir,net,isdir,weight)													# Inicia os cálculos...				
######################################################################		
######################################################################
	dataset_dir2 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_without_ego/"						############### Arquivo contendo arquivos com a lista de arestas das redes-ego
	if not os.path.isdir(dataset_dir2):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/net_structure_hashmap/by_model/connected_comp/graphs_without_ego/"
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