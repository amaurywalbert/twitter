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
##		Status - Versão 1 - Gerar Estatísticas do Dataset - Listas (Ground-Truth)
##			- Numero médio de listas por usuário ego e o desvio padrão...
##			- Eu encontro a lista na rede-ego?? - o tamanho da intersecção pelo tamanho da lista (fração) - para cada Lista.
##			- Quais alters estão na lista? será que é acima de 70%
##
##										AVALIA SOMENTE OS MEMBROS DAS LISTAS
######################################################################################################################################################################

################################################################################################
# Função para converter nome da rede
################################################################################################
def convert_label(net):
	network = ' '
	
	if net == 'n1':
		network = 'follow'
						
	elif net == 'n2':
		network = 'retweets'			
			
	elif net == 'n3':
		network = 'likes'
			
	elif net == 'n4':
		network = 'mentions'
			
	elif net == 'n9':
		network = 'followers'
						
	elif net == 'n5':
		network = 'co-follow'
					
	elif net == 'n6':
		network = 'co-retweets'
		
	elif net == 'n7':
		network = 'co-likes'
		
	elif net == 'n8':
		network = 'co-mentions'
				
	elif net == 'n10':
		network = 'co-followers'
	
	else:
		network = ' '	

	return network
			
################################################################################################
# Função para calcular o csj entre dois conjuntos de dados
################################################################################################         
def jaccard_modified(list_set,alters_set):
	
	intersection = len(list_set.intersection(alters_set))	
	rate = intersection/float(len(list_set))						#Tamanho da interseção dos conjuntos sobre o tamanho da lista... verifica se os membros das Listas estão no conjunto de alters.

	return rate
	
######################################################################################################################################################################
#
# Recupera cada lista e compara com o conjunto de alters
#
###############################################################
def lists_verify(file):
	with open(file, 'r') as f:
		_users_by_list	= []											#partial
		lists_by_ego = 0
		users_total = 0
		n_lists = 0														# numero de listas
		
			
		for line in f:													# Users_by_list - users para cada Lista
			ubl = 0														# usuários por lista
			a = line.split(' ')
			list_set = set()

			for item in a:
				if item != "\n":
					list_set.add(long(item))
					users_total = users_total+1				# necessário pois não dá pra usar o tamanho do conjunto porque há casos em que o mesmo alter aparece em diversas Listas
					ubl+=1
		
			_users_by_list.append(ubl)
			lists_by_ego = lists_by_ego+1
			n_lists = n_lists+1
			
		users_by_list_avg = float(users_total/lists_by_ego)			
		

		return _users_by_list, users_by_list_avg, lists_by_ego
	


######################################################################################################################################################################
#
# Recupera cada lista e compara com o conjunto de alters
#
###############################################################
def jaccard_verify(file,alters_set):
	with open(file, 'r') as f:
		_ego_jaccard = []
		_full_lists_jaccard = []
			
		for line in f:													# para cada Lista
			a = line.split(' ')
			list_set = set()
			if a is not None and a[0] != " ":
				for item in a:
					if item != "\n":
						list_set.add(long(item))
		
				j_m = jaccard_modified(list_set,alters_set)
				_ego_jaccard.append(j_m)
				_full_lists_jaccard.append(j_m)

		ego_jaccard = calc.calcular_full(_ego_jaccard)			
		

		return ego_jaccard['media'], _full_lists_jaccard
	
######################################################################################################################################################################
#
# Recupera o conjunto de alters a a partir do grafo
#
###############################################################
def recovery_alters(file):
	alters_set = set()
	with open(file, 'r') as f:
		for line in f:			
			a = line.split(' ')
			alters_set.add(long(a[0]))									#Pega só o primeiro campo - nó1
			alters_set.add(long(a[1]))									#Pega só o primeiro campo - nó 2 -  Exclui o peso das arestas...
	return alters_set
######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(type_graphs,singletons):	
	source_dir = "/home/amaury/dataset/ground_truth_only_members/lists_users_TXT/"+str(singletons)+"/"
	output_dir = "/home/amaury/Dropbox/lists_properties_only_members/"+str(type_graphs)+"_"+str(singletons)+"/"	
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
		
	if not os.path.exists(source_dir):
		print ("\nImpossível encontrar diretório com ground-truth communities: "+str(source_dir))
	else:
		users_by_list_avg = []
		users_by_list = []
		lists_by_ego = []
		
		for file in os.listdir(source_dir):
			_users_by_list, _users_by_list_avg, _lists_by_ego = lists_verify(source_dir+file)
			users_by_list_avg.append(_users_by_list_avg) 													# Usuários por lista - média por ego
			lists_by_ego.append(_lists_by_ego)
			for item in _users_by_list:
				users_by_list.append(item)
								
		graphics.histogram(users_by_list_avg,output_dir,title='Users by Lists - Average by Ego', xaxis='Users', yaxis='Lists')
		graphics.histogram(users_by_list,output_dir,title='Users by Lists - Full Egos', xaxis='Users', yaxis='Lists')
		graphics.histogram(lists_by_ego,output_dir,title='Lists by Ego', xaxis='Lists', yaxis='Egos')
												
		USERS_BY_LIST = calc.calcular_full(users_by_list)
		USERS_BY_LIST_AVG = calc.calcular_full(users_by_list_avg)
		LISTS_BY_EGO = calc.calcular_full(lists_by_ego)	
		overview = {'users_by_list':USERS_BY_LIST,'users_by_list_avg':USERS_BY_LIST_AVG,'lists_by_ego':LISTS_BY_EGO}
		lists_details = {'users_by_lists_avg': users_by_list_avg, 'number_of_lists':lists_by_ego}

		with open (output_dir+"lists_overview.json", 'w') as f:
			f.write(json.dumps(overview))
		with open (output_dir+"lists_details.json", 'w') as f:
			f.write(json.dumps(lists_details))			
					
		for i in range(10):
			
			ego_jaccard = [] 
			full_lists_jaccard = []		
			i+=1
			net = "n"+str(i)
			network = convert_label(net)
			graphs_dir = "/home/amaury/graphs/"+str(net)+"/"+str(type_graphs)+"/"

			if not os.path.isdir(graphs_dir):
				print ("\nImpossível encontrar diretório com os grafos: "+str(graphs_dir))
			else:
				i=0
				for file in os.listdir(graphs_dir):																# Para cada ego da rede $net
					if not os.path.isfile(graphs_dir+file):
						print ("\nImpossível encontrar arquivo com lista de arestas: "+str(graphs_dir)+str(file))
					else:							
						ego_id = file.split(".edge_list")
						ego_id = long(ego_id[0])
					
						if not os.path.isfile(source_dir+str(ego_id)+".txt"):
							print ("\nImpossível encontrar arquivo de ground truth: "+str(source_dir)+str(ego_id)+".txt")
						else:
						
							i+=1
							print (str(graphs_dir)+" - recuperando alters para o ego: "+str(i)+" - "+str(ego_id))
							alters_set = recovery_alters(str(graphs_dir)+str(file))											# Recupera os alters para o ego.
						
							_ego_jaccard, _full_lists_jaccard = jaccard_verify(str(source_dir)+str(ego_id)+".txt", alters_set)

							ego_jaccard.append(_ego_jaccard)

							for item in _full_lists_jaccard:
								full_lists_jaccard.append(item)
								
				output = str(output_dir)+str(network)+"/"
				if not os.path.exists(output):
					os.makedirs(output)

				graphics.histogram(ego_jaccard,output,title=str(network)+' - Jaccard Modified by Egos', xaxis='Jaccard Modified', yaxis='Egos')
				graphics.histogram(full_lists_jaccard,output,title=str(network)+' - Jaccard Modified by Lists', xaxis='Jaccard Modified', yaxis='Lists')

				JACCARD_AVG = calc.calcular_full(ego_jaccard)
				FULL_LISTS_JACCARD = calc.calcular_full(full_lists_jaccard)	

				overview = {'jaccard_by_ego_avg':JACCARD_AVG, 'jaccard_by_lists':FULL_LISTS_JACCARD}

				with open (output+str(network)+".json", 'w') as f:
					f.write(json.dumps(overview))
													
		
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
	instructions(type_graphs1,singletons2)
	instructions(type_graphs2,singletons1)
	instructions(type_graphs2,singletons2)	
	
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