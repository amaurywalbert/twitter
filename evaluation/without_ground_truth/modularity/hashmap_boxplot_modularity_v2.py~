# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plot_modularity
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar a modularidade em BoxPlot
## 
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
							for k,v in data['modularity_data'].iteritems():
								_metric.append(v[0])
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
		alg = "oslom_without_weight_k50"
	elif op2 == 4:
		alg = "oslom_without_weight"
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

######################################################################
	
	metric = 'modularity'

	print"#################################################################################"
	print ("\nPreparando dados para o algoritmo: "+str(alg))
			
	dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
	data1 = prepare_box_plot(dataset1,metric)											 		#Só para Infomap
	if data1 is not None:
		plot_modularity.box_plot_without_singletons(output,data1,metric,alg)			# Só para INFOMAP
	else:
		print ("\nImpossível gerar gráfico para o cenário...\n")
		print data1
	
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