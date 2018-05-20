	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, math
import numpy as np
from math import*
import calc
import graphics

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1
##			- Pega os top-k de cada interação e analisa se eles ocorrem nas outras camadas. Apresentar antes da parte de comunidades...
##			- Verificar se os alters que mais sofrem interações do egos por uma camada aparecem como alters em outras camadas.
##
##       - Objetivo: mostrar que alters mais retwitados e que mais sofrem likes não são amigos do ego em vários casos.
##					Isso mostra que o Twitter deveria sugerir fortemente ao ego que ele siga os alters com quem ele interage,
##					pois do contrário ele pode estar perdendo tweets que esses alters criam. No caso de retweet essa implicação é ainda mais grave,
##					pois restringe a cascata de propagação dos tweets daquele alter na rede como um todo.
##					Se o ego não recebe um tweet de um usuário que ele tem alta probabilidade de retuitar,
##					ele não propaga esse tweet para os usuários que o seguem, aftetando a cascata de informações a partir do alter-autor.
##
##
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dirs(x):
	if not os.path.exists(x):
		os.makedirs(x)

######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(output_dir_json,dataset_json,name):
	with open(output_dir_json+name+".json","w") as f:
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
# Recupera o conjunto de alters a partir do grafo
#
###############################################################
def get_top_k(ego,file):
	alters_set = set()

	ranking = []
	with open(file, 'r') as f:
		for line in f:			
			a = line.split(' ')
			if long(a[0])==long(ego):
				alters_set.add(long(a[1]))										# Pega só o primeiro campo - nó1
				if len(a) > 2:
					tuple=(long(a[1]),float(a[2]))							# Armazena o peso do relacionamento entre o alter e o ego para formar um ranking depois.
					ranking.append(tuple)
			elif long(a[1])==long(ego):
				alters_set.add(long(a[0]))										# Pega só o segundo campo - nó 2
				if len(a) > 2:
					tuple=(long(a[0]),float(a[2]))							# Armazena o peso do relacionamento entre o alter e o ego para formar um ranking depois.
					ranking.append(tuple)
								
	ranking = sorted(ranking, key=lambda x: (x[1], -x[0]), reverse=True)	#Ordena uma tupla decrescente (id,weight)). Em caso de empate ordena crecente pelo id os empatados

	top_k = []
	i=0						
	for i in range(10):		#10 é o tamanho do ranking (top-k)		# Cria um sub-ranking com apenas os top-k elementos com os quais o ego mais interagiu nessa camada.
		i+1
		try:
			top_k.append(ranking[i][0])
		except Exception as e:													# Ranking menor que o top-k
			pass
	
	return alters_set,top_k														# Só retorna a lista de alters, sem considerar o ego, embora o ego apareça nas listas em que ele está inscrito.


######################################################################################################################################################################
#
# Calcula Rank_based Overlap - Extended entre os rankings de pares de layers  
#
######################################################################################################################################################################
def jaccard_modified(ranking1,ranking2):
	ranking1 = set(ranking1)
	ranking2 = set(ranking2)
	intersection = len(ranking1.intersection(ranking2))	
	result = intersection/float(len(ranking2))				#Tamanho da interseção dos rankings sobre o tamanho d segundo ranking
	return result															#... verifica qual o percentual dos top_k da segunda camada está na primeira
																				
######################################################################################################################################################################
#
# Prepara o cálculo da co-ocorrência entre os pares de layers - Extended entre os rankings de pares de layers  
#
######################################################################################################################################################################
def calc_co_occurrence(top_k):
	pairs = {}			

	for k,v in top_k.iteritems():
		ranking1 = []
		for item in v:
			ranking1.append(item)					# Colocando ranking em lista para a camada 1 - Apenas o ID do vertice

		for j, x in top_k.iteritems():
#			if j >= k and j != k:					# Considera todos os pares, inclusive duas camadas iguais.
			ranking2 = []
			for item in x:
				ranking2.append(item)				# Colocando ranking em lista para a camada 2 - Apenas o ID do vertice
				
			name = str(k)+str(j)
			pairs[name] = jaccard_modified(ranking1,ranking2)	# Comparando os rankings com jaccard_modified (tamanho da interseção sobre o tamanho do segundo conjunto (ranking2)				 	
	
	return pairs
								
######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(type_graphs,singletons):
	output_dir = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs)+"_"+str(singletons)+"/"
	create_dirs(output_dir)																				# Cria diretótio para salvar arquivos.
	
	if os.path.exists(output_dir+"top_k_co_occurrence.json"):
		print ("Arquivo de destino já existe!"+str(output_dir+"top_k_co_occurrence.json"))
	else:
		i=0
		top_k_dataset = {}																											# Armazenar os tpo-k de todas as camadas.
		with open(output_dir+"top_k_co_occurrence.txt",'w') as out_file:
			for ego,v in dictionary.iteritems():
				i+=1
				top_k = {}																													# armazena os top-k das camadas do ego em corrente
				nets = ["n1","n2","n3","n4","n9"] #[amigos,seguidores,retweets,likes,menções]							# Camadas de interações no Twitter					
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
				
					graphs_dir = "/home/amaury/graphs/"+str(net)+"/"+str(type_graphs)+"/"
					if not os.path.exists(graphs_dir):
						print ("Impossível encontrar arquivos com o grafo: "+str(graphs_dir))
					else:
						top_k[layer] = get_top_k(ego,graphs_dir+str(ego)+".edge_list")												# Recupera os alters da camada n para ego_id

				pairs = calc_co_occurrence(top_k) 
				save_file(ego,pairs,out_file)																						# Salvar arquivo texto			
				top_k_dataset[ego] = pairs
					
				print ("Ego: "+str(i)+" - Top-K Pairs: "+str(top_k_dataset[ego]))
				print
			
		name = "top_k_co_occurrence.json"
		save_json(output_dir,top_k_dataset,name)
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "\n#######################################################################\n"	
	type_graphs1 = "graphs_with_ego"
	type_graphs2 = "graphs_without_ego"
	singletons1 = "full"
	singletons2 = "without_singletons"
#######################################################################
	
	instructions(type_graphs1,singletons1)
#	instructions(type_graphs1,singletons2)
#	instructions(type_graphs2,singletons1)
#	instructions(type_graphs2,singletons2)	
	
#######################################################################
	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

data_dir = "/home/amaury/graphs/n1/graphs_with_ego/"												# Pegar a lista com os ids dos egos	
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