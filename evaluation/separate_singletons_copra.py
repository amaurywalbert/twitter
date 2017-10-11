	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Receber o conjunto de conjunto de comunidades e o ground_truth e separar em conjunto completo e conjunto sem singletons.
##								
## # INPUT:
##		- Arquivos com as comunidades completas
## # OUTPUT:
##		- Arquivos com as comunidades sem singletons
######################################################################################################################################################################

######################################################################################################################################################################
#
# Salva os dados de cada algoritmo em formato JSON
#
######################################################################################################################################################################
def save_data(data,graph_type,metric,algorithm):
	print
	print ("Salvando dados... FUNÇÃO EM DESENVOLVIMENTO!")
	print
	
######################################################################################################################################################################
#
# Prepara apresentação dos resultados para o algoritmo COPRA 
#
######################################################################################################################################################################

def nmi_copra(graph_type,metric,algorithm):
	nmi_data = {}																				# Armazenar o nome da rede e o maior valor do trheshold do COPRA para o NMI - Formato {{'N1':0.012},...}
	os.system('clear')
	print ("##################################################")
	print ("Recuperando dados da métrica "+str(metric)+" calculada nas comunidades detectadas pelo algoritmo "+str(algorithm))
	print ("##################################################")
	print
	dictionary = {}																			# Armazenar todos os valores NMI para cada threshold do COPRA em cada rede - Formato {'n8': {1: {'soma': 6.059981138000007, 'media': 0.025787153778723433, 'desvio_padrao': 0.006377214443559922, 'variancia': 4.0668864059149294e-05}, 2: {'soma': 6.059981138000007...}}
	for i in range(10):																		# para i variando de N1 a N10
		print ("##################################################")
		i+=1
		network = "n"+str(i)
		print ("Recuperando dados da rede "+str(network))
		nmi_data[network] = {'threshold':" ",'nmi':float(0)}
		communities = str(source_dir)+str(graph_type)+"/"+algorithm+"/"+str(metric)+"/n"+str(i)+"/"	#Diretório para procurar pelos arquivos do Threshold do COPRA
		partial = {}																											#Armazena as informações do NMI para todos os trhesholds do diretório da rede i - Depois junta tudo no dictionary 
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
				#print threshold, result['media']
				partial[threshold] = result												# Adiciona os caclulos feitos num dicionário com indice FILE (ou seja, o threshold usado pelo COPRA)
				if	float(result['media']) > nmi_data[network]['nmi']:
					nmi_data[network] = {'threshold':threshold,'nmi':float(result['media'])}
		else:
			print ("Diretório \""+str(communities)+"\" não encontrado. Continuando...")
	
		dictionary[network] = partial
		print graph_type,nmi_data[network]
	
	return nmi_data
		
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
	print ("Algoritmo para separa singletons. Escolha um conjunto de arquivos para a separação:")
	print
	print("01 - GROUND_TRUTH")
	print("02 - COMMUNITIES BY COPRA")
	print("03 - ")
	print
	op = int(raw_input("Escolha uma opção acima: "))
	if op == 01  

	else:
		algorithm = ""
		print("Opção inválida! Saindo...")
		exit()
	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

if __name__ == "__main__": main()