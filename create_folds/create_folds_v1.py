# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Recebe três vetores aleatórios e identifica os egos correspondentes, criando um arquivo para cada FOLD.
## 
######################################################################################################################################################################

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	v1=[]
	v2=[]
	v3=[]

															# Ler arquivos com os números aleatórios e armazenar em um vetor
	with open(arq1, 'r') as f1:
		for line in range(n):
			v1.append(int(f1.readline()))

	with open(arq2, 'r') as f2:
		for line in range(n):
			v2.append(int(f2.readline()))	
	
	with open(arq3, 'r') as f3:
		for line in range(n):
			v3.append(int(f3.readline()))
																# Ordenar os vetores
	v1=sorted(v1)
	v2=sorted(v2)
	v3=sorted(v3)

	egos_v1=[]
	egos_v2=[]
	egos_v3=[]
																# Localizar os índices (números aleatórios) e armazenar a lista com os respectivos IDs dos egos
															
	for indice in v1:
		egos_v1.append(egos[indice])													
	for indice in v2:
		egos_v2.append(egos[indice])
	for indice in v3:
		egos_v3.append(egos[indice])			

																# Salvando os IDS dos egos aleatórios em arquivos JSON
	with open(folds+"egos_fold1.json", 'w') as f:
		json.dump(egos_v1, f)
	with open(folds+"egos_fold2.json", 'w') as f:
		json.dump(egos_v2, f)
	with open(folds+"egos_fold3.json", 'w') as f:
		json.dump(egos_v3, f)

	A = set(egos_v1)
	B = set(egos_v2)
	C = set(egos_v3)
	
	egos_set = A.union(B, C)
	print ("Quantidade de egos distintos: "+str(len(egos_set)))

		
######################################################################################################################################################################
######################################################################################################################################################################			
	
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")


#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
data_dir_n1 = "/home/amaury/coleta/n1/egos_friends/full_with_prunned/bin/" 	#################### Diretório contendo todos os egos da rede n1
data_dir_n2 = "/home/amaury/coleta/n2/egos/full_with_prunned/bin/" 				#################### Diretório contendo todos os egos da rede n2
data_dir_n3 = "/home/amaury/coleta/n3/egos/full_with_prunned/bin/" 				#################### Diretório contendo todos os egos da rede n3
data_dir_n4 = "/home/amaury/coleta/n4/egos/full_with_prunned/bin/" 				#################### Diretório contendo todos os egos da rede n4
data_dir_n9 = "/home/amaury/coleta/n9/egos_followers/full_with_prunned/bin/" 	#################### Diretório contendo todos os egos da rede n9

arq1 = "/home/amaury/twitter/create_folds/random1.txt"								#################### Arquivo com a sequencia de numeros aleatórios 1
arq2 = "/home/amaury/twitter/create_folds/random2.txt"								#################### Arquivo com a sequencia de numeros aleatórios 2
arq3 = "/home/amaury/twitter/create_folds/random3.txt"								#################### Arquivo com a sequencia de numeros aleatórios 3

egos = []																							#################### Lista de todos os egos
n = 175																								#################### Número de elementos em cada fold

folds = "/home/amaury/twitter/create_folds/"					 							#################### Diretório contendo a lista com os membros de cada fold


#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino_n1):
	os.makedirs(destino_n1)
if not os.path.exists(destino_n2):
	os.makedirs(destino_n2)
if not os.path.exists(destino_n3):
	os.makedirs(destino_n3)
if not os.path.exists(destino_n4):
	os.makedirs(destino_n4)	
if not os.path.exists(destino_n9):
	os.makedirs(destino_n9)

###### Iniciando dicionário - tabela hash a partir de todos os egos

print
print("######################################################################")
print ("Criando tabela hash...")
for file in os.listdir(data_dir_n1):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	egos.append(user_id)
print ("Lista de egos gerada com sucesso...") 
print("######################################################################\n")
print
print("######################################################################\n")
print ("Usando FOLDS de tamanho: "+str(n))
print("######################################################################\n")
print
#Executa o método main
if __name__ == "__main__": main()