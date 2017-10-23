# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
# Script auxiliar para cálculos matemáticos que deve estar no mesmo diretório deste aqui.
import calc
import plot_modularity
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
def net_structure(dataset_dir,output_dir,graph_type,metric):
	os.system('clear')	
	if os.path.isfile(str(output_dir)+"overview.json"):
		os.remove(str(output_dir)+"overview.json")	
		
	print("\n######################################################################\n")
	print("\nScript para cálculo da modularidade das comunidades detectadas\n")
		
	modularity_plot = {}																	# Armazenar o nome da rede e o maior valor do da modularidade - Formato {{'N1':0.012},...}
	for network in range(10):
		_net = network+1
		net = "n"+str(_net)
		
		modularity_plot[net] = {'threshold':' ',metric:float(0)}
		graphs_dir = "/home/amaury/graphs/"+str(net)+"/"+str(graph_type)+"/"
		
		if not os.path.exists(graphs_dir):
			print ("Diretório não encontrado: "+str(graphs_dir))
		
		else:
			print("\n######################################################################\n")
			print("\nScript para cálculo da modularidade das comunidades detectadas - Rede "+str(net)+"\n")	

			if not os.path.isdir(dataset_dir+str(net)+"/"):
				print ("Diretório com avaliações da rede "+str(net)+" não encontrado: "+str(dataset_dir+str(net)+"/"))
			else:	
				for threshold in os.listdir(dataset_dir+str(net)+"/"):
					modularity = []																										# Vetor com a Média das modularidades de cada grafo	
					i = 0
			
					for file in os.listdir(dataset_dir+str(net)+"/"+str(threshold)+"/"):
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
				
						m_file = []																					# vetor de modularidade das comunidades do ego i
						for comm in communities:
							if comm is not None:
								Nodes = snap.TIntV()
								for nodeId in comm:
									if nodeId is not None:						
										Nodes.Add(long(nodeId))			
								m_file.append(snap.GetModularity(G, Nodes, n_edges))						#Passar o número de arestas do grafo como parâmetro para agilizar o processo


						_m_file = calc.calcular(m_file)
						modularity.append(_m_file['media'])
	
						print (str(graph_type)+" - Rede "+str(net)+" - Modularidade para o ego %d: %5.3f" % (i,_m_file['media']))
						print("######################################################################")	
		
					M = calc.calcular_full(modularity)
					overview = {'threshold': threshold, 'modularity':M}
					if M is not None:						
						if	float(M['media']) > modularity_plot[net][metric]:
							modularity_plot[net] = {'threshold': threshold, metric:float(M['media'])}
					with open(str(output_dir)+str(net)+"_overview.json", 'a+') as f:
						f.write(json.dumps(overview)+"\n")		
			
				print("\n######################################################################\n")	
				print ("Rede: %s   ---   Threshold: %s   ---   Modularity: Média: %5.3f -- Var:%5.3f -- Des. Padrão: %5.3f"% (net,threshold,M['media'],M['variancia'],M['desvio_padrao']))
				print("\n######################################################################\n")


	return modularity_plot
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
	
	metric = 'modularity'
	data1 = {}
	data2 = {}
	data3 = {}
	data4 = {}
######################################################################		
######################################################################
	graph_type = "graphs_with_ego"
	dataset_dir1 = "/home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/full/"	############### Arquivo contendo arquivos contendo as comunidades
	
	if not os.path.isdir(dataset_dir1):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir1))
	else:
		output_dir1 = "/home/amaury/Dropbox/modularity/"+str(graph_type)+"/"+str(alg)+"/full/"
		if not os.path.exists(output_dir1):
			os.makedirs(output_dir1)

		print ("\nCalcular modularidade... /home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/full/")
		data1 = net_structure(dataset_dir1,output_dir1,graph_type,metric)														# Inicia os cálculos...
		plot_modularity.plot_single(output_dir1,data1,metric,alg,title=str(graph_type)+" - Communities with singletons")				
######################################################################				
######################################################################
	graph_type = "graphs_with_ego"	
	dataset_dir2 = "/home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/without_singletons/"	############### Arquivo contendo arquivos contendo as comunidades
	
	if not os.path.isdir(dataset_dir2):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir2))
	else:
		output_dir2 = "/home/amaury/Dropbox/modularity/"+str(graph_type)+"/"+str(alg)+"/without_singletons/"
		if not os.path.exists(output_dir2):
			os.makedirs(output_dir2)
		print ("\nCalcular modularidade... /home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/without_singletons/")
		data2 = net_structure(dataset_dir2,output_dir2,graph_type,metric)														# Inicia os cálculos...
		plot_modularity.plot_single(output_dir2,data2,metric,alg,title=str(graph_type)+" - Communities without singletons")			


######################################################################
######################################################################
	graph_type = "graphs_without_ego"
	dataset_dir3 = "/home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/full/"	############### Arquivo contendo arquivos contendo as comunidades
	
	if not os.path.isdir(dataset_dir3):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir3))
	else:
		output_dir3 = "/home/amaury/Dropbox/modularity/"+str(graph_type)+"/"+str(alg)+"/full/"
		if not os.path.exists(output_dir3):
			os.makedirs(output_dir3)
		print ("\nCalcular modularidade... /home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/full/")
		data3 = net_structure(dataset_dir3,output_dir3,graph_type,metric)													# Inicia os cálculos...
		plot_modularity.plot_single(output_dir3,data3,metric,alg,title=str(graph_type)+" - Communities with singletons")	
######################################################################		
######################################################################
	graph_type = "graphs_without_ego"
	dataset_dir4 = "/home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/without_singletons/"	############### Arquivo contendo arquivos contendo as comunidades

	if not os.path.isdir(dataset_dir4):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir4))
	else:
		output_dir4 = "/home/amaury/Dropbox/modularity/"+str(graph_type)+"/"+str(alg)+"/without_singletons/"
		if not os.path.exists(output_dir4):
			os.makedirs(output_dir4)
		print ("\nCalcular modularidade... /home/amaury/communities/"+str(graph_type)+"/"+str(alg)+"/without_singletons/")
		data4 = net_structure(dataset_dir4,output_dir4,graph_type,metric)													# Inicia os cálculos...
		plot_modularity.plot_single(output_dir4,data4,metric,alg,title=str(graph_type)+" - Communities without singletons")		
######################################################################
######################################################################		
	if data1 is not None and data2 is not None and data3 is not None and data4 is not None:
		output = "/home/amaury/Dropbox/modularity/"+str(alg)+"/"
		plot_modularity.plot_full(output,data1,data2,data3,data4,metric,alg)		
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