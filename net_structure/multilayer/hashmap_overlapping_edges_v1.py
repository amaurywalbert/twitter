# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import networkx as nx

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular a interseção entre os conjuntos de arestas das redes-ego, par-a-par e armazenar em um arquivo texto.
##								- Quero descobrir se há porcentagem de sobreamento entre as redes... quantas arestas em comum, sobrepostas. 
##								- Para os conjuntos x e y, calcula-se a interseção dos conjuntos x e y sobre o tamanho do conjunto x. Faz-se o processo para todo par de conjuntos (layers)
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
# Cálculo da Interseção entre os dois conjuntos de arestas
#
######################################################################################################################################################################
def overlapping_pairs(x,y):

	intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
	return intersection_cardinality/float(len(x))

######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(dataset_json):
	with open(output_dir_json+"overlapping_edges.json","w") as f:
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
	print" Cálculo da Interseção (Overlapping) para a par entre os arestas das camadas		"
	print"																											"
	print"#################################################################################"
	print
	i=0
	if os.path.exists(output_dir_json+"overlapping_edges.json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json+"overlapping_edges.json"))
	else:
		create_dirs(output_dir_txt,output_dir_json)																				# Cria diretótio para salvar arquivos.

		dataset_json = {}																													# Salvar Arquivos no Formato Json

		with open(output_dir_txt+"overlapping_edges.txt",'w') as out_file:
			
			for ego,v in dictionary.iteritems():
				i+=1
				nets = ["n1","n2","n3","n4","n9"] #[amigos,seguidores,retweets,likes,menções]							# Camadas de interações no Twitter
				dataset = {}
				for net1 in nets:
					if net1 == "n1":
						layer1 = "a"
					elif net1 == "n9":
						layer1 = "s"
					elif net1 == "n2":
						layer1 = "r"
					elif net1 == "n3":
						layer1 = "l"
					elif net1 == "n4":
						layer1 = "m"
					else:
						print ("Rede 1 inválida")
						sys.exit()

					edge_list1 = "/home/amaury/graphs_hashmap/"+str(net1)+"/graphs_with_ego/"							# Diretório da camada i

					if not os.path.isdir(edge_list1):																				# Verifica se diretório existe	
						print ("Impossível localizar diretório com lista de arestas: "+str(edge_list1))

					else:

						source = str(edge_list1)+str(ego)+".edge_list"
						G1 = nx.read_weighted_edgelist(source,create_using=nx.DiGraph())								# Carrega o grafo da camada i
						edges1 = set(G1.edges)
						G1.clear()
						for net2 in nets:																								# Busca pelo arquivo do mesmo ego nas outras camadas (redes) j
							if net2 == "n1":
								layer2 = "a"
							elif net2 == "n9":
								layer2 = "s"
							elif net2 == "n2":
								layer2 = "r"
							elif net2 == "n3":
								layer2 = "l"
							elif net2 == "n4":
								layer2 = "m"
							else:
								print ("Rede 2 inválida")
								sys.exit()	
														
							dest = "/home/amaury/graphs_hashmap/"+str(net2)+"/graphs_with_ego/"+str(ego)+".edge_list"	# Diretório do arquivo na camada j							
							if not os.path.isfile(dest):																	# Testa se arquivo do mesmo ego existe na camada j	
								print ("Impossível localizar arquivo no destino: "+str(dest))
							else:
								G2 = nx.read_weighted_edgelist(dest,create_using=nx.DiGraph())					# Carrega o grafo da camada j
								edges2 = set(G2.edges)																		
								G2.clear()
								result = overlapping_pairs(edges1,edges2)													# Calcula a sobreposição dos dois grafos
								pair=str(layer1)+str(layer2)
								dataset[pair] = result
				dataset_json[ego] = dataset
				print dataset_json[ego]
				save_file(ego,dataset,out_file)																					# Salvar arquivo texto
				
				print
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
output_dir_txt = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/txt/"	
output_dir_json = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/json/"	


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