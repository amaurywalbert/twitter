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
def net_structure(graphs_dir,dataset_dir,output_dir,net):
	os.system('clear')	
	print("\n######################################################################\n")
	print("\nScript para calculo da modularidade das comunidades detectadas\n")
		
	if os.path.isfile(str(output_dir)+"overview.json"):
		os.remove(str(output_dir)+"overview.json")	

	for threshold in os.listdir(dataset_dir):
		modularity = []																										# Vetor com a Média das modularidades de cada grafo	
		i = 0
		
		for file in os.listdir(dataset_dir+threshold):
			i+=1
			ego_id = file.split(".txt")
			ego_id = long(ego_id[0])
			communities = []																													# Armazenar as comunidades da rede-ego
						
			try:
				G = snap.LoadEdgeList(snap.PNGraph, str(graphs_dir)+str(ego_id)+".edge_list", 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
				n_edges = G.GetEdges()																										# Número de arestas do grafo
			except IOError:
				print ("\nERRO - Impossível carregar o grafo para o ego: "+str(ego_id)+"  --  "+str(graphs_dir)+str(ego_id)+".edge_list\n")
				

			try:
				with open(dataset_dir+str(threshold)+"/"+str(file), 'r') as f:
					for line in f:
						comm = []																					#Lista para armazenar as comunidades			
						a = line.split(' ')
						for item in a:
							if item != "\n":
								comm.append(item)
						communities.append(comm)						
			except Exception as e:
				print ("\nERRO - Impossível carregar as comunidades: "+dataset_dir+str(threshold)+"/"+str(file)+"\n")
				print e
			
			m_file = []																					# vetor de modularidade das comunidades do ego i
			for comm in communities:
				if comm is not None:
					Nodes = snap.TIntV()
					for nodeId in comm:
						if nodeId is not None and comm != ' ':						
							Nodes.Add(long(nodeId))			
					m_file.append(snap.GetModularity(G, Nodes, n_edges))						#Passar o número de arestas do grafo como parâmetro para agilizar o processo



			_m_file = calc.calcular(m_file)
			modularity.append(_m_file['media'])
	
			print ("Modularidade para o ego %d: %5.3f" % (i,_m_file['media']))
			print("######################################################################\n")	
		
		M = calc.calcular_full(modularity)
		overview = {'threshold': threshold, 'modularity':M}
		with open(str(output_dir)+"overview.json", 'a+') as f:
			f.write(json.dumps(overview)+"\n")
		
	print("\n######################################################################\n")	
	print ("Threshold: %s   ---   Modularity: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (threshold,M['media'],M['variancia'],M['desvio_padrao']))
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
	print" Script para calculo da modularidade das comunidades detectadas						"
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
	net = "n"+str(op)
	
	print "################################################################################"
	print"																											"
	print" Escolha o algoritmo usado na detecção das comunidades							"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - Copra"
	print"  2 - Oslom"		
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"
	else:
		print("Opção inválida! Saindo...")
		sys.exit()		
######################################################################
	
	
######################################################################		
######################################################################
	dataset_dir = "/home/amaury/communities/graphs_with_ego/"+str(alg)+"/full/"+str(net)+"/"	############### Arquivo contendo arquivos contendo as comunidades
	graphs_dir = "/home/amaury/graphs/"+str(net)+"/graphs_with_ego/"
	if not os.path.isdir(dataset_dir):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir))
	else:
		output_dir = "/home/amaury/Dropbox/communities/graphs_with_ego/"+str(alg)+"/full/"+str(net)+"/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)

		print ("\nCalcular modularidade... /home/amaury/communities/graphs_with_ego/"+str(alg)+"/full/"+str(net)+"/")
		net_structure(graphs_dir,dataset_dir,output_dir,net)														# Inicia os cálculos...				
######################################################################				
######################################################################
	dataset_dir2 = "/home/amaury/communities/graphs_with_ego/"+str(alg)+"/without_singletons/"+str(net)+"/"	############### Arquivo contendo arquivos contendo as comunidades
	graphs_dir2 = "/home/amaury/graphs/"+str(net)+"/graphs_with_ego/"
	if not os.path.isdir(dataset_dir2):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/communities/graphs_with_ego/"+str(alg)+"/without_singletons/"+str(net)+"/"
		if not os.path.exists(output_dir2):
			os.makedirs(output_dir2)
		print ("\nCalcular modularidade... /home/amaury/communities/graphs_with_ego/"+str(alg)+"/without_singletons/"+str(net)+"/")
		net_structure(graphs_dir2,dataset_dir2,output_dir2,net)														# Inicia os cálculos...			
######################################################################
######################################################################
	dataset_dir3 = "/home/amaury/communities/graphs_without_ego/"+str(alg)+"/full/"+str(net)+"/"	############### Arquivo contendo arquivos contendo as comunidades
	graphs_dir3 = "/home/amaury/graphs/"+str(net)+"/graphs_without_ego/"
	if not os.path.isdir(dataset_dir3):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir3))
	else:
		output_dir3 = "/home/amaury/Dropbox/communities/graphs_without_ego/"+str(alg)+"/full/"+str(net)+"/"
		if not os.path.exists(output_dir3):
			os.makedirs(output_dir3)
		print ("\nCalcular modularidade... /home/amaury/communities/graphs_without_ego/"+str(alg)+"/full/"+str(net)+"/")
		net_structure(graphs_dir3,dataset_dir3,output_dir3,net)													# Inicia os cálculos...	
######################################################################		
######################################################################
	dataset_dir4 = "/home/amaury/communities/graphs_without_ego/"+str(alg)+"/without_singletons/"+str(net)+"/"	############### Arquivo contendo arquivos contendo as comunidades
	graphs_dir4 = "/home/amaury/graphs/"+str(net)+"/graphs_without_ego/"
	if not os.path.isdir(dataset_dir4):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir4))
	else:
		output_dir4 = "/home/amaury/Dropbox/communities/graphs_without_ego/"+str(alg)+"/without_singletons/"+str(net)+"/"
		if not os.path.exists(output_dir4):
			os.makedirs(output_dir4)
		print ("\nCalcular modularidade... /home/amaury/communities/graphs_without_ego/"+str(alg)+"/without_singletons/"+str(net)+"/")
		net_structure(graphs_dir4,dataset_dir4,output_dir4,net)													# Inicia os cálculos...	
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