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

######################################################################################################################################################################
#
# Criar diretórios
#
######################################################################################################################################################################
def create_dirs(x):
	
	if not os.path.exists(x):
		os.makedirs(x)	

######################################################################################################################################################################
#
# Ler arquivos com o dataset
#
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
	print" 	Verficando estatísticas sobre as comunidades detectadas			"
	print"																											"
	print"																											"
	print"#################################################################################"
	print "Algoritmo utilizado na detecção das comunidades"
	print
	print"  1 - COPRA - Without Weight - K=10"
#	print"  2 - COPRA - Without Weight - K=2-20"
#	print"  3 - OSLOM - Without Weight - K=5,10,50"
	print"  4 - OSLOM - Without Weight - K=50"
	print"  5 - RAK - Without Weight"		
#
#	print"  6 - INFOMAP - Partition"
	print"  6 - INFOMAP - Partition - Without Weight"												
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
#
	if op2 == 1:
		alg = "copra_without_weight_k10"
#	elif op2 == 2:
#		alg = "copra_without_weight"
#	elif op2 == 3:
#		alg = "oslom_without_weight"
	elif op2 == 4:
		alg = "oslom_without_weight_k50"
	elif op2 == 5:
		alg = "rak_without_weight"
	elif op2 == 6:
		alg = "infomap_without_weight"		
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")
	print	

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
	data_snap_density =  str(source_snap)+"density/graphs_with_ego/"+str(alg)+"/full/"
	data_snap_modularity =  str(source_snap)+"modularity/graphs_with_ego/"+str(alg)+"/full/"
		
	comm = get_dataset(data_comm)
	chen_mod_density = get_dataset(data_chen_mod_density)
	chen_modularity = get_dataset(data_chen_modularity)
	chen_intra_density = get_dataset(data_chen_intra_density)
	chen_conductance = get_dataset(data_chen_conductance)
	
	snap_coef_clust = get_dataset(data_snap_coef_clust)
	snap_conductance = get_dataset(data_snap_conductance)
	snap_density = get_dataset(data_snap_density)
	snap_modularity = get_dataset(data_snap_modularity)

	#for k,v in snap_modularity.iteritems():
	#	print k,v
	#	time.sleep(5)
		
	for net,net_data in comm.iteritems():
		if net in ("n1","n2","n3","n4","n9"):
			for threshold,threshold_data in net_data.iteritems():
				dictionary = {}
				output_dir = str(output)+str(alg)+"/"+str(net)+"/"
				create_dirs(output_dir)
				csv = open(output_dir+threshold+"_comm_statistics.csv", "w") #"w" indicates that you're writing strings to the file
				columns = ["ego_id","n_nodes","n_edges","n_comm","max_comm_len","min_comm_len","comm_size_avg","comm_size_std","n_singletons","alters_ignored","chen_modularity_avg","chen_mod_density_avg","chen_conductance_avg","chen_intra_density_avg","snap_coef_clust_avg","snap_conductance_avg","snap_density_avg","snap_modularity_avg"]
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
					
					try:
						chen_mod_density_avg = chen_mod_density[net][threshold][ego]
					except Exception as e:
						chen_mod_density_avg = 0
					try:
						chen_modularity_avg = chen_modularity[net][threshold][ego]
					except Exception as e:
						chen_modularity_avg = 0
					try:
						chen_conductance_avg = chen_conductance[net][threshold][ego]
					except Exception as e:
						chen_conductance_avg = 0
					try:
						chen_intra_density_avg = chen_intra_density[net][threshold][ego]
					except Exception as e:
						chen_intra_density_avg = 0

					try:
						snap_coef_clust_avg = snap_coef_clust[net][threshold]["coef_clust_data"][ego][0]
					except Exception as e:
						snap_coef_clust_avg = 0
					try:
						snap_conductance_avg = snap_conductance[net][threshold][ego]["media"]
					except Exception as e:
						snap_conductance_avg = 0
					try:
						snap_density_avg = snap_density[net][threshold][ego]["media"]
					except Exception as e:
						snap_density_avg = 0
					try:
						snap_modularity_avg = snap_modularity[net][threshold]["modularity_data"][ego][0]
					except Exception as e:
						snap_modularity_avg = 
					
					row = str(ego_id)+","+str(n_nodes)+","+str(n_edges,)+","+str(n_comm)+","+str(max_comm_len)+","+str(min_comm_len)+","+str(comm_size_avg)+","+str(comm_size_std)+","+str(n_singletons)+","+str(alters_ignored)+","+str(chen_modularity_avg)+","+str(chen_mod_density_avg)+","+str(chen_conductance_avg)+","+str(chen_intra_density_avg)+","+str(snap_coef_clust_avg)+","+str(snap_conductance_avg)+","+str(snap_density_avg)+","+str(snap_modularity_avg)
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