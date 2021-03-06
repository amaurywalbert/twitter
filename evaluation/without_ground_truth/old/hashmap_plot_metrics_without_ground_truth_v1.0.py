	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, math
import numpy as np
from math import*
import calc
import plot_metrics_statistics

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Gerar Estatísticas a partir dos dados Obtidos pelos scrits do Amaury
##				
##							0.2 - Calcula qual melhor threshold
##							0.3 - Plota gráficos comparando cada métrica
##												
## # INPUT: Arquivos com os resultado obtidos em cada métricas 
## # OUTPUT:
##		- Arquivos com estatísticas dos resultados
######################################################################################################################################################################


######################################################################################################################################################################
#
# Prepara apresentação dos resultados para cada - METRICA
#
######################################################################################################################################################################
def algorithm(data_source,metric):
	
	data_overview = {}																	# Armazenar o nome da rede e o maior valor do trheshold do algoritmo para a MetricaI - Formato {{'N1':0.012},...	
	data = {}

	if not os.path.isdir(data_source):
		print ("\n##################################################\n\n")
		print ("Diretório não encontrado: "+str(data_source))
		print ("\n\n##################################################\n")					
	else:	

		for file in os.listdir(data_source):
			network = file.split(".json")														# pegar o nome do arquivo que indica o a rede analisada
			network = network[0]

			data_overview[network] = {'threshold':' ',metric:float("-inf"),'std':float(0)}
			print ("##################################################")
			print ("Preparando resultados para a métrica: "+(metric)+" - Recuperando dados da rede "+str(network))	
		
			with open(data_source+file, 'r') as g:
				for line in g:
					comm_data = json.loads(line) 
					for k, v in comm_data.iteritems():										# Para cada threshold
						values = []
						for item in v:
							if not math.isnan(item):
								if item != float("inf") and item != float("-inf"): 											# exclui calculo de da METRICA que retorna valor NaN e Infinity
									values.append(item)
						print 						
						print metric
						print values
						print
													
						result = calc.calcular_full(values)									# Calcula média e outros dados da METRICA recuperados para o conjunto de egos usando o threshold k				 				
						if result is not None:	
														
							if	float(result['media']) > data_overview[network][metric]:
								data_overview[network] = {'threshold':k,metric:float(result['media']),'std':float(result['desvio_padrao'])}
								result['n_egos'] = len(values)
								result['t_egos'] = len(v)
								data[network] = {'threshold':k,metric:result}
		print ("##################################################")	
	
	return data_overview

######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(alg):
################################################################################################
################################################################################################

	output_graphics_single = output+"/graphics/bars_single/"
	output_graphics = output+"/graphics/bars/"
	
	source_dir = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/by_metrics/"

################################################################################################

	data_print1 = {}

	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):

			data_source = str(source_dir)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"			
			data_overview = algorithm(data_source,metric)	
			data_print1[metric] = data_overview
	
	for k, v in data_print1.iteritems():
		if data_print1[k] is not None:
			print data_print1[k]
			title = "Avaliação das redes usando a métrica "+str(k)+" e algoritmo "+str(alg)+"\nREDE COM EGO - COMUNIDADES COM SINGLETONS"	
			plot_metrics_statistics.plot_single(output_graphics_single,data_print1[k],k,alg,title)		

################################################################################################

	data_print2 = {}

	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):

			data_source = str(source_dir)+str(metric)+"/graphs_with_ego/"+str(alg)+"/without_singletons/"			
			data_overview = algorithm(data_source,metric)	
			data_print2[metric] = data_overview
	
	for k, v in data_print2.iteritems():
		if data_print2[k] is not None:
			print data_print2[k]
			title = "Avaliação das redes usando a métrica "+str(k)+" e algoritmo "+str(alg)+"\nREDE COM EGO - COMUNIDADES SEM SINGLETONS"	
			plot_metrics_statistics.plot_single(output_graphics_single,data_print2[k],k,alg,title)
			
################################################################################################

	data_print3 = {}

	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):

			data_source = str(source_dir)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"			
			data_overview = algorithm(data_source,metric)	
			data_print3[metric] = data_overview
	
	for k, v in data_print3.iteritems():
		if data_print3[k] is not None:
			print data_print3[k]
			title = "Avaliação das redes usando a métrica "+str(k)+" e algoritmo "+str(alg)+"\nREDE COM SEM - COMUNIDADES COM SINGLETONS"	
			plot_metrics_statistics.plot_single(output_graphics_single,data_print3[k],k,alg,title)
						
################################################################################################

	data_print4 = {}

	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):

			data_source = str(source_dir)+str(metric)+"/graphs_without_ego/"+str(alg)+"/without_singletons/"			
			data_overview = algorithm(data_source,metric)	
			data_print4[metric] = data_overview
	
	for k, v in data_print4.iteritems():
		if data_print4[k] is not None:
			print data_print4[k]
			title = "Avaliação das redes usando a métrica "+str(k)+" e algoritmo "+str(alg)+"\nREDE SEM EGO - COMUNIDADES SEM SINGLETONS"	
			plot_metrics_statistics.plot_single(output_graphics_single,data_print4[k],k,alg,title)
					
################################################################################################

# Salvando Gráficos Completos

	if data_print1 is not None and data_print2 is not None and data_print3 is not None and data_print4 is not None:
		for k, v in data_print1.iteritems():
			plot_metrics_statistics.plot_full(output_graphics,data_print1[k],data_print2[k],data_print3[k],data_print4[k],k,alg)
	else:
		print ("\nConferir arquivos com as métricas para impressão de gráfico completo\n")	
		
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "\n#######################################################################\n"	

	print "\n#######################################################################\n"	
	print ("Algoritmo usado na detecção das comunidades:\n")
	print("01 - COPRA ")
	print("02 - OSLOM")
	print	
	alg_op = int(raw_input("Escolha uma opção acima: "))
	print ("\n##################################################\n")
#######################################################################
	if alg_op == 01:
		alg = "copra"
#######################################################################		
	elif alg_op == 02:
		alg = "oslom"
#######################################################################
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		exit()	
#######################################################################

	instructions(alg)
	
#######################################################################
	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
#####Alterar as linhas para Dropbox quando executado em ambiente de produção
source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth/"
######################################################################################################################

if __name__ == "__main__": main()