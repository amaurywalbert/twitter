# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para gerar arquivo contendo as principais informações sobre as comunidades detectadas...
## 
######################################################################################################################################################################
def get_dataset(dataset):
	if not os.path.isdir(dataset):
		print ("Diretório não encontrado: "+str(dataset))
	else:	
		dataset_full = {}																	# Armazenar o nome da rede e o maior valor do métrica

		for directory in os.listdir(dataset):
			if os.path.isdir(dataset+directory):
				net = str(directory)
				for file in os.listdir(dataset+directory):
					with open(dataset+directory+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							dataset_full[net] = data
		return dataset_full

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
	print" 	Verficando estatísticas sobre as comunidades detectadas com o INFOMAP			"
	print"																											"
	print"																											"
	print"#################################################################################"
	print
	alg = 'infomap'
	print
	print"#################################################################################"

######################################################################
	print"#################################################################################"
	print ("\nPreparando dados para o algoritmo: "+str(alg))
	dataset = {}
	data_comm = str(source_comm)+"graphs_with_ego/"+str(alg)+"/full/"
	data_metrics = str(source_metrics)+"graphs_with_ego/"+str(alg)+"/full/"	
	comm = get_dataset(data_comm)
	metrics = get_dataset(data_metrics)

	for net,net_data in comm.iteritems():
		if net in ("n1","n2","n3","n4","n9"):
			dictionary = {}
			csv = open(output+net+"_comm_statistics.csv", "w") #"w" indicates that you're writing strings to the file
			columns = ["ego_id","n_nodes","n_edges","n_comm","max_comm_len","min_comm_len","comm_size_avg","comm_size_std","n_singletons","alters_ignored","mod_density_avg","conductance_avg","density_avg"]
			columnTitleRow = ""
			for column in columns:
				columnTitleRow = columnTitleRow+str(column)+","
			csv.write(columnTitleRow+"\n")
		
			i=0
			for ego,ego_data in net_data.iteritems():
				i+=1
				print i,net,ego,ego_data
				ego_id = ego
				n_nodes = ego_data['n_nodes']
				n_edges = ego_data['n_edges']
				n_comm = ego_data['n_communities']
				#max_comm_len = ego_data['greater_comm']
				#min_comm_len = ego_data['smalleer_comm']
				max_comm_len = 0
				min_comm_len = 0
				comm_size_avg = ego_data['avg_size']
				comm_size_std = ego_data['std_size']
				n_singletons = ego_data['n_singletons']
				alters_ignored = ego_data['alters_ignored']
				mod_density_avg = 0
				conductance_avg = 0
				density_avg = 0
				row = str(ego_id)+","+str(n_nodes)+","+str(n_edges,)+","+str(n_comm)+","+str(max_comm_len)+","+str(min_comm_len)+","+str(comm_size_avg)+","+str(comm_size_std)+","+str(n_singletons)+","+str(alters_ignored)+","+str(mod_density_avg)+","+str(conductance_avg)+","+str(density_avg)
				csv.write(row+"\n")				
				print
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source_comm = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/"
source_metrics = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_chen"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()