# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import networkx as nx
from scipy.stats.stats import pearsonr    


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular a reciprocidade (correlação entre in-degree e out-degree) e armazenar o resultado num arquivo texto.
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
# Cálculo da Reciprocidade entre In-Degree e Out-Degree - correlação entre Matrizes de Adjacencia p(X,Y)= p(Aij,Aji)
#
######################################################################################################################################################################
def reciprocity(G):
	result = None        #REMOVER
	in_degree = {}
	out_degree = {}
	v_in_d = []
	v_out_d = []
	
	InDegV = snap.TIntPrV()
	snap.GetNodeInDegV(G,InDegV)					#Retorna o id do vertice e o grau de entrada- inclusive se o grau for 0 
	for item in InDegV:
		node = item.GetVal1()
		degree = item.GetVal2()
		in_degree[node] = degree
	
	OutDegV = snap.TIntPrV()
	snap.GetNodeOutDegV(G, OutDegV)
	for item in OutDegV:
		node = item.GetVal1()
		degree = item.GetVal2()
		out_degree[node] = degree

	for k,v in in_degree.iteritems():
		if k in out_degree:
			v_in_d.append(v)
			v_out_d.append(out_degree[k])
	result = pearsonr(v_in_d,v_out_d)				#Retorna uma tupla (coef,p-value)
	return result[0]									 	#Retorna apenas o coef									

######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(dataset_json):
	with open(output_dir_json+"reciprocity.json","w") as f:
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
	print" Cálculo da Reciprocidade em cada Layer			"
	print"																											"
	print"#################################################################################"
	print
	i=0
	if os.path.exists(output_dir_json+"reciprocity.json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json+"reciprocity.json"))
	else:
		create_dirs(output_dir_txt,output_dir_json)																				# Cria diretótio para salvar arquivos.
		dataset_json = {}																													# Salvar Arquivos no Formato Json
		with open(output_dir_txt+"reciprocity.txt",'w') as out_file:
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
						result = reciprocity(G)																						# Calcula a Reciprocidade em cada layer
						dataset[layer] = result
						
				dataset_json[ego] = dataset
				print i, dataset_json[ego]
				save_file(ego,dataset,out_file)																					# Salvar arquivo texto
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
output_dir_txt = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/txt/"	# Pegar a lista com os ids dos egos
output_dir_json = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/json/"	# Pegar a lista com os ids dos egos


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