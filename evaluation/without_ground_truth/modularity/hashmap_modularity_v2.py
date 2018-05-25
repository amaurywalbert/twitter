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
def net_structure(dataset_dir,output_dir,graph_type,metric,net,alg):
	os.system('clear')	
	print("\n######################################################################\n")
	print("\nScript para cálculo da modularidade das comunidades detectadas\n")

	if alg == "infomap":
		graphs_dir = "/home/amaury/graphs_hashmap_infomap/"+str(net)+"/"+str(graph_type)+"/"
	elif alg == "infomap_without_weight":
		graphs_dir = "/home/amaury/graphs_hashmap_infomap_without_weight/"+str(net)+"/"+str(graph_type)+"/"	
	else:
		graphs_dir = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(graph_type)+"/"
		
	if not os.path.exists(graphs_dir):
		print ("Diretório não encontrado: "+str(graphs_dir))
		
	else:
		print("\n######################################################################\n")
		print("\nScript para cálculo da modularidade das comunidades detectadas - Rede "+str(net)+"\n")	

		if not os.path.isdir(dataset_dir+str(net)+"/"):
			print ("Diretório com avaliações da rede "+str(net)+" não encontrado: "+str(dataset_dir+str(net)+"/"))
		else:	
			for threshold in os.listdir(dataset_dir+str(net)+"/"):
				if os.path.isfile(str(output_dir)+str(threshold)+".json"):
					print ("Arquivo de destino já existe. "+str(output_dir)+str(threshold)+".json")
				else:
					 				
					modularity = []																			# Vetor com a Média das modularidades de cada grafo
					modularity_data = {}																		# Dicionário com o ego e as modularidades para cada comunidade	
					i = 0
			
					for file in os.listdir(dataset_dir+str(net)+"/"+str(threshold)+"/"):
						i+=1
						ego_id = file.split(".txt")
						ego_id = long(ego_id[0])
						communities = []																													# Armazenar as comunidades da rede-ego
						m_file = []																					# vetor de modularidade das comunidades do ego i
						
						
						try:
							G = snap.LoadEdgeList(snap.PNGraph, str(graphs_dir)+str(ego_id)+".edge_list", 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
							n_edges = G.GetEdges()																										# Número de arestas do grafo
						
							if n_edges == 0:
								a = 0							
								m_file.append(a)
							else:
								try:
									with open(dataset_dir+str(net)+"/"+str(threshold)+"/"+str(file), 'r') as f:
										for line in f:
											comm = []																					#Lista para armazenar as comunidades			
											a = line.split(' ')
											for item in a:
												if item != "\n":
													comm.append(item)
											communities.append(comm)						
								except Exception as e:
									print ("\nERRO - Impossível carregar as comunidades: "+dataset_dir+str(net)+"/"+str(threshold)+"/"+str(file)+"\n")
									print e
				
						
								for comm in communities:
									if comm is not None:
										Nodes = snap.TIntV()
										for nodeId in comm:
											if nodeId is not None:						
												Nodes.Add(long(nodeId))			
										m_file.append(snap.GetModularity(G, Nodes, n_edges))						#Passar o número de arestas do grafo como parâmetro para agilizar o processo					

						except Exception as e:	
							print ("\nERRO - Impossível carregar o grafo para o ego: "+str(ego_id)+"  --  "+str(graphs_dir)+str(ego_id)+".edge_list\n")
							print e
			

						_m_file = calc.calcular(m_file)
						modularity_data[ego_id] = m_file
						if _m_file is not None:
							modularity.append(_m_file['media'])
	
							print (str(graph_type)+" - Rede: "+str(net)+" - Threshold: "+str(threshold)+" - Modularidade para o ego "+str(i)+" ("+str(file)+"): %5.3f" % (_m_file['media']))
							print("######################################################################")	
					M = calc.calcular_full(modularity)
	
					if M is not None:
						overview = {'threshold': threshold, 'modularity':M,'modularity_data':modularity_data}
						print("\n######################################################################\n")	
						print ("Rede: %s   ---   Threshold: %s   ---   Modularity: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (net,threshold,M['media'],M['variancia'],M['desvio_padrao']))
						print("\n######################################################################\n")	

					if overview is not None:
						with open(str(output_dir)+str(threshold)+".json", 'a+') as f:
							f.write(json.dumps(overview)+"\n")		

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
	print"																											"
	print" Script para cálculo da Modularidade 															"
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
	print
	op = int(raw_input("Escolha uma opção acima: "))
	
	if not op in range(1,11): 
	
		print("Opção inválida! Saindo...")
		sys.exit()
######################################################################
	net = "n"+str(op)	
######################################################################
	print "################################################################################"
	print"																											"
	print" Escolha o algoritmo usado na detecção das comunidades							"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print"  3 - GN"		
	print"  4 - COPRA - Partition"
	print"  5 - INFOMAP - Partition"		
	print"  6 - INFOMAP - Partition - Without Weight"	
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"
	elif op2 == 3:
		alg = "gn"
	elif op2 == 4:
		alg = "copra_partition"
	elif op2 == 5:
		alg = "infomap"
	elif op2 == 6:
		alg = "infomap_without_weight"		
	else:
		print("Opção inválida! Saindo...")
		sys.exit()		
######################################################################
	
	metric = 'modularity'

######################################################################		
######################################################################
	graph_type = "graphs_with_ego"
	dataset_dir1 = "/home/amaury/communities_hashmap/"+str(graph_type)+"/"+str(alg)+"/full/"	############### Arquivo contendo arquivos contendo as comunidades
	
	if not os.path.isdir(dataset_dir1):
		print("Diretório das comunidades não encontrado: "+str(dataset_dir1))
	else:
		output_dir1 = str(output)+str(metric)+"/"+str(graph_type)+"/"+str(alg)+"/full/"+str(net)+"/"
		if not os.path.exists(output_dir1):
			os.makedirs(output_dir1)

		print ("\nCalcular modularidade... /home/amaury/communities_hashmap/"+str(graph_type)+"/"+str(alg)+"/full/")	
		net_structure(dataset_dir1,output_dir1,graph_type,metric,net,alg)														# Inicia os cálculos...

######################################################################		
######################################################################

	graph_type = "graphs_without_ego"
	dataset_dir3 = "/home/amaury/communities_hashmap/"+str(graph_type)+"/"+str(alg)+"/full/"	############### Arquivo contendo arquivos contendo as comunidades
	
	if not os.path.isdir(dataset_dir3):
		print("Diretório das comunidades não encontrado: "+str(dataset_dir3))
	else:
		output_dir3 = str(output)+str(metric)+"/"+str(graph_type)+"/"+str(alg)+"/full/"+str(net)+"/"
		if not os.path.exists(output_dir3):
			os.makedirs(output_dir3)
		print ("\nCalcular modularidade... /home/amaury/communities_hashmap/"+str(graph_type)+"/"+str(alg)+"/full/")
		net_structure(dataset_dir3,output_dir3,graph_type,metric,net,alg)													# Inicia os cálculos...

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

output = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"
			 

#Executa o método main
if __name__ == "__main__": main()