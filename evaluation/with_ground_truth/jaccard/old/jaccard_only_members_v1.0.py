# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular Jaccard Index
##								
## # INPUT: Arquivos com as comunidades detectadas e o ground truth 
## # OUTPUT:
##		- Arquivos com os índices Jaccard
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
	performance_pred = []														# Armazenar os maiores indices Jaccard para cada comunidade detectada
	performance_true = []														# Armazenar os maiores indices Jaccard para cada comunidade ground_truth	
	performance = []																# Armazenar a média  dos maiores indices Jaccard das comunidades detectadas e do ground truth

#	print ("detectadas")			
	for key, values in communities.iteritems():
		bigger = 0 
		y_pred = values															# conjunto de ids do usuarios da comunidade detectada
		for k, v in ground_truth_communities.iteritems():
			y_true = v																# conjunto de ids do usuarios da comunidade ground_truth
			jaccard = csj(y_true, y_pred)
#			print jaccard
			if jaccard > bigger:
				bigger = jaccard
#		print bigger
#		print
		performance_pred.append(bigger)		

#	######################################################################################################################
#	print ("ground_truth")				
	for k, v in ground_truth_communities.iteritems():
		bigger = 0 
		y_true = v																	# conjunto de ids do usuarios da comunidade detectada
		for key, values in communities.iteritems():
			y_pred = values														# conjunto de ids do usuarios da comunidade ground_truth
			jaccard = csj(y_pred,y_true)
#			print jaccard
			if jaccard > bigger:
				bigger = jaccard		
#		print bigger
#		print		
		performance_true.append(bigger)					
				
	######################################################################################################################			
	result_pred = calcular(performance_pred)
	result_true = calcular(performance_true)
#	print performance_pred
#	print performance_true

#	print result_pred
#	print result_true
		
#	time.sleep(20)
	performance.append(result_pred['media'])
	performance.append(result_true['media'])

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
	if not os.path.isfile(str(output)+str(net)+".json"):
		result={}
		for threshold in range(51):	#Parâmetro do algoritmo - todos até agora rodam no máximo até 20 parâmetros diferentes
			threshold+=1
			i=0 		#Ponteiro para o ego
			if os.path.isdir(str(communities)+str(threshold)+"/"):
				print("######################################################################")
				score = []																				# Armazenar os indices de cada ego e salvar depois em uma linha para cada threshold do arquivo result.json
				for file in os.listdir(str(communities)+str(threshold)+"/"):
					i+=1
					if os.path.isfile(str(ground_truth)+str(file)):
						try:
							jaccard = jaccard_prepare_data(str(communities)+str(threshold)+"/"+str(file),str(ground_truth)+str(file))						
							print ("Jaccard Index para a rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego: "+str(i)+": "+str(jaccard))
							score.append(jaccard)
						except Exception as e:
							print e
					else:
						print ("ERROR - EGO: "+str(i)+" - Arquivo de ground truth não encontrado:" +(str(ground_truth)+str(file)))
												
				print("######################################################################")
				result[threshold] = score						
			else:
				print ("Diretório com as comunidades não encontrado: "+str(communities)+str(threshold))
		if len(result) > 0:
			with open(str(output)+str(net)+".json", 'w') as f:
				f.write(json.dumps(result))						
	else:
		print ("Arquivo de destino já existe: "+str(output)+str(net)+".json")			
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
	print" Algoritmo para cálculo da métrica Jaccard Index 											"
	print"																											"
	print"#################################################################################"
	print
	print"Realizar o cálculo usando Singletons?"
	print 
	print" 01 - SIM - full"
	print" 02 - NÃO"
	print
	op = int(raw_input("Escolha uma opção acima: "))
	if op == 01:
		singletons = "full"
	elif op == 02:
		singletons = "without_singletons"
	else:
		singletons = ""
		print("Singletons - Opção inválida! Saindo...")
		sys.exit()	
#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print 
	print" 01 - COPRA"
	print" 02 - OSLOM"
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
	if op2 == 01:
		alg = "copra"
	elif op2 == 02:
		alg = "oslom"
	else:
		alg = ""
		print("Algoritmo - Opção inválida! Saindo...")
		sys.exit()
	print
	print
	print ("Opção escolhida: "+str(singletons)+" - "+str(alg))
	print ("Aguarde...")
	time.sleep(5)

	######################################################################################################################
	#####Alterar as linhas para Dropbox quando executado em ambiente de produção
	ground_truth = "/home/amaury/dataset/ground_truth_only_members/lists_users_TXT/"
	communities1 = "/home/amaury/communities/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/evaluation_only_members/graphs_with_ego/"+str(alg)+"/jaccard/"
	output2 = "/home/amaury/Dropbox/evaluation_only_members/graphs_without_ego/"+str(alg)+"/jaccard/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		net = "n"+str(i)
		print
		print ("Calculando Jaccard Index nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))
		jaccard_alg(communities1,output1,singletons,net,ground_truth)
		print
		print ("Calculando Jaccard Index nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
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