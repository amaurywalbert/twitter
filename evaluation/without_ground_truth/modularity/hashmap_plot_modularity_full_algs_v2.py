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
##		Status - Versão 1 - Script para plotar a modularidade
## 
######################################################################################################################################################################
def prepare(dataset):
	if not os.path.isdir(dataset):
		print ("Diretório com modularidades não encontrado: "+str(dataset))
	else:	
		modularity_plot = {}																	# Armazenar o nome da rede e o maior valor do da modularidade - Formato {{'N1':0.012},...}

		for net in os.listdir(dataset):
			if not os.path.isdir(str(dataset)+str(net)+"/"):
				print ("Diretório não encontrado. "+str(dataset)+str(net)+"/")
			else:			
				modularity_plot[net] = {'threshold':' ','modularity':float(0),'std':float(0)}

				for file in os.listdir(dataset+str(net)+"/"):
					threshold = file.split(".json")
					threshold = threshold[0]

					with open(dataset+str(net)+"/"+str(file), 'r') as f:
						data = json.load(f)
						M = data['modularity']
						if M is not None:
							print net,threshold,M['media']			
							if	float(M['media']) > modularity_plot[net]['modularity']:
								modularity_plot[net] = {'threshold': threshold, 'modularity':float(M['media']),'std':float(M['desvio_padrao'])}
 			print ("\n#####################################################################################\n")
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
	print" 					Impressão de Gráficos da Modularidade										"
	print"																											"
	print" Escolha o algoritmo usado na detecção das comunidades									"
	print"																											"
	print"#################################################################################"

######################################################################

	algs = ["copra_without_weight","copra_without_weight_k10","oslom_without_weight_k50","rak_without_weight","infomap_without_weight"]	
	metric = 'modularity'
	algorithms_data = []

######################################################################		
	for alg in algs:
		dataset = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
		data = prepare(dataset)
		if data is not None:
			algorithms_data.append(data)						
	plot_modularity.plot_full_algs_only_with_ego(output,algorithms_data,metric)

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