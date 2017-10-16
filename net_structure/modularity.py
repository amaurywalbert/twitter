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
##		Status - Versão 1 - Script para calcular modularidade da rede-ego
## 
######################################################################################################################################################################


######################################################################################################################################################################
#
# Armazenar as propriedades do dataset
#
######################################################################################################################################################################
def net_structure(dataset_dir,output_dir,net,IsDir):
	print("\n######################################################################\n")
	print ("Dataset Modularity - " +str(dataset_dir))

	m = []																										# Média das modularidades de cada grafo	
	
	i = 0
	for file in os.listdir(dataset_dir):
		i+=1 
		G = snap.LoadEdgeList(snap.PUNGraph, dataset_dir+file, 0, 1)					# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')

#####################################################################################

		CmtyV = snap.TCnComV()
		modularity = snap.CommunityCNM(G, CmtyV)												# Roda o CNM e pega a modularidade- Desconsidera direção das arestas... 
		m.append(modularity)
		print ("Calculando modularidade para o ego %d: %5.3f" % (i,modularity))
#####################################################################################
	
	
	M = calc.calcular_full(m)


	overview = {}
	overview['Modularity'] = M

	
	with open(str(output_dir)+str(net)+"_modularity.json") as f:
		f.write(json.dumps(overview))
		
		
	print("\n######################################################################\n")	
	print ("NET: %s -- Egos-net: %d" % (net,len(n)))
	print ("Modularity: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (M['media'],M['variancia'],M['desvio_padrao']))

	print("\n######################################################################\n")

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
	elif op in (1,2,3,4,9):
		isdir = True 
	else:
		print("Opção inválida! Saindo...")
		sys.exit()
######################################################################
	
	net = "n"+str(op)	

######################################################################		
######################################################################
	dataset_dir = "/home/amaury/graphs/"+str(net)+"/graphs_with_ego/"								############### Arquivo contendo arquivos com a lista de arestas das redes-ego

	if not os.path.isdir(dataset_dir):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir))
	else:
		output_dir = "/home/amaury/Dropbox/net_structure/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		net_structure(dataset_dir,output_dir,net,isdir)														# Inicia os cálculos...				
######################################################################		
######################################################################
#	dataset_dir2 = "/home/amaury/graphs/"+str(net)+"/graphs_without_ego/"						############### Arquivo contendo arquivos com a lista de arestas das redes-ego
#	if not os.path.isdir(dataset_dir2):
#		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
#	else:
#		output_dir = "/home/amaury/Dropbox/net_structure/graphs_without_ego/"
#		if not os.path.exists(output_dir):
#			os.makedirs(output_dir)
#		net_structure(dataset_dir2,output_dir2,net,isdir)													# Inicia os cálculos...	
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