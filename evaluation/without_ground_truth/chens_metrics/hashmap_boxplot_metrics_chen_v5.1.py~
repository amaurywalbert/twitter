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
##		Status - Versão 1 - Script para plotar as métricas de avaliação sem ground_truth do Chen
##					Versão 2 - não considera without singletons
## 				Versão 3 - Filtra os dados salvos para impressão dos gráficos. Arquivos foram salvos com todos os calculos.
## 				Versão 4 - Filtra os resultados das outras métricas com o threshold que retorna a maior Modularity Density
## 				Versão 5 - Filtra os resultados das outras métricas com o threshold que retorna a melhor Métrica especificada - ou seja, para cada métrica calculada, salva um arquivo com o melhor threshold.
##					Versão 5.1 - Plota só informações das redes com ego full
######################################################################################################################################################################

######################################################################################################################################################################
#
# Calcular e armazenar o MAIOR valor para cada métrica
#
######################################################################################################################################################################
def prepare_box_plot(dataset,metric):
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
	else:	
		metric_plot = {}
		for directory in os.listdir(dataset):
			if os.path.isdir(dataset+directory):
				net = str(directory)
				for file in os.listdir(dataset+directory):
					with open(dataset+directory+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							_metric = []
							for k,v in data.iteritems():
								_metric.append(v)
			
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
	print" Escolha o algoritmo usado na detecção das comunidades									"
	print"																											"
	print"#################################################################################"
	print "Algoritmo utilizado na detecção das comunidades"
	print
	print"  1 - COPRA - Without Weight - K=10"
	print"  2 - COPRA - Without Weight - K=2-20"
	print"  3 - OSLOM - Without Weight - K=5,10,50"
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
	elif op2 == 2:
		alg = "copra_without_weight"
	elif op2 == 3:
		alg = "oslom_without_weight"
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

######################################################################		
######################################################################

	m_greater = ["modularity_density","modularity","N_modularity","intra_edges","intra_density","modularity_degree","contraction"]
	for metric in m_greater:
		print"#################################################################################"
		print ("\nPreparando dados para o algoritmo: "+str(alg))
		data1 = {}
			
		dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
		data1 = prepare_box_plot(dataset1,metric)											 	
		if data1 is not None:
			plot_metrics.box_plot_without_singletons(output,data1,metric,alg)
		else:
			print ("\nImpossível gerar gráfico para o cenário...\n")
			print data1
######################################################################
			
	m_less = ["inter_edges","expansion","conductance"]
	for metric in m_less:
		print"#################################################################################"
		print ("\nPreparando dados para o algoritmo: "+str(alg))
		data1 = {}
			
		dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
		data1 = prepare_box_plot(dataset1,metric)
		if data1 is not None:
			plot_metrics.box_plot_without_singletons(output,data1,metric,alg)
		else:
			print ("\nImpossível gerar gráfico para o cenário...\n")
			print data1
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
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth_chen/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()