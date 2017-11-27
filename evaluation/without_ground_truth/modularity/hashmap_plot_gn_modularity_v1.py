# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plot_modularity
import calc
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar a modularidade do algoritmo GN
## 
######################################################################################################################################################################
def prepare(dataset):
	if not os.path.isdir(dataset):
		print ("Diretório com modularidades não encontrado: "+str(dataset))
	else:	
		modularity_plot = {}																	# Armazenar o nome da rede e o maior valor do da modularidade - Formato {{'N1':0.012},...}

		for file in os.listdir(dataset):
			net = file.split(".json")
			net = net[0]
			with open(dataset+file, 'r') as f:
				data = json.load(f)
			M = calc.calcular_full(data)			
			if M is not None:
				modularity_plot[net] = {'threshold': '1', 'modularity':float(M['media']),'std':float(M['desvio_padrao'])}
 
		return modularity_plot

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
	print" 					Impressão de Gráficos da Modularidade do Algoritmo GN									"
	print"																											"
######################################################################
	alg = 'girvan_newman'
	metric = 'modularity'
	data1 = {}
	data2 = {}
	data3 = {}
	data4 = {}
######################################################################		
######################################################################

	dataset1 = str(source)+"graphs_with_ego/"	
	data1 = prepare(dataset1)

######################################################################
######################################################################

	dataset2 = str(source)+"graphs_without_ego/"	
	data2 = prepare(dataset2)

######################################################################		
######################################################################

	if data1 is not None and data2 is not None:
		plot_modularity.plot_bars_gn(output,data1,data2,metric,alg)		

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

source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/modularity_gn/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth/modularity_gn/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()