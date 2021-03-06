# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Two-Sided Kolmogorov-Smirnov Tests - Testar se dois grupos de amostras foram tirados de conjuntos com a mesma distribuição. 
##									Compara de dois em dois.EX: 03 folds - A,B,C - compara AeB, AeC, e BeC. 
##									Teste realizado entre os conjuntos de alters de cada modelo da rede ego.
## 
######################################################################################################################################################################

######################################################################################################################################################################
#
#Two-Sided Kolmogorov-Smirnov Tests
#
######################################################################################################################################################################
def ks_test(data1,data2):
	statistical, p_value = stats.ks_2samp(data1, data2)
	print statistical, p_value


def prepare(graphs_dir,output_dir,net,isdir):


	for file in os.listdir(graphs_dir):
		i+=1 
		print (str(graphs_dir)+str(file)+" - Recuperando grafo: "+str(i))
		if IsDir is True:
			G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
		else:
			G = snap.LoadEdgeList(snap.PUNGraph, dataset_dir+file, 0, 1)					# load from a text file - pode exigir um separador
			
		n_nodes = G.GetNodes()												# Número de vértices
		n_edges = G.GetEdges()												# Número de arestas
		
		#Verificar se é com esse teste mesmo...
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
	print" Script para cálculo de significância estatística dos modelos							"
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

######################################################################
	
	net = "n"+str(op)	

######################################################################		
######################################################################
	graphs_dir = "/home/amaury/graphs/"+str(net)+"/graphs_with_ego/"								# Diretório dos grafos - antes da conversão com hashmap

	if not os.path.isdir(graphs_dir):
		print("Diretório dos grafos não encontrado: "+str(graphs_dir))
	else:
		output_dir = "/home/amaury/Dropbox/ks_test/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		prepare(graphs_dir,output_dir,net,isdir)															# Inicia os cálculos...				
######################################################################		
######################################################################
	graphs_dir2 = "/home/amaury/graphs/"+str(net)+"/graphs_without_ego/"							# Diretório dos grafos - antes da conversão com hashmap
	if not os.path.isdir(graphs_dir2):
		print("Diretório dos grafos não encontrado: "+str(graphs_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/ks_test/graphs_with_ego/"
		if not os.path.exists(output_dir2):
			os.makedirs(output_dir2)
		prepare(graphs_dir2,output_dir2,net,isdir)														# Inicia os cálculos...	
		

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