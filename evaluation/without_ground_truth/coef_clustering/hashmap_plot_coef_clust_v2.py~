# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plot_coef_clust
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar a coef_clust
## 
######################################################################################################################################################################
def prepare(dataset):
	if not os.path.isdir(dataset):
		print ("Diretório com coef_clust não encontrado: "+str(dataset))
	else:	
		coef_clust_plot = {}																	# Armazenar o nome da rede e o maior valor do coef_clust - Formato {{'N1':0.012},...}

		for net in os.listdir(dataset):
			if not os.path.isdir(str(dataset)+str(net)+"/"):
				print ("Diretório não encontrado. "+str(dataset)+str(net)+"/")
			else:			
				coef_clust_plot[net] = {'threshold':' ','coef_clust':float(0),'std':float(0)}

				for file in os.listdir(dataset+str(net)+"/"):
					threshold = file.split(".json")
					threshold = threshold[0]

					with open(dataset+str(net)+"/"+str(file), 'r') as f:
						print ("Abrindo: "+str(dataset)+str(net)+"/"+str(file))
						data = json.load(f)
						M = data['coef_clust']
						if M is not None:
							print net,threshold,M['media']				
							if	float(M['media']) > coef_clust_plot[net]['coef_clust']:
								coef_clust_plot[net] = {'threshold': threshold, 'coef_clust':float(M['media']),'std':float(M['desvio_padrao'])}
 
		return coef_clust_plot

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
	print" 					Impressão de Gráficos da coef_clust										"
	print"																											"
	print" Escolha o algoritmo usado na detecção das comunidades									"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - COPRA - Without Weight"
	print"  2 - OSLOM - Without Weight"
	print"  3 - RAK - Without Weight"		
#
#	print"  5 - INFOMAP - Partition"
	print"  6 - INFOMAP - Partition - Without Weight"												
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
#
	if op2 == 1:
		alg = "copra_without_weight"
	elif op2 == 2:
		alg = "oslom_without_weight"
	elif op2 == 3:
		alg = "rak_without_weight"
#	elif op2 == 4:
#		alg = "infomap_without_weight"				
#	if op2 == 5:
#		alg = "infomap_without_weight"
	elif op2 == 6:
		alg = "infomap_without_weight"		
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")		
######################################################################
	
	metric = 'coef_clust'
	data1 = {}
	data2 = {}
	data3 = {}
	data4 = {}
######################################################################		
######################################################################

	dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
	data1 = prepare(dataset1)
	
######################################################################				
######################################################################

#	dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
#	data3 = prepare(dataset3)


#	if data1 is not None and data3:
#		plot_coef_clust.plot_bars_full_without_singletons(output,data1,data3,metric,alg)		
	if data1 is not None:
		plot_coef_clust.plot_full_only_with_ego(output,data1,metric,alg)
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