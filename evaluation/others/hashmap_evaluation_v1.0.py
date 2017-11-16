	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, math
import numpy as np
from math import*
import calc
import plot_evaluation

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Gerar Resultados
##								
## # INPUT: Arquivos com os resultado obtidos em cada métricas 
## # OUTPUT:
##		- Arquivos com estatísticas dos resultados
######################################################################################################################################################################

######################################################################################################################################################################
#
# Salva os dados de cada algoritmo em formato JSON
#
######################################################################################################################################################################
def save_data(output,data,data_overview):
	if not os.path.exists(output):
		os.makedirs(output)
	print ("\n##################################################\n")
	print ("Salvando dados em: "+str(output))
	
	with open(output+"evaluation.json", 'w') as f:
		for k, v in data.iteritems():
			network = k,v	 
			f.write(json.dumps(network)+"\n")	
	with open(output+"statistics_overview.json", 'w') as g:
		for k, v in data_overview.iteritems():	 
			network = k,v	 
			g.write(json.dumps(network)+"\n")
				
	print ("##################################################\n")
	
######################################################################################################################################################################
#
# Prepara apresentação dos resultados para o algoritmo - METRICA
#
######################################################################################################################################################################
def algorithm(comm_data_dir,metric):
	data = {}																				# Armazenar todos os valores da Metrica para cada threshold do algoritmo em cada rede - Formato {'n8': {1: {'soma': 6.059981138000007, 'media': 0.025787153778723433, 'desvio_padrao': 0.006377214443559922, 'variancia': 4.0668864059149294e-05}, 2: {'soma': 6.059981138000007...}}	
	data_overview = {}																	# Armazenar o nome da rede e o maior valor do trheshold do algoritmo para a MetricaI - Formato {{'N1':0.012},...}
	
	if os.path.isdir(comm_data_dir):
		for file in os.listdir(comm_data_dir):
			network = file.split(".json")														# pegar o nome do arquivo que indica o a rede analisada
			network = network[0]
			data_overview[network] = {'threshold':' ',metric:float(0)}
			print ("\n##################################################")
			print ("Recuperando dados da rede "+str(network))	

			if os.path.isfile(comm_data_dir+file):		
				with open(comm_data_dir+file, 'r') as f:
					partial = {}

					for line in f:
						comm_data = json.loads(line) 
						for k, v in comm_data.iteritems():
							values = []
							for item in v:
								if not math.isnan(item):											# exclui calculo de da METRICA que retorna valor NaN
									values.append(item)				

							result = calc.calcular_full(values)									# Calcula média e outros dados da METRICA recuperados para o conjunto de egos usando o threshold k				 				
							if result is not None:						
								if	float(result['media']) > data_overview[network][metric]:
									data_overview[network] = {'threshold':k,metric:float(result['media'])}
								partial[k] = result													# Adiciona os caclulos feitos num dicionário com indice k (ou seja, o threshold usado pelo algoritmo)
								data[network] = partial				
			else:
				print ("Arquivo não encontrado: "+str(comm_data_dir+file))
		
			print data_overview[network]														# Maior média para a rede [network]
	else:
		print ("Diretório não encontrado: "+str(comm_data_dir))					
	print
	print ("##################################################\n")
	return data,data_overview
	print ("##################################################")	

######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(metric,alg):
################################################################################################	
	
	comm_data_dir = str(source)+"graphs_with_ego/"+alg+"/"+str(metric)+"/full/"
	output_dir = str(output)+"graphs_with_ego/"+alg+"/"+str(metric)+"/full/"
		
	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
#	plot_evaluation.plot_single(output,data_overview,metric,alg,title='Graphs with ego - Communities with singletons')	
	data1 = data_overview
################################################################################################

	comm_data_dir = str(source)+"graphs_with_ego/"+alg+"/"+str(metric)+"/without_singletons/"
	output_dir = str(output)+"graphs_with_ego/"+alg+"/"+str(metric)+"/without_singletons/"

	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
#	plot_evaluation.plot_single(output,data_overview,metric,alg,title='Graphs with ego - Communities without singletons')	
	data2 = data_overview
################################################################################################

	comm_data_dir = str(source)+"graphs_without_ego/"+alg+"/"+str(metric)+"/full/"
	output_dir = str(output)+"graphs_without_ego/"+alg+"/"+str(metric)+"/full/"

	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
#	plot_evaluation.plot_single(output,data_overview,metric,alg,title='Graphs without ego - Communities with singletons')
	data3 = data_overview
################################################################################################

	comm_data_dir = str(source)+"graphs_without_ego/"+alg+"/"+str(metric)+"/without_singletons/"
	output_dir = str(output)+"graphs_without_ego/"+alg+"/"+str(metric)+"/without_singletons/"

	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
#	plot_evaluation.plot_single(output,data_overview,metric,alg,title='Graphs without ego - Communities without singletons')	
	data4 = data_overview

################################################################################################
	plot_evaluation.plot_full(output,data1,data2,data3,data4,metric,alg)		
		
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
	print ("Métrica a ser aplicada na geração dos resultados:\n")
	print("01 - NMI - Normalized Mutual Infomation. ")
	print("02 - Ômega Index.")
	print("03 - Jaccard Similarity.")
	print	
	metric_op = int(raw_input("Escolha uma opção acima: "))
	print ("\n##################################################\n")
#######################################################################
	if metric_op == 01:
		metric = "nmi"
#######################################################################		
	elif metric_op == 02:
		metric = "omega"
#######################################################################
	elif metric_op == 03:
		metric = "jaccard"
#######################################################################
	else:
		metric = ""
		print("Opção inválida! Saindo...")
		exit()	
#######################################################################

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

	instructions(metric,alg)
	
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
source = "/home/amaury/Dropbox/evaluation_hashmap/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/"
######################################################################################################################


if __name__ == "__main__": main()