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
##		Status - Versão 1 - Script para plotar as métricas de avaliação sem ground_truth do Chen - Para todos os algoritmos
##					Versão 2 - não considera without singletons
## 				Versão 3 - Filtra os dados salvos para impressão dos gráficos. Arquivos foram salvos com todos os calculos.
## 				Versão 4 - Filtra os resultados das outras métricas com o threshold que retorna a maior Modularity Density
## 				Versão 5 - Filtra os resultados das outras métricas com o threshold que retorna a melhor Métrica especificada - ou seja, para cada métrica calculada, salva um arquivo com o melhor threshold.
##					Versão 5.1 - Plota só informações das redes com ego full
######################################################################################################################################################################

######################################################################################################################################################################
#
# Calcular e armazenar o MAIOR threshold para cada métrica
#
######################################################################################################################################################################
def metric_calc_greater_than(dataset,metric,graph_type,alg): # Verifica pelo melhor threshold. Em caso de empate pega o último threshold verificado.
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
	else:	
		best_t = {}																	# Armazenar o nome da rede e o melhor valor do métrica

		for net in os.listdir(dataset):
			print
			if os.path.isdir(dataset+net):
				best_t[net] = {'threshold':' ',metric:float("inf"),'std':float(0)}
				for file in os.listdir(dataset+net):
					data_avg_values = []
					threshold = file.split(".json")
					threshold = threshold[0]
					with open(dataset+net+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							for k,v in data.iteritems():
								data_avg_values.append(v)
							#print len(data_avg_values)
												
							M = calc.calcular_full(data_avg_values)
							if M is not None:

								print threshold, M['media']
								
								if	float(M['media']) <= best_t[net][metric]:
									best_t[net] = {'threshold': threshold, metric:float(M['media']),'std':float(M['desvio_padrao'])}
			print																		
		with open(str(output)+str(graph_type)+"_"+str(alg)+"_"+str(metric)+"_best_threshold.json", "w") as f:
			f.write(json.dumps(best_t))
		return best_t


######################################################################################################################################################################
#
# Calcular e armazenar o MENOR threshold para cada métrica
#
######################################################################################################################################################################
def metric_calc_less_than(dataset,metric,graph_type,alg): # Verifica pelo melhor threshold. Em caso de empate pega o último threshold verificado.
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
	else:	
		best_t = {}																	# Armazenar o nome da rede e o melhor valor do métrica

		for net in os.listdir(dataset):
			print
			if os.path.isdir(dataset+net):
				best_t[net] = {'threshold':' ',metric:float("-inf"),'std':float(0)}
				for file in os.listdir(dataset+net):
					data_avg_values = []
					threshold = file.split(".json")
					threshold = threshold[0]
					with open(dataset+net+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							for k,v in data.iteritems():
								data_avg_values.append(v)
							#print len(data_avg_values)
												
							M = calc.calcular_full(data_avg_values)
							if M is not None:

								print threshold, M['media']
								
								if	float(M['media']) >= best_t[net][metric]:
									best_t[net] = {'threshold': threshold, metric:float(M['media']),'std':float(M['desvio_padrao'])}
			print																		
		with open(str(output)+str(graph_type)+"_"+str(alg)+"_"+str(metric)+"_best_threshold.json", "w") as f:
			f.write(json.dumps(best_t))
		return best_t

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
	print" Impressão de Gráficos - Métricas de Avaliação Sem Ground - Truth						"
	print"																											"
	
	algs = ["copra_without_weight_k2","oslom_without_weight_k50","rak_without_weight","infomap_without_weight"]
	
	m_greater = ["modularity_density","modularity","intra_edges","intra_density","contraction"]
	for metric in m_greater:
		algorithms_data = []	
		for alg in algs:
			graph_type1 = "graphs_with_ego"
			dataset1 = str(source)+str(metric)+"/"+str(graph_type1)+"/"+str(alg)+"/full/"	
			best_t1 = metric_calc_greater_than(dataset1,metric,graph_type1,alg)
			if best_t1 is not None:
				algorithms_data.append(best_t1)						
			else:
				print ("\nImpossível gerar gráfico para o cenário...\n")
				print best_t1
				exit(0)
		plot_metrics.plot_full_algs_only_with_ego(output,algorithms_data,metric)
######################################################################		
######################################################################

	m_less = ["inter_edges","expansion","conductance"]
	for metric in m_less:

		algorithms_data = []
		for alg in algs:
				
			graph_type1 = "graphs_with_ego"
			dataset1 = str(source)+str(metric)+"/"+str(graph_type1)+"/"+str(alg)+"/full/"	
			best_t1 = metric_calc_less_than(dataset1,metric,graph_type1,alg)		
			if best_t1 is not None:
				algorithms_data.append(best_t1)						
			else:
				print ("\nImpossível gerar gráfico para o cenário...\n")
				print best_t1
				exit(0)
		plot_metrics.plot_full_algs_only_with_ego(output,algorithms_data,metric)
######################################################################
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_chen/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth_chen/full_algs/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()