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

		for file in os.listdir(dataset):
			net = file.split(".json")
			net = net[0]
			modularity_plot[net] = {'threshold':' ','modularity':float(0),'std':float(0)}
	
			with open(dataset+file, 'r') as f:
				for line in f:
					data = json.loads(line)
					threshold = data['threshold']
					M = data['modularity']
					if M is not None:						
						if	float(M['media']) > modularity_plot[net]['modularity']:
							modularity_plot[net] = {'threshold': threshold, 'modularity':float(M['media']),'std':float(M['desvio_padrao'])}
 
		return modularity_plot
		
######################################################################################################################################################################
##		Preparar os dados...
######################################################################################################################################################################
def instructions(metric,alg):
######################################################################		

	dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
	data1 = prepare(dataset1)
	
######################################################################				

	dataset2 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/without_singletons/"	
	data2 = prepare(dataset2)

######################################################################

	dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
	data3 = prepare(dataset3)
		
######################################################################

	dataset4 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/without_singletons/"
	data4 = prepare(dataset4)
	
######################################################################

	data_full = [data1,data2,data3,data4]

	return data_full		
	
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
	print
	print"  1 - Copra"
	print"  2 - Oslom"		
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"
	else:
		print("Opção inválida! Saindo...")
		sys.exit()		
######################################################################
	
	metric = 'modularity'

	alg = "copra"
	data_full1 = instructions(metric,alg)
		
	alg = "oslom"
	data_full2 = instructions(metric,alg)
	
	plot_modularity.plot_full_algs(output,data_full1,data_full2,metric)	

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