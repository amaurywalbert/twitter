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
def prepare_box_plot(dataset,metric): #Só para Infomap
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
	print
#	print"  1 - COPRA"
#	print"  2 - OSLOM"
#	print"  3 - GN"		
#	print"  4 - COPRA - Partition"
	print"  5 - INFOMAP - Partition"
	print"  6 - INFOMAP - Partition - Without Weight"																								
	print
	op1 = int(raw_input("Escolha uma opção acima: "))

#	if op1 == 1:
#		alg = "copra"
#	elif op1 == 2:
#		alg = "oslom"
#	elif op1 == 3:
#		alg = "gn"
#	elif op1 == 4:
#		alg = "copra_partition"
	if op1 == 5:
		alg = "infomap"							
	elif op1 == 6:
		alg = "infomap_without_weight"	
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")
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
		data1 = prepare_box_plot(dataset1,metric)											 	#Só para Infomap
		if data1 is not None:
			plot_metrics.box_plot_without_singletons(output,data1,metric,alg)			# Só para INFOMAP
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
		data1 = prepare_box_plot(dataset1,metric)												#Só para Infomap
		if data1 is not None:
			plot_metrics.box_plot_without_singletons(output,data1,metric,alg)			# Só para INFOMAP
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