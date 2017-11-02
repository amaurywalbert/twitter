# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##
##		26-10-2017 - Separar egos com mais de 3.5k alters para geração paralela das redes N5 e N10
##
##						
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin_alters(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		alters_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			alter = user_struct.unpack(buffer)
			alters_file.append(alter[0])
	return alters_file

################################################################################################
# Copia arquivo da origem para o destino...
################################################################################################
def copy(file,origem,destino):
	shutil.copy(origem+file,destino)


################################################################################################
# Faz a seleção separando os conjuntos...
################################################################################################
def execute(data_dir,sub_3k_dir,sub_5k_dir):
	_3k = 0
	_5k = 0
	t = 0
	for file in os.listdir(data_dir):
		t+=1
		alters_list = read_arq_bin_alters(data_dir+file) 			#Verificando número de alters
#################################################################################### Testando número de AMIGOS			
		if len(alters_list) <= 3500:
			copy(file,data_dir,sub_3k_dir)				## Se menor ou igual que 3k, copia arquivo com amigos para o novo diretório
			_3k+=1
		else:
			copy(file,data_dir,sub_5k_dir)				## Se menor ou igual que 3k, copia arquivo com amigos para o novo diretório
			_5k+=1

	print ("Usuários com até 3k alters: "+str(_3k))
	print ("Usuários com mais de 3k alters: "+str(_5k))
	print ("Total de usuários no diretório: "+str(t))
		
		

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():

	execute(data_dir_n1,sub_3k_dir_n1,sub_5k_dir_n1)
	execute(data_dir_n9,sub_3k_dir_n9,sub_5k_dir_n9)
					
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

data_dir_n1 = "/home/amaury/dataset/n1/egos_limited_5k/bin/" 					#################### Diretório contendo 500 egos aleatórios da rede n1

sub_3k_dir_n1 = "/home/amaury/dataset/n1/egos_3k_alters/bin/"
sub_5k_dir_n1 = "/home/amaury/dataset/n1/egos_3k_a_5k_alters/bin/"


data_dir_n9 = "/home/amaury/dataset/n9/egos_limited_5k/bin/" 					#################### Diretório contendo 500 egos aleatórios da rede n9

sub_3k_dir_n9 = "/home/amaury/dataset/n9/egos_3k_alters/bin/"
sub_5k_dir_n9 = "/home/amaury/dataset/n9/egos_3k_a_5k_alters/bin/"

formato = 'l'				####################################################### Long para o código ('l') - id dos amigos de cada user
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(sub_3k_dir_n1):
	os.makedirs(sub_3k_dir_n1)

if not os.path.exists(sub_5k_dir_n1):
	os.makedirs(sub_5k_dir_n1)			

if not os.path.exists(sub_3k_dir_n9):
	os.makedirs(sub_3k_dir_n9)

if not os.path.exists(sub_5k_dir_n9):
	os.makedirs(sub_5k_dir_n9)	
	
#Executa o método main
if __name__ == "__main__": main()