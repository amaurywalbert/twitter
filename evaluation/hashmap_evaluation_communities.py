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
#
# Criar diretórios
#
######################################################################################################################################################################
def create_dirs(x):
	
	if not os.path.exists(x):
		os.makedirs(x)	
######################################################################################################################################################################
##		Status - Versão 1 - Script para gerar arquivo contendo as principais informações sobre as comunidades detectadas...
## 
######################################################################################################################################################################
def get_dataset(dataset, metric=None):
	if not os.path.isdir(dataset):
		print ("Diretório não encontrado (get_dataset): "+str(dataset))
	else:	
		dataset_full = {}																	# Armazenar o nome da rede e o maior valor do métrica
		for directory in os.listdir(dataset):
			if os.path.isdir(dataset+directory):
				net = str(directory)
				for file in os.listdir(dataset+directory):
					with open(dataset+directory+"/"+file, 'r') as f:
						threshold = file.split(".json")
						threshold = threshold[0]
						data_t = {}									#Armazena os dados lidos por threshold
						data = json.load(f)
						if data is not None:
							data_t[threshold] = data
				dataset_full[net] = data_t	
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
	data_chen_mod_density = str(source_chen)+"modularity_density/graphs_with_ego/"+str(alg)+"/full/"
	data_chen_modularity =  str(source_chen)+"modularity/graphs_with_ego/"+str(alg)+"/full/"
	data_chen_intra_density =  str(source_chen)+"intra_density/graphs_with_ego/"+str(alg)+"/full/"
	data_chen_conductance =  str(source_chen)+"conductance/graphs_with_ego/"+str(alg)+"/full/"
	
	data_snap_coef_clust =  str(source_snap)+"coef_clust/graphs_with_ego/"+str(alg)+"/full/"
	data_snap_conductance =  str(source_snap)+"conductance/graphs_with_ego/"+str(alg)+"/full/"
	
	comm = get_dataset(data_comm)
	chen_mod_density = get_dataset(data_chen_mod_density)
	chen_modularity = get_dataset(data_chen_modularity)
	chen_intra_density = get_dataset(data_chen_intra_density)
	chen_conductance = get_dataset(data_chen_conductance)
	
	snap_coef_clust = get_dataset(data_snap_coef_clust)
	snap_conductance = get_dataset(data_snap_conductance)

#	for k,v in snap_conductance.iteritems():
#		print k,v
#		time.sleep(5)
		
	for net,net_data in comm.iteritems():
		if net in ("n1","n2","n3","n4","n9"):
			for threshold,threshold_data in net_data.iteritems():
				dictionary = {}
				output_dir = str(output)+str(alg)+"/"+str(net)+"/"
				create_dirs(output_dir)
				csv = open(output_dir+threshold+"_comm_statistics.csv", "w") #"w" indicates that you're writing strings to the file
				columns = ["ego_id","n_nodes","n_edges","n_comm","max_comm_len","min_comm_len","comm_size_avg","comm_size_std","n_singletons","alters_ignored","chen_modularity_avg","chen_mod_density_avg","chen_conductance_avg","chen_intra_density_avg","snap_coef_clust_avg","snap_conductance_avg"]
				columnTitleRow = ""
				for column in columns:
					columnTitleRow = columnTitleRow+str(column)+","
				csv.write(columnTitleRow+"\n")
		
				i=0
				for ego,ego_data in threshold_data.iteritems():
					i+=1
					print i,net,threshold,ego,ego_data
					print

					ego_id = ego
					n_nodes = ego_data['n_nodes']
					n_edges = ego_data['n_edges']

					n_comm = ego_data['n_communities']
					max_comm_len = ego_data['greater_comm']
					min_comm_len = ego_data['smaller_comm']
					comm_size_avg = ego_data['avg_size']
					comm_size_std = ego_data['std_size']
					n_singletons = ego_data['n_singletons']
					alters_ignored = ego_data['alters_ignored']

					chen_mod_density_avg = chen_mod_density[net][threshold][ego]
					chen_modularity_avg = chen_modularity[net][threshold][ego]
					chen_conductance_avg = chen_conductance[net][threshold][ego]
					chen_intra_density_avg = chen_intra_density[net][threshold][ego]
					
					snap_coef_clust_avg = snap_coef_clust[net][threshold]["coef_clust_data"][ego][0]
					snap_conductance_avg = snap_conductance[net][threshold][ego]["media"]
					
					row = str(ego_id)+","+str(n_nodes)+","+str(n_edges,)+","+str(n_comm)+","+str(max_comm_len)+","+str(min_comm_len)+","+str(comm_size_avg)+","+str(comm_size_std)+","+str(n_singletons)+","+str(alters_ignored)+","+str(chen_modularity_avg)+","+str(chen_mod_density_avg)+","+str(chen_conductance_avg)+","+str(chen_intra_density_avg)+","+str(snap_coef_clust_avg)+","+str(snap_conductance_avg)
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
source_chen = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_chen/"
source_snap = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/"

#Executa o método main
if __name__ == "__main__": main()