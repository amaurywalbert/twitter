# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Recebe arquivo com 3572 egos (podados com k=10 do conjunto original), cria uma tabela hash e mapeia um vetor com números aleatórios aos IDs dos egos correspondentes)
##  	Um arquivo JSON com os ids dos egos é gerado e armazenado
##						
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
	i = 0
	with open(arq1, 'r') as file:
		while i < n_egos:																		# Enquanto menor que n_egos
			i+=1 
			id = file.readline()																# Leia o id da lista
			if (id == ''):																		# Se id for igual a vazio é porque chegou ao final do arquivo.
					print ("Final do arquivo!!!")
					break
																									# Ler arquivos com os números aleatórios e armazenar em vetor
			else:
					v1.append(int(id))

	print("Ordenando vetor de tamanho "+str(len(v1))+"...")						# Ordenar o vetor
	v1=sorted(v1)

	print("Localizando egos...")															# Localizar os índices (números aleatórios) e armazenar a lista com os respectivos IDs dos egos
	egos_v1=[]											
	for indice in v1:
#		print indice,egos[indice-1]
		egos_v1.append(egos[indice-1])		


	print("Salvando lista de egos aleatórios em arquivo...")
	with open(random_egos+str(n_egos)+".json", 'w') as f:							# Salvando os IDS dos egos aleatórios em arquivos JSON
		json.dump(egos_v1, f)
		
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

arq1 = "/home/amaury/coleta/subconjunto/random_k_10_3572_egos.txt"				#################### Arquivo com a sequencia de numeros aleatórios 1
egos_threshold = "/home/amaury/coleta/threshold/intersection_k_10.json"			#################### Arquivo com egos q tenham um mínimo de alters... k = 10
random_egos = "/home/amaury/coleta/subconjunto/random_egos/k10/"	 				#################### Saída - Diretório contendo os egos aleatórios podados com k=10
n_egos = 500																						#################### Tamanho do vetor aleatório - egos aleatórios para o subconjunto

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(random_egos):
	os.makedirs(random_egos)


###### Iniciando dicionário - tabela hash a partir de todos os egos

print
print("######################################################################")
print ("Criando tabela hash...")
egos = []																							#################### Lista de todos os egos
with open(egos_threshold, 'r') as f:
	file = json.load(f)	
	for user in file:
		egos.append(user_id)
print ("Lista de egos gerada com sucesso...") 
print("######################################################################\n")
print
print("######################################################################\n")
print
#Executa o método main
if __name__ == "__main__": main()