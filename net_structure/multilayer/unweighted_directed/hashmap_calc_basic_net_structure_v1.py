# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
#Calculadora copiada da net...
import calc						


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular o métricas básicas como numero de vértices, arestas, densidade, etc. e armazenar em um arquivo texto.
##								- Considerar apenas redes-ego com a presença do ego.
##								- Calcula-se as métricas a partir da lista de arestas...
## 
##	INPUT: Redes-ego
##
## Output: arquivo texto. Formato:
##
##ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dirs(x,y):
	if not os.path.exists(x):
		os.makedirs(x)
	if not os.path.exists(y):
		os.makedirs(y)		

######################################################################################################################################################################
#
# Cálculo do JACCARD entre os dois conjuntos de arestas
#
######################################################################################################################################################################
def calc_metric(G,metric):
	IsDir = True														# Todas as redes são direcionadas
	n_nodes = G.GetNodes()
	n_edges = G.GetEdges()

	if metric == "nodes":
		result = n_nodes

	elif metric == "edges":
		result = n_edges

	elif metric == "size":
		result = n_nodes+n_edges

	elif metric == "avg_degree":
		result = float(2*n_edges)/float(n_nodes)

	elif metric == "diameter":
		result = snap.GetBfsFullDiam(G, 100, IsDir)
		
	elif metric == "density":
		result = float(n_edges)/(float(n_nodes)*(float(n_nodes-1)))

	elif metric == "closeness_centr":
		Normalized = True
		cc = []
		for NI in G.Nodes():
			cc.append(snap.GetClosenessCentr(G, NI.GetId(), Normalized, IsDir)) #get a closeness centrality
		
		_cc = calc.calcular(cc)
		result = _cc['media']	

	elif metric == "betweenness_centr_nodes":
		bc_n = []		
		if n_edges == 0 or n_nodes < 3:
			bc_n.append(int(0))
		else:
			Nodes = snap.TIntFltH()
			Edges = snap.TIntPrFltH()
			snap.GetBetweennessCentr(G, Nodes, Edges, 1.0, IsDir)								#Betweenness centrality Nodes
			if IsDir is True:
				max_betweenneess = (n_nodes-1)*(n_nodes-2)
			else:
				max_betweenneess = ((n_nodes-1)*(n_nodes-2))/2
			for node in Nodes:
				bc_n_normalized = float(Nodes[node]) / float(max_betweenneess)
				bc_n.append(bc_n_normalized)
		_bc_n = calc.calcular(bc_n)			
		result = _bc_n['media']

	elif metric == "betweenness_centr_edges":
		bc_e = []
		if n_edges == 0 or n_nodes < 3:
			bc_e.append(int(0))
		else:
			Nodes = snap.TIntFltH()
			Edges = snap.TIntPrFltH()
			snap.GetBetweennessCentr(G, Nodes, Edges, 1.0, IsDir)								#Betweenness centrality Edges
			if IsDir is True:
				max_betweenneess = (n_nodes-1)*(n_nodes-2)
			else:
				max_betweenneess = ((n_nodes-1)*(n_nodes-2))/2
			for edge in Edges:
				bc_e_normalized = float(Edges[edge]) / float(max_betweenneess)
				bc_e.append(bc_e_normalized)
		_bc_e = calc.calcular(bc_e)
		result = _bc_e['media']

	elif metric == "clust_coef":
		result = snap.GetClustCf(G, -1)

	else:
		result = None
		print ("\nImpossível calcular "+str(metric))
		print ("\n")
		sys.exit()

	return result
######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(dataset_json,metric):
	with open(str(output_dir_json)+str(metric)+".json","w") as f:
		f.write(json.dumps(dataset_json))
######################################################################################################################################################################
#
# Salvar arquivo texto com padrão:  ego_id as:data ar:data al:data am:data ... rm:data  
#
######################################################################################################################################################################
def save_file(ego,dataset,f):
	f.write(str(ego))
	for k,v in dataset.iteritems():
		f.write(" "+str(k)+":"+str(v))
	f.write("\n")
					
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
	print" Cálculo da Basic Net Structure																	"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - Nodes"
	print"  2 - Edges"
	print"  3 - Size"
	print"  4 - Average Degree"
	print"  5 - Diameter"
	print"  6 - Density"
	print"  7 - Closeness Centrality"				
	print"  8 - Betweenness Centrality Nodes"
	print"  9 - Betweenness Centrality Edges"
	print"  10 - Clustering Coefficient"
			
	print("\n")
	op = int(raw_input("Escolha uma opção acima: "))

	if op == 1:
		metric = "nodes"
	elif op == 2:
		metric = "edges"
	elif op == 3:
		metric = "size"
	elif op == 4:
		metric = "avg_degree"
	elif op == 5:
		metric = "diameter"
	elif op == 6:
		metric = "density"
	elif op == 7:
		metric = "closeness_centr"
	elif op == 8:
		metric = "betweenness_centr_nodes"
	elif op == 9:
		metric = "betweenness_centr_edges"
	elif op == 10:
		metric = "clust_coef"
	else:
		metric = 0
		print("Opção inválida! Saindo...")
		sys.exit()													

	if os.path.exists(str(output_dir_json)+str(metric)+".json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json)+str(metric)+".json")
	else:	
		create_dirs(output_dir_txt,output_dir_json)																				# Cria diretótio para salvar arquivos.
		dataset_json = {}																													# Salvar Arquivos no Formato Json
		i=0																																	# Contador do ego
		with open(str(output_dir_txt)+str(metric)+".txt",'w') as out_file:
			for ego,v in dictionary.iteritems():
				i+=1
				nets = ["n1","n2","n3","n4","n9"] #[amigos,seguidores,retweets,likes,menções]							# Camadas de interações no Twitter
				dataset = {}
				for net in nets:
					if net == "n1":
						layer = "a"
					elif net == "n9":
						layer = "s"
					elif net == "n2":
						layer = "r"
					elif net == "n3":
						layer = "l"
					elif net == "n4":
						layer = "m"
					else:
						print ("Rede inválida")
						sys.exit()

					edge_list1 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_with_ego/"							# Diretório da camada i

					if not os.path.isdir(edge_list1):																				# Verifica se diretório existe	
						print ("Impossível localizar diretório com lista de arestas: "+str(edge_list1))

					else:
						source = str(edge_list1)+str(ego)+".edge_list"
						G = snap.LoadEdgeList(snap.PNGraph, source, 0, 1)					   								# Carrega o grafo da camada i - Direcionado e Não Ponderado
						result = calc_metric(G,metric)																				# Calcula Métrica
						dataset[layer] = result
							
				dataset_json[ego] = dataset
				print i, metric, dataset_json[ego]
				save_file(ego,dataset,out_file)																						# Salvar arquivo texto
				print
		save_json(dataset_json,metric)																								# Salvar arquivo no formato JSON
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

data_dir = "/home/amaury/graphs_hashmap/n1/graphs_with_ego/"												# Pegar a lista com os ids dos egos
output_dir_txt = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/txt/basics/"	# Pegar a lista com os ids dos egos
output_dir_json = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/basics/"	# Pegar a lista com os ids dos egos


dictionary = {}				#################################################### Tabela {chave:valor} para armazenar lista de egos
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print("######################################################################")
print ("Criando tabela hash...")
n = 0	#Conta quantos arquivos existem no diretório
for file in os.listdir(data_dir):
	user_id = file.split(".edge_list")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	n+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
if n <> 500:
	print ("Diretório não contém lista com todos os egos...")
	sys.exit()
else:

	#Executa o método main
	if __name__ == "__main__": main()