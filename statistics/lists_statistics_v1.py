	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, math
import numpy as np
from math import*
import calc
import plot_statistics
import histogram

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Gerar Estatísticas do Dataset - Listas (Ground-Truth)
##			- Numero médio de listas por usuário ego e o desvio padrão...
##			- Eu encontro a lista na rede-ego?? - o tamanho da intersecção pelo tamanho da lista (fração) - para cada Lista.
##			- Quais alters estão na lista? será que é acima de 70%
##
######################################################################################################################################################################


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
def lists_verify(file,alters_set):
	with open(file, 'r') as f:
		_ego_jaccard = []
		_users_by_list	= []											#partial
		lists_by_ego = 0
		users_total = 0
			
		for line in f:													# para cada Lista
			ubl = 0														# usuários por lista
			a = line.split(' ')
			list_set = set()

			for item in a:
				if item != "\n":
					list_set.add(long(item))
					users_total = users_total+1				# necessário pois não dá pra usar o tamanho do conjunto porque há casos em que o mesmo alter aparece em diversas Listas
					ubl+=1
		
			j_m = jaccard_modified(list_set,alters_set)
			_users_by_list.append(ubl)
			_ego_jaccard.append(j_m)
			lists_by_ego = lists_by_ego+1

		users_by_list_average = float(users_total/lists_by_ego)
		ego_jaccard = calc.calcular_full(_ego_jaccard)			
		
#		print _users_by_list								#OK
#		print users_by_list_average							#OK
#		print lists_by_ego										#OK
#		print ego_jaccard['media']								#OK
#		time.sleep(10)												#OK

		return _users_by_list, users_by_list_average, lists_by_ego, ego_jaccard['media']
	
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
	source_dir = "/home/amaury/dataset/ground_truth/lists_users_TXT/"+str(singletons)+"/"
	output_dir = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs)+"_"+str(singletons)+"/"	
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
		
	if not os.path.exists(source_dir):
		print ("\nImpossível encontrar diretório com ground-truth communities: "+str(source_dir))
	else:
		for i in range(10):
			
			users_by_list_average = []
			users_by_list = []
			lists_by_ego = []
			ego_jaccard = [] 			
			i+=1
			net = "n"+str(i)
			graphs_dir = "/home/amaury/graphs/"+str(net)+"/"+str(type_graphs)+"/"

			if not os.path.isdir(graphs_dir):
				print ("\nImpossível encontrar diretório com os grafos: "+str(graphs_dir))
			else:
				i=0
				for file in os.listdir(graphs_dir):																# Para cada ego da rede $net
					ego_id = file.split(".edge_list")
					ego_id = long(ego_id[0])
					
					if not os.path.isfile(source_dir+str(ego_id)+".txt"):
						print ("\nImpossível encontrar arquivo de ground truth: "+str(source_dir)+str(ego_id)+".txt")
					else:
						
						i+=1
						print (str(graphs_dir)+" - recuperando alters para o ego: "+str(i))
						alters_set = recovery_alters(str(graphs_dir)+str(file))											# Recupera os alters para o ego.
						
						_users_by_list,_users_by_list_average, _lists_by_ego, _ego_jaccard = lists_verify(str(source_dir)+str(ego_id)+".txt", alters_set)

						users_by_list_average.append(_users_by_list_average)
						lists_by_ego.append(_lists_by_ego)
						ego_jaccard.append(_ego_jaccard)
						for item in _users_by_list:
							users_by_list.append(item)
			output = str(output_dir)+str(net)+"/"
			if not os.path.exists(output):
				os.makedirs(output)			
			histogram.histogram(users_by_list_average,output,title='Users by Lists - Average', xaxis='Users', yaxis='Lists')
			histogram.histogram(users_by_list,output,title='Users by Lists - Full Egos', xaxis='Users', yaxis='Lists')
			histogram.histogram(lists_by_ego,output,title='Lists by Ego', xaxis='Lists', yaxis='Egos')
			histogram.histogram(ego_jaccard,output,title='Jaccard Modified', xaxis='Jaccard Modified', yaxis='Egos')
												
			USERS_BY_LIST = calc.calcular_full(users_by_list)
			USERS_BY_LIST_AVERAGE = calc.calcular_full(users_by_list_average)
			LISTS_BY_EGO = calc.calcular_full(lists_by_ego)
			JACCARD_AVG = calc.calcular_full(ego_jaccard)
	
#			overview = {'users_by_list':USERS_BY_LIST,'users_by_list_avg':USERS_BY_LIST_AVERAGE,'lists_by_ego':LISTS_BY_EGO,'jaccard_avg':JACCARD_AVG,'ego_jaccard':ego_jaccard}
			overview = {'users_by_list':USERS_BY_LIST,'users_by_list_avg':USERS_BY_LIST_AVERAGE,'lists_by_ego':LISTS_BY_EGO,'jaccard_avg':JACCARD_AVG}

			with open (output_dir+str(net)+".json", 'w') as f:
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