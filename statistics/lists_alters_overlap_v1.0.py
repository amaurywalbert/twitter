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
##			- Estudar a relação entre os alters de um ego e os componentes das listas em que o ego está envolvido (ajuda a justificar a coleta baseada em lista):
##					interseção entre os alters e os usuários das listas
##					(pode juntar todos os usuários das listas em um único conjunto e podemos calcular o overlap em relação às listas e em relação aos alters).
##
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
# Recupera cada lista e compara com o conjunto de alters
#
###############################################################
def get_lists_set(file):
	with open(file, 'r') as f:
		lists_set = set()											#Usado na versão 0 - armazena todos os elementos da lista (membros e incritos)
		for line in f:
			a = line.split(' ')
			for item in a:
				if item != "\n":
					lists_set.add(long(item))
		return lists_set
		
######################################################################################################################################################################
#
# Recupera o conjunto de alters a partir do grafo
#
###############################################################
def get_alters_set(ego_id,file):
	alters_set = set()
	alters_set_full = set()

	ranking = []
	with open(file, 'r') as f:
		for line in f:			
			a = line.split(' ')

			alters_set_full.add(long(a[0]))									#Pega só o primeiro campo - nó1
			alters_set_full.add(long(a[1]))									#Pega só o segundo campo - nó 2
			
			if len(a) > 2:
				if long(a[0])==long(ego_id):
					alters_set.add(long(a[0]))										# Pega só o primeiro campo - nó1
					tuple=(a[1],a[2])													# Armazena o peso do relacionamento entre o alter e o ego para formar um ranking depois.
					ranking.append(tuple)
				elif long(a[1])==long(ego_id):
					alters_set.add(long(a[1]))										# Pega só o segundo campo - nó 2
					tuple=(a[0],a[2])													# Armazena o peso do relacionamento entre o alter e o ego para formar um ranking depois.
					ranking.append(tuple)
			else:																			# Rede sem peso
				weight = 1
				if long(a[0])==long(ego_id):
					alters_set.add(long(a[0]))										# Pega só o primeiro campo - nó1
					tuple=(a[1],weight)												# Armazena o peso do relacionamento entre o alter e o ego para formar um ranking depois.
					ranking.append(tuple)
				elif long(a[1])==long(ego_id):
					alters_set.add(long(a[1]))										# Pega só o segundo campo - nó 2
					tuple=(a[0],weight)												# Armazena o peso do relacionamento entre o alter e o ego para formar um ranking depois.
					ranking.append(tuple)				
				
	ranking = sorted(ranking, key=lambda x: (x[1], -x[0]), reverse=True) 		#Ordena uma tupla decrescente (id,weight)). Em caso de empate ordena crecente pelo id os empatados
	
	top_k = []
	i=0						
	for i in range(10):															# Cria um sub-ranking com apenas os top-k elementos com os quais o ego mais interagiu nessa camada.
		i+1
		try:
			top_k.append(ranking[i])
		except Exception as e:
			print e
	
	print ranking	
	print top_k
			
	print len(alters_set),len(alters_set_full)
	return alters_set
			
################################################################################################
# Função para calcular o a sobreposição e o csj entre dois conjuntos de dados
################################################################################################         
def calc_overlap(lists_set,alters_set):
	
	def calc_jaccard(lists_set,alters_set):
		intersection = len(lists_set.intersection(alters_set))
		union = len(lists_set.union(alters_set))	
		jaccard = intersection/float(union)									#Jaccard Tradicional
		return jaccard
	
	def calc_overlap_lists(lists_set,alters_set):
		intersection = len(lists_set.intersection(alters_set))	
		overlap_lists = intersection/float(len(lists_set))				#Tamanho da interseção dos conjuntos sobre o tamanho do conjunto das listas... 
		return overlap_lists														#... verifica se os membros das Listas estão no conjunto de alters.
																						# Qual a porcentagem de elementos das listas com que o ego interage?
	def calc_overlap_alters(lists_set,alters_set):
		intersection = len(lists_set.intersection(alters_set))	
		overlap_alters = intersection/float(len(alters_set))			#Tamanho da interseção dos conjuntos sobre o tamanho do conjunto de alters... verifica se os alters estão nas listas.
		return overlap_alters													#... verifica se os alters estão nas listas
																						# Qual a porcentagem dos alters aparecem nas listas?		
	jaccard = calc_jaccard(lists_set,alters_set)
	overlap_lists = calc_overlap_lists(lists_set,alters_set)
	overlap_alters = calc_overlap_alters(lists_set,alters_set)

	return jaccard,overlap_lists,overlap_alters
 
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
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(type_graphs,singletons):	
	ground_truth_dir = "/home/amaury/dataset/ground_truth/lists_users_TXT/"+str(singletons)+"/"
	output_dir_json = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs)+"_"+str(singletons)+"/json/"
	output_dir_txt = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs)+"_"+str(singletons)+"/txt/"	

	create_dirs(output_dir_txt,output_dir_json)																				# Cria diretótio para salvar arquivos.
	
	if os.path.exists(output_dir_json+"jaccard.json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json+"jaccard.json"))
	else:
		if not os.path.exists(ground_truth_dir):
			print ("\nImpossível encontrar diretório com ground-truth communities: "+str(ground_truth_dir))
		else:

			dataset_json_jaccard = {}																													# Salvar Arquivos no Formato Json
			dataset_json_overlap_lists = {}
			dataset_json_overlap_alters = {}
			
			with open(output_dir_txt+"jaccard.txt",'w') as out_file_jaccard:
				with open(output_dir_txt+"overlap_lists.txt",'w') as out_file_overlap_lists:
					with open(output_dir_txt+"overlap_alters.txt",'w') as out_file_overlap_alters:
						i=0
						for ground_truth_file in os.listdir(ground_truth_dir):			
							lists_set = get_lists_set(ground_truth_dir+ground_truth_file)														# Recupera o conjunto de elementos das listas do ego.
							ego_id = ground_truth_file.split(".txt")
							ego_id = long(ego_id[0])
							i+=1
							nets = ["n1","n2","n3","n4","n9"] #[amigos,seguidores,retweets,likes,menções]							# Camadas de interações no Twitter
							dataset_jaccard = {}
							dataset_overlap_lists = {}
							dataset_overlap_alters = {}
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
								if not os.path.isfile(graphs_dir+str(ego_id)+".edge_list"):
									print ("\nImpossível encontrar arquivo com lista de arestas: "+str(graphs_dir)+str(ego_id)+".edge_list")
								else:
									alters_set = get_alters_set(ego_id,graphs_dir+str(ego_id)+".edge_list")												# Recupera os alters da camada n para ego_id
									jaccard,overlap_lists,overlap_alters = calc_overlap(lists_set,alters_set)

									dataset_jaccard[layer] = jaccard
									dataset_overlap_lists[layer] = overlap_lists
									dataset_overlap_alters[layer] = overlap_alters
					
							save_file(ego_id,dataset_jaccard,out_file_jaccard)								# Salvar arquivo texto
							save_file(ego_id,dataset_overlap_lists,out_file_overlap_lists)
							save_file(ego_id,dataset_overlap_alters,out_file_overlap_alters)

							dataset_json_jaccard[ego_id] = dataset_jaccard									# Salvar arquivo json
							dataset_json_overlap_lists[ego_id] = dataset_overlap_lists
							dataset_json_overlap_alters[ego_id] = dataset_overlap_alters
					
							print ("Ego: "+str(i)+" - Jaccard: "+str(dataset_json_jaccard[ego_id])+" - Lists: "+str(dataset_json_overlap_lists[ego_id])+" - Alters: "+str(dataset_json_overlap_alters[ego_id]))
							print
			
			name = "jaccard"
			save_json(output_dir_json,dataset_json_jaccard,name)
			name = "overlap_lists"
			save_json(output_dir_json,dataset_json_overlap_lists,name)
			name = "overlap_alters"
			save_json(output_dir_json,dataset_json_overlap_alters,name)
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

######################################################################################################################

if __name__ == "__main__": main()