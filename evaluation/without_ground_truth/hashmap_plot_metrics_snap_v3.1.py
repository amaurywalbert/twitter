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
## 				Versão 3 - Filtra os dados salvos para impressão dos gráficos. Arquivos foram salvos com todos os calculos.
##					Versão 3.1 - Plota só informações das redes com ego full
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
					data_avg_values = []
					threshold = file.split(".json")
					threshold = threshold[0]
					with open(dataset+directory+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							for k,v in data.iteritems():
								data_avg_values.append(v['media'])
							print len(data_avg_values)
												
							M = calc.calcular_full(data_avg_values)
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

	metrics = ["average_degree","conductance","cut_ratio","density","expansion","normalized_cut","separability"]
	for metric in metrics:
		
######################################################################		

		dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
		data1 = prepare(dataset1,metric)

######################################################################				

		if data1 is not None:
			plot_metrics.plot_full_only_with_ego(output,data1,metric,alg)
		else:
			print ("\nImpossível gerar gráfico para os 02 cenários...\n")
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

source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()