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
##					Versão 3 - Usa dados (threshold) gerados pelas métricas do CHEN - Apenas Modularidade estendida.
##					Versão 4 - Usa dados (threshold) gerados pelas métricas do CHEN - Escolhe a métrica do Chen e dá opção para calcular estatísticas das comunidades de acordo com a métrica.
## 
######################################################################################################################################################################
def prepare(dataset,metric,graph_type,alg,file):
	metric_plot = {}																							# Armazenar o nome da rede e o maior valor do métrica			
	with open(file, "r") as f:
		data = json.load(f)
	for net in os.listdir(dataset):																		# Para cada modelo de rede do dataset
		if os.path.isdir(dataset+net):		
			t = data[net]																						# Recebe o melhor threhsold determinado pelas métricas do Chen
			threshold = t['threshold']
			print net, threshold, t 
			if not os.path.isfile(str(dataset)+str(net)+"/"+str(threshold)+".json"):
				print ("Impossível abrir arquivo com threshold: "+str(dataset)+str(net)+"/"+str(threshold)+".json")
			else:
				print ("Lendo arquivo com threshold: "+str(dataset)+str(net)+"/"+str(threshold)+".json")						
				with open(str(dataset)+str(net)+"/"+str(threshold)+".json", 'r') as f:					# Abre arquivo com o melhor threshold			
					data1 = json.load(f)
					if data1 is not None:
						_metric = []
						for k,v in data1.iteritems():
							_metric.append(v[metric])
						M = calc.calcular_full(_metric)															#Calcula a média para a métrica...
						if M is not None:					
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
		metrics = ["n_communities","avg_size","avg_size_norm","overlap","n_singletons","n_non_singletons","alters_ignored","alters_ignored_norm","greater_comm_avg"]
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
		metrics = ["greater_comm_avg"]
	else:
		print("Opção inválida! Saindo...")
		sys.exit()
	print ("\n")
######################################################################

	for metric in metrics:
		
	##################################################################
	
		algorithms = ['copra','oslom','gn','copra_partition','infomap']
		data_full = {}
		for alg in algorithms:
			print"#################################################################################"
			print ("\nPreparando dados para o algoritmo: "+str(alg)+" - Statistics Community Data: "+str(metric))
			data1 = {}
			data2 = {}
			chen_metrics = ["conductance","contraction","expansion","inter_edges","intra_density","intra_edges","modularity","modularity_density"]
			for chen_metric in chen_metrics:
				print ("\nChen Metric: "+str(chen_metric)+"\n")
######################################################################		
######################################################################
				graph_type1 = "graphs_with_ego"
				dataset1 = str(source)+"graphs_with_ego/"+str(alg)+"/full/"	
				if not os.path.isdir(dataset1):
					print ("Diretório não encontrado: "+str(dataset1))
				else:
					if not os.path.isfile(str(threshold_data)+str(graph_type1)+"_"+str(alg)+"_"+str(chen_metric)+".json"):
						print ("Impossível abrir arquivo com os resultados da Métrica: "+str(threshold_data)+str(graph_type1)+"_"+str(alg)+"_"+str(chen_metric)+".json")
					else:
						file1 = str(threshold_data)+str(graph_type1)+"_"+str(alg)+"_"+str(chen_metric)+".json"
						data1 = prepare(dataset1,metric,graph_type1,alg,file1)
						title = str(metric)+"_graphs_with_ego_"+str(alg)+"_full"	

######################################################################				
######################################################################
				graph_type2 = "graphs_without_ego"
				dataset2 = str(source)+"graphs_without_ego/"+str(alg)+"/full/"	
				if not os.path.isdir(dataset2):
					print ("Diretório não encontrado: "+str(dataset2))
				else:	
					if not os.path.isfile(str(threshold_data)+str(graph_type2)+"_"+str(alg)+"_"+str(chen_metric)+".json"):
						print ("Impossível abrir arquivo com os resultados da Métrica: "+str(threshold_data)+str(graph_type2)+"_"+str(alg)+"_"+str(chen_metric)+".json")
					else:
						file2 = str(threshold_data)+str(graph_type2)+"_"+str(alg)+"_"+str(chen_metric)+".json"
						data2 = prepare(dataset2,metric,graph_type2,alg,file2)
						title = str(metric)+"_graphs_without_ego_"+str(alg)+"_full"	

######################################################################		
######################################################################		

				if data1 is not None and data2:
					if len(data1) == len(data2):
						output_dir = output+chen_metric+"/"
						plot_metrics.plot_without_singletons(output,data1,data2,metric,str(alg))
				else:
					print ("\nImpossível gerar gráfico para os 02 cenários...\n")
					print data1
					print data2

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
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/communities_statistics_chen_threshold/"
threshold_data = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth_chen/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()