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
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print"  3 - GN"		
	print"  4 - COPRA - Partition"						
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"
	elif op2 == 3:
		alg = "gn"
	elif op2 == 4:
		alg = "copra_partition"				
	else:
		print("Opção inválida! Saindo...")
		sys.exit()		
######################################################################
	
	metric = 'modularity'
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

	dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
	data3 = prepare(dataset3)
	
######################################################################
######################################################################		


	if data1 is not None and data3:
		plot_modularity.plot_bars_full_without_singletons(output,data1,data3,metric,alg)		
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