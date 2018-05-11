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
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print"  3 - GN"		
	print"  4 - COPRA - Partition"
	print"  5 - INFOMAP - Partition"												
	print
	op1 = int(raw_input("Escolha uma opção acima: "))

	if op1 == 1:
		alg = "copra"
	elif op1 == 2:
		alg = "oslom"
	elif op1 == 3:
		alg = "gn"
	elif op1 == 4:
		alg = "copra_partition"
	elif op1 == 5:
		alg = "infomap"							
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")
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