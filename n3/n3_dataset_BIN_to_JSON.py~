# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##	2017-07-31
##		Status - Versão 1 - Faz leitura do binário, separa o id do tweet do id do autor e salva apenas o ID DO AUTOR em formato JSON
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		authors_list = []
		while f.tell() < tamanho:
			buffer = f.read(favorites_struct.size)
			tweet, user = favorites_struct.unpack(buffer)
			authors_list.append(user)
	return authors_list

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	j = 0		# Quantidade de arquivos copiados 
	k = 0		# Quantidade de arquivos não encontrados

	for file in os.listdir(fonte):
		authors_list = read_arq_bin(fonte+file) # Função para converter o binário de volta em string em formato json.
		ego = file.split(".dat")
		ego = long(user_id[0])
		if authors_list:
			with open(output+str(ego)+".json", 'w') as f:
				json.dump(authors_list, f)
				
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
fonte = "/home/amaury/dataset/n3/egos/bin/"
output = "/home/amaury/dataset/n3/egos/json/"

formato = 'll'				####################################################### Long para id do tweet e outro long para autor
favorites_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()