# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import rbo, rbo_calc
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
from math import*
import pandas as pd
import pandas_datareader
from pandas_datareader import data, wb
from pandas import Series, DataFrame
pd.__version__  


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular a sobreposição de Rankings usando Rank-Biased Overlap - Extended, para o ranking de closeness centrality.
##								- Considerar apenas redes-ego com a presença do ego.
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
# Cálculo Correlação de Ranking
#
######################################################################################################################################################################
def get_close_centr_rank(G):
	result = None        #REMOVER
	IsDir = True														# Todas as redes são direcionadas
	Normalized = True
	inlinkNumb = []
	cc = []
	for NI in G.Nodes():
		cc = snap.GetClosenessCentr(G, NI.GetId(), Normalized, IsDir) #get a closeness centrality
		node = NI.GetId()
		_tuple = (node,cc)
		inlinkNumb.append(_tuple)

	close_centr_rank = sorted(inlinkNumb, key=lambda x: (x[1], -x[0]), reverse=True) 		#Ordena uma tupla decrescente (id,close_centr)). Em caso de empate ordena crecente pelo id os empatados
	
	return close_centr_rank						#Retorna o id do vertice e o grau de entrada- inclusive se o grau for 0								

######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(dataset_json):
	with open(output_dir_json+metric+".json","w") as f:
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
#
# Calcula Rank_based Overlap - Extended entre os rankings de pares de layers  
#
######################################################################################################################################################################
def calc_rbo_extended(dataset):
	pairs = {}
	p = 0.98											#parametro do RBO_extend - alterar para profundidade do ranking
														# com p = 0.98 - top 50k com peso de +/- 86% na avaliação do overlap entre os rankings			

	for k,v in dataset.iteritems():
		ranking1 = []
		for item in v:
			ranking1.append(item[0])				# Colocando ranking em lista para a camada 1 - Apenas o ID do vertice

		for j, x in dataset.iteritems():
			if j >= k and j != k:
				ranking2 = []
				for item in x:
					ranking2.append(item[0])		# Colocando ranking em lista para a camada 2 - Apenas o ID do vertice
				
				name = str(k)+str(j)
				pairs[name] = rbo_calc.calc_rbo(ranking1,ranking2,p)		# Comparando os rankings com RBO_CALC.py				 	
	
	return pairs
						
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
	print" Cálculo da sobreposição de ranks entre Layers - Closeness Centrality				"
	print"																											"
	print"#################################################################################"
	print

	i=0
	if os.path.exists(output_dir_json+metric+".json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json+metric+".json"))
	else:
		create_dirs(output_dir_txt,output_dir_json)																				# Cria diretótio para salvar arquivos.
		dataset_json = {}																													# Salvar Arquivos no Formato Json
		with open(output_dir_txt+metric+".txt",'w') as out_file:
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

					edge_list = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_with_ego/"							# Diretório da camada i

					if not os.path.isdir(edge_list):																				# Verifica se diretório existe	
						print ("Impossível localizar diretório com lista de arestas: "+str(edge_list))
					else:
						source = str(edge_list)+str(ego)+".edge_list"
						G = snap.LoadEdgeList(snap.PNGraph, source, 0, 1)					   							# Carrega o grafo da camada i - Direcionado e Não Ponderado
						close_centr_rank = get_close_centr_rank(G)																	# Retorna o ranking  - por enquanto desordenado - da camada x
						dataset[layer] = close_centr_rank
				

				pairs = calc_rbo_extended(dataset) 


				dataset_json[ego] = pairs
				print i, dataset_json[ego]
				save_file(ego,pairs,out_file)																						# Salvar arquivo texto
				print
						
		save_json(dataset_json)																										# Salvar arquivo no formato JSON
		
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

data_dir = "/home/amaury/graphs_hashmap/n1/graphs_with_ego/"												# Pegar a lista com os ids dos egos
output_dir_txt = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/txt/"	# 
output_dir_json = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/"	# 

metric = "rbo_extended_closeness_centrality"

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