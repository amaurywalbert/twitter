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
def prepare(dataset,metric):
	if not os.path.isdir(dataset):
		print ("Diretório não encontrado: "+str(dataset))
	else:	
		metric_plot = {}																	# Armazenar o nome da rede e o maior valor do métrica

		for directory in os.listdir(dataset):
			if os.path.isdir(dataset+directory):
				net = str(directory)
				metric_plot[net] = {'threshold':' ',metric:float(0),'std':float(0)}
				
				for file in os.listdir(dataset+directory):
					threshold = file.split(".json")
					threshold = threshold[0]
					
					with open(dataset+directory+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							_metric = []
							for k,v in data.iteritems():
								_metric.append(v[metric])
							M = calc.calcular_full(_metric)
							if M is not None:						
								if	float(M['media']) > metric_plot[net][metric]:
									metric_plot[net] = {'threshold': threshold, metric:float(M['media']),'std':float(M['desvio_padrao'])}
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
#	print" Escolha o algoritmo usado na detecção das comunidades									"
	print"																											"
	print"#################################################################################"
	print
#	print"  1 - COPRA"
#	print"  2 - OSLOM"
#	print"  3 - GN"		
#	print"  4 - COPRA - Partition"
#	print"  5 - INFOMAP - Partition"												
#	print
#	op1 = int(raw_input("Escolha uma opção acima: "))
#
#	if op1 == 1:
#		alg = "copra"
#	elif op1 == 2:
#		alg = "oslom"
#	elif op1 == 3:
#		alg = "gn"
#	elif op1 == 4:
#		alg = "copra_partition"				
#	elif op1 == 5:
#		alg = "infomap"
#	else:
#		alg = ""
#		print("Opção inválida! Saindo...")
#		sys.exit()	
#	print ("\n")
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
	
		alg = ['copra','oslom','gn','copra_partition','infomap']
		data_full = {}
		for i in range(len(alg)):
			print"#################################################################################"
			print ("\nPreparando dados para o algoritmo: "+str(alg[i]))
			data1 = {}
			data2 = {}
	
######################################################################		
######################################################################

			dataset1 = str(source)+"graphs_with_ego/"+str(alg[i])+"/full/"	
			data1 = prepare(dataset1,metric)
			title = str(metric)+"_graphs_with_ego_"+str(alg[i])+"_full"	

######################################################################				
######################################################################

			dataset2 = str(source)+"graphs_without_ego/"+str(alg[i])+"/full/"	
			data2 = prepare(dataset2,metric)
			title = str(metric)+"_graphs_without_ego_"+str(alg[i])+"_full"	

######################################################################		
######################################################################		

			if data1 is not None and data2:
				if len(data1) == len(data2):
				
#					data_full[alg] = {'data1':data1,'data2':data2}
					plot_metrics.plot_without_singletons(output,data1,data2,metric,str(alg[i]))
			else:
				print ("\nImpossível gerar gráfico para os 02 cenários...\n")
				print data1
				print data2
			
######################################################################
# Plotar todos resultados com todos os algoritmos	
#	plot_metrics.plot_full_without_singletons(output,data_full,metric)
######################################################################	
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/communities_statistics/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()