# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plot_metrics
import calc
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar as métricas de avaliação sem ground_truth
##					Versão 2 - não considera without singletons
## 
######################################################################################################################################################################

######################################################################################################################################################################
def prepare_box_plot(dataset,metric): #Só para Infomap
	if not os.path.isdir(dataset):
		print ("Diretório não encontrado: "+str(dataset))
	else:	
		metric_plot = {}																	# Armazenar o nome da rede e o maior valor do métrica

		for directory in os.listdir(dataset):
			if os.path.isdir(dataset+directory):
				net = str(directory)
				for file in os.listdir(dataset+directory):					# file = Threshold.txt ou json
					with open(dataset+directory+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							_metric = []
							for k,v in data.iteritems():
								_metric.append(v[metric])
			
							metric_plot[net] = _metric
		return metric_plot

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
	print" 					Impressão de Gráficos - Métricas de Avaliação Sem Ground - Truth	"
	print"																											"
	print"																											"
	print"#################################################################################"
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print
	print"  1 - COPRA - Without Weight - K=10"
	print"  2 - COPRA - Without Weight - K=2"
	print"  4 - OSLOM - Without Weight - K=50"
	print"  5 - RAK - Without Weight"		
	print"  6 - INFOMAP - Partition - Without Weight"												
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
#
	if op2 == 1:
		alg = "copra_without_weight_k10"
	elif op2 == 2:
		alg = "copra_without_weight_k2"
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
	print
	print"  0 - All Metrics"
	print"  1 - Number of Communities"	
	print"  2 - Communities Size"
	print"  3 - Communities Size Normalized"
	print"  4 - Overlap"
	print"  5 - Singletons"
	print"  6 - Non Singletons"
	print"  7 - Alters Ignored"
	print"  8 - Alters Ignored Normalized"
	print"  9 - Greater Community AVG"				
	print
	op2 = int(raw_input("Escolha uma opção acima: "))


	if op2 == 0:
		metrics = ["n_communities","avg_size","avg_size_norm","overlap","n_singletons","n_non_singletons","alters_ignored","alters_ignored_norm","greater_comm","greater_comm_norm","smaller_comm"]
	elif op2 == 1:
		metrics = ["n_communities"]	
	elif op2 == 2:
		metrics = ["avg_size"]
	elif op2 == 3:
		metrics = ["avg_size_norm"]
	elif op2 == 4:
		metrics = ["overlap"]
	elif op2 == 5:
		metrics = ["n_singletons"]		
	elif op2 == 6:
		metrics = ["n_non_singletons"]
	elif op2 == 7:
		metrics = ["alters_ignored"]
	elif op2 == 8:
		metrics = ["alters_ignored_norm"]
	elif op2 == 9:
		metrics = ["greater_comm"]
	elif op2 == 10:
		metrics = ["greater_comm_norm"]
	elif op2 == 11:
		metrics = ["smaller_comm"]
	else:
		print("Opção inválida! Saindo...")
		sys.exit()
	print ("\n")
######################################################################

	for metric in metrics:
		data_full = {}
		print"#################################################################################"
		print ("\nPreparando dados para o algoritmo: "+str(alg))
		data1 = {}
			
		dataset1 = str(source)+"graphs_with_ego/"+str(alg)+"/full/"	
		data1 = prepare_box_plot(dataset1,metric)
		title = str(metric)+"_graphs_with_ego_"+str(alg)+"_full_"	
		if data1 is not None:
			plot_metrics.box_plot_without_singletons(output,data1,metric,str(alg)) # Só para INFOMAP
	
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/communities_statistics/boxplots/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()