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
##		Status - Versão 1 - Script para plotar a métricas com todos os algoritmos no mesmo grafo
## 
######################################################################################################################################################################
def prepare(dataset,metric):
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
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
							M = calc.calcular_full(data)
							if M is not None:						
								if	float(M['media']) > metric_plot[net][metric]:
									metric_plot[net] = {'threshold': threshold, metric:float(M['media']),'std':float(M['desvio_padrao'])}
		return metric_plot
		
######################################################################################################################################################################
##		Preparar os dados...
######################################################################################################################################################################
def instructions(metric,alg):
######################################################################		
######################################################################
	
	data1 = {}
	data2 = {}
	data3 = {}
	data4 = {}

######################################################################		

	dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
	data1 = prepare(dataset1,metric)

######################################################################				

	dataset2 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/without_singletons/"	
	data2 = prepare(dataset2,metric)

######################################################################

	dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
	data3 = prepare(dataset3,metric)
######################################################################		

	dataset4 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/without_singletons/"
	data4 = prepare(dataset4,metric)

######################################################################
######################################################################		
	
	if data1 is not None and data2 is not None and data3 is not None and data4 is not None:
		if len(data1) == len(data2) == len(data3) == len(data4):
			data_full = [data1,data2,data3,data4]
			return data_full	
	
	else:
		print ("\nImpossível gerar gráfico para os 04 cenários...\n")
		print data1
		print data2
		print data3
		print data4	

	
	
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
	print" 			Impressão de Gráficos - Métricas de Avaliação Sem Ground - Truth			"
	print"																											"
	print" Escolha o algoritmo usado na detecção das comunidades									"
	print"																											"
	print"#################################################################################"
	print"#################################################################################"
	print
	print"  1 - Average Degree"
	print"  2 - Conductance"
	print"  3 - Cut Ratio"
	print"  4 - Density"	
	print"  5 - Expansion"
	print"  6 - Normalized Cut"
	print"  7 - Separability"	
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		metric = "average_degree"
	elif op2 == 2:
		metric = "conductance"
	elif op2 == 3:
		metric = "cut_ratio"
	elif op2 == 4:
		metric = "density"
	elif op2 == 5:
		metric = "expansion"
	elif op2 == 6:
		metric = "normalized_cut"
	elif op2 == 7:
		metric = "separability"		
	else:
		print("Opção inválida! Saindo...")
		sys.exit()
	print ("\n")

	alg1 = "copra"
	data_full1 = instructions(metric,alg1)
		
	alg2 = "oslom"
	data_full2 = instructions(metric,alg2)
	
	if data_full1 is not None and data_full2 is not None:
		plot_metrics.plot_full_algs(output,data_full1,data_full2,metric)
	else:
		print ("\nImpossível gerar gráfico COM TODOS OS ALGORITMOS para os 04 cenários...\n")
		print alg1,data_full1
		print alg2,data_full2			

######################################################################
######################################################################	
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()