	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
import powerlaw
import seaborn as sns
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import math
from math import*


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
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calcular(valores=None):
	calculos = {}
	if valores:
		if valores.__class__.__name__ == 'list' and calculos.__class__.__name__ == 'dict':
			def somar(valores):
				soma = 0
				for v in valores:
					soma += v
				return soma
 
			def media(valores):
				soma = somar(valores)
				qtd_elementos = len(valores)
				media = soma / float(qtd_elementos)
				return media
 
 			def variancia(valores):
 				_media = media(valores)
 				soma = 0
 				_variancia = 0
 
 				for valor in valores:
 					soma += math.pow( (valor - _media), 2)
 					_variancia = soma / float( len(valores) )
 					return _variancia
 
 			def desvio_padrao(valores):
 				return math.sqrt( variancia(valores) )

			calculos['soma'] = somar(valores)
			calculos['media'] = media(valores)
			calculos['variancia'] = variancia(valores)
			calculos['desvio_padrao'] = desvio_padrao(valores)
			return calculos

######################################################################################################################################################################
#
# Salva os dados de cada algoritmo em formato JSON
#
######################################################################################################################################################################
def save_data(communities,data):
	if not os.path.exists(output_dir+communities):
		os.makedirs(output_dir+communities)
	print
	print
	print ("Salvando dados em: "+str(output_dir)+str(communities))
	with open(output_dir+communities+"result.txt", 'w') as f:
		for k, v in data.iteritems():	 
			print k,v
			f.write(str(k)+str(v)+"\n")
	print ("##################################################")
	
######################################################################################################################################################################
#
# Prepara apresentação dos resultados para o algoritmo COPRA 
#
######################################################################################################################################################################

def nmi_copra(communities_dir):
	nmi_data = {}																				# Armazenar o nome da rede e o maior valor do trheshold do COPRA para o NMI - Formato {{'N1':0.012},...}
	dictionary = {}																			# Armazenar todos os valores NMI para cada threshold do COPRA em cada rede - Formato {'n8': {1: {'soma': 6.059981138000007, 'media': 0.025787153778723433, 'desvio_padrao': 0.006377214443559922, 'variancia': 4.0668864059149294e-05}, 2: {'soma': 6.059981138000007...}}
	for i in range(10):																		# para i variando de N1 a N10
		i+=1
		network = "n"+str(i)
		print ("Recuperando dados da rede "+str(network))
		nmi_data[network] = {'threshold':" ",'nmi':float(0)}
		communities = str(source_dir)+str(communities_dir)+"n"+str(i)+"/"								#Diretório para procurar pelos arquivos do Threshold do COPRA
		partial = {}																			#Armazena as informações do NMI para todos os trhesholds do diretório da rede i - Depois junta tudo no dictionary 
		if os.path.isdir(communities):													
			for file in os.listdir(communities):										# Para cada arquivo no diretório
				values = []																		# Valores de NMI para os 500 egos calculados com o threshold FILE
				threshold = file.split(".txt")											# pegar o nome do arquivo que indica o threshold analisado
				threshold = int(threshold[0])			
				with open(communities+file, 'r') as f:
					for line in f:																# para cada NMI calculado para cada um dos 500 egos, seleciona apenas aqueles em que foi possível recuperar o valor
						a = line.split('\t')
						b = float(a[1])
						if not math.isnan(b):												# exclui calculo de NMI que retorna valor NaN
							values.append(b)				
				result = calcular(values)													# Calcula média e outros dados dos NMIs recuperados para o conjunto de egos usando o threshold FILE				 
				partial[threshold] = result												# Adiciona os caclulos feitos num dicionário com indice FILE (ou seja, o threshold usado pelo COPRA)
				if result is not None:
					if	float(result['media']) > nmi_data[network]['nmi']:
						nmi_data[network] = {'threshold':threshold,'nmi':float(result['media'])}
		else:
			print ("Diretório "+str(communities)+" não encontrado. Continuando...")
	
		dictionary[network] = partial
	print nmi_data
	return nmi_data
	print ("##################################################")	
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print	
	print "#######################################################################"	
	print
	print ("Métrica a ser aplicada na geração dos resultados:")
	print
	print("01 - NMI - Normalized Mutual Infomation. ")
#	print("02 - Ômega Index.")
#	print("03 - Jaccard Similarity.")
	print
	print
	metric_op = int(raw_input("Escolha uma opção acima: "))
	if metric_op == 01:
		metric = "nmi"
#	elif metric_op == 02:
#		metric = "omega"
#	elif metric_op == 03:
#		metric = "jaccard"
	else:
		metric = ""
		print("Opção inválida! Saindo...")
		exit()	
#######################################################################	
	print	
	print "#######################################################################"	
	print
	print ("Algoritmo usado no processo de deteção de comunidades:")
	print
	print("01 - COPRA. ")
	print("02 - ")
	print("03 - ")
	print
	algorithm_op = int(raw_input("Escolha uma opção acima: "))
	if algorithm_op == 01 and metric_op == 01: 
		algorithm = "copra"
#######################################################################		

		communities_full = "graphs_with_ego/"+algorithm+"/"+str(metric)+"/full/"									# Diretório para procurar pelos arquivos do Threshold do COPRA
		data_with_ego = nmi_copra(communities_full)																			# Chama função e passa o parâmetros para cálcular as estatísticas para os resultados obtidos pelo algoritmo em questão
		save_data(communities_full,data_with_ego)


		communities_without_singletons = "graphs_with_ego/"+algorithm+"/"+str(metric)+"/without_singletons/"			# Diretório para procurar pelos arquivos do Threshold do COPRA
		data_with_ego = nmi_copra(communities_without_singletons)																						# Chama função e passa o parâmetros para cálcular as estatísticas para os resultados obtidos pelo algoritmo em questão
		save_data(communities_without_singletons,data_with_ego)	
#######################################################################		

		communities_full = "graphs_without_ego/"+algorithm+"/"+str(metric)+"/full/"									# Diretório para procurar pelos arquivos do Threshold do COPRA
		data_without_ego = nmi_copra(communities_full)																								# Chama função e passa o parâmetros para cálcular as estatísticas para os resultados obtidos pelo algoritmo em questão
		save_data(communities_full,data_without_ego)

		communities_without_singletons = "graphs_without_ego/"+algorithm+"/"+str(metric)+"/without_singletons/"		# Diretório para procurar pelos arquivos do Threshold do COPRA
		data_without_ego = nmi_copra(communities_without_singletons)																					# Chama função e passa o parâmetros para cálcular as estatísticas para os resultados obtidos pelo algoritmo em questão
		save_data(communities_without_singletons,data_without_ego)
		
#######################################################################
	else:
		algorithm = ""
		print("Opção inválida! Saindo...")
		exit()
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
#source_dir = "/home/amaury/Dropbox/evaluation/"
#output_dir = "/home/amaury/Dropbox/statistics/"
source_dir = "/home/amaury/evaluation/"
output_dir = "/home/amaury/statistics/"
######################################################################################################################


if __name__ == "__main__": main()