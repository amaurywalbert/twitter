# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular Jaccard Modificado para avaliar se é possível usar as Listas como ground Truth
##			
##								
## 	Neste script, para cada Lista do usuário ego, comparamo-as com as comunidades detectadas e ao final damos a média para o ego, indicando se o algoritmo de deteção foi capaz de retornar as Listas do ego.
## 	Não é realizado o processo em duas vias, isto é, não é feita a comparação entre as comunidades detectadas e as Listas), pois a intenção é apenas saber se é possível encontrar as Listas nas comunidades...
##		independente se há mais comunidades do ego que não foram catalogadas/organizadas em Listas.
######################################################################################################################################################################

################################################################################################
# Função para calcular o csj entre dois conjuntos de dados
################################################################################################         
def csj(data1,data2):
	a = set(data1)
	b = set(data2)
	intersection = len(a.intersection(b))
	union = len(a.union(b))
# Calcula o CSJ entre os dois conjuntos e atribui 0 caso a união dos conjuntos for 0	
	if union != 0:
		result = intersection/float(union)									# float(uniao) para resultado no intervalo [0,1]
	else:
		result = 0
#	print ("União: "+str(union)+" --- Interseção: "+str(intersection)+" --- CSJ: "+str(result))	
	return result

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

			calculos['soma'] = somar(valores)
			calculos['media'] = media(valores)
			return calculos

######################################################################################################################################################################
#
# Recebe todas as comunidades do ego e calcula o Jaccard Index, retornando um real [0,1] para o ego em questão
#
######################################################################################################################################################################
def jaccard_index(communities, ground_truth_communities):
#	print ("Comunidades detectadas: "+str(len(communities)))
#	print ("Comunidades ground_truth: "+str(len(ground_truth_communities)))
	performance = []														# Armazenar os maiores indices Jaccard para cada comunidade ground_truth	

	for k, v in ground_truth_communities.iteritems():
		bigger = 0 
		y_true = v																	# conjunto de ids do usuarios da comunidade detectada
		for key, values in communities.iteritems():
			y_pred = values														# conjunto de ids do usuarios da comunidade ground_truth
			jaccard = csj(y_pred,y_true)
			if jaccard > bigger:
				bigger = jaccard
		performance.append(bigger)			

	result = calcular(performance)
	
	return result['media']

######################################################################################################################################################################
#
# Formata entrada e envia para calculo do Índice Jaccard
#
######################################################################################################################################################################

def jaccard_prepare_data(communities_file, ground_truth_communities_file):

	with open(communities_file, 'r') as f:
		i=0
		communities = {}
		for line in f:
			i+=1
			key="com"+str(i)																#Chave para o dicionário comm
			comm = []																		#Lista para armazenar as comunidades			
			a = line.split(' ')
			for item in a:
				if item != "\n":
					comm.append(item)
			communities[key] = comm														#dicionário communities recebe a lista de ids das comunidades tendo como chave o valor key
	
	with open(ground_truth_communities_file, 'r') as f:
		i=0
		ground_truth_communities = {}
		for line in f:
			i+=1
			key="com"+str(i)																#Chave para o dicionário comm
			comm = []																		#Lista para armazenar as comunidades			
			a = line.split(' ')
			for item in a:
				if item != "\n":
					comm.append(item)
			ground_truth_communities[key] = comm									#dicionário communities recebe a lista de ids das comunidades tendo como chave o valor key				
					
	jaccard = jaccard_index(communities, ground_truth_communities)
	return jaccard


######################################################################################################################################################################
#
# Prepara apresentação dos resultados - Indice Jaccard
#
######################################################################################################################################################################
def jaccard_alg(communities,output,singletons,net,ground_truth):
	
	communities = communities+singletons+"/"+net+"/"
	ground_truth = ground_truth+singletons+"/"
	output = output+singletons+"/"
	if not os.path.exists(output):
		os.makedirs(output)
	print	
	print("######################################################################")
	print ("Os arquivos serão armazenados em: "+str(output))
	print("######################################################################")
	if os.path.isfile(str(output)+str(net)+".json"):
		print ("Arquivo de destino já existe: "+str(output)+str(net)+".json")
	else:	
		result={}
		for threshold in range(51):	#Parâmetro do algoritmo
			threshold+=1
			i=0 		#Ponteiro para o ego
			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Diretório com as comunidades não encontrado: "+str(communities)+str(threshold))
			else:	
				print("######################################################################")
				score = []																				# Armazenar os indices de cada ego e salvar depois em uma linha para cada threshold do arquivo result.json
				for file in os.listdir(str(communities)+str(threshold)+"/"):
					i+=1
					if not os.path.isfile(str(ground_truth)+str(file)):
						print ("ERROR - EGO: "+str(i)+" - Arquivo de ground truth não encontrado:" +(str(ground_truth)+str(file)))
					else:	
						try:
							jaccard = jaccard_prepare_data(str(communities)+str(threshold)+"/"+str(file),str(ground_truth)+str(file))						
							print ("Jaccard Index para a rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego: "+str(i)+": "+str(jaccard))
							score.append(jaccard)
						except Exception as e:
							print e
																	
				print("######################################################################")
				result[threshold] = score						
		
		if len(result) > 0:
			with open(str(output)+str(net)+".json", 'w') as f:
				f.write(json.dumps(result))
			
	print("######################################################################")			

######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" Algoritmo para cálculo da métrica Jaccard Index Modified											"
	print"																											"
	print"#################################################################################"
	print
	singletons = "full"
#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print 
	print" 01 - COPRA"
	print" 02 - OSLOM"
	print" 03 - GN"
	print" 04 - COPRA -Partition"
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
	if op2 == 01:
		alg = "copra"
	elif op2 == 02:
		alg = "oslom"
	elif op2 == 03:
		alg = "gn"
	elif op2 == 04:
		alg = "copra_partition"		
	else:
		alg = ""
		print("Algoritmo - Opção inválida! Saindo...")
		sys.exit()
	print

	######################################################################################################################
	#####Alterar as linhas para Dropbox quando executado em ambiente de produção
	ground_truth = "/home/amaury/dataset/ground_truth/lists_users_TXT_hashmap/"
	communities1 = "/home/amaury/communities_hashmap/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities_hashmap/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/evaluation_hashmap/with_ground_truth/jaccard_modified/graphs_with_ego/"+str(alg)+"/"
	output2 = "/home/amaury/Dropbox/evaluation_hashmap/with_ground_truth/jaccard_modified/graphs_without_ego/"+str(alg)+"/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		net = "n"+str(i)
		print
		print ("Calculando Jaccard Modified nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))
		jaccard_alg(communities1,output1,singletons,net,ground_truth)
		print
		print ("Calculando Jaccard Modified nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
		jaccard_alg(communities2,output2,singletons,net,ground_truth)
	print("######################################################################")
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
if __name__ == "__main__": main()