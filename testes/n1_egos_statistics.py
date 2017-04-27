# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Exibe estatísticas do ego.
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
		friends_list = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_list.append(friend[0])
	return friends_list

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	dictionary={}
	for file in os.listdir(fonte):
		friends_list = read_arq_bin(fonte+file) # Função para converter o binário de volta em string em formato json.
		if friends_list:
			user_id = file.split(".dat")
			user_id = long(user_id[0])
			dictionary[user_id] = len(friends_list)
	print dictionary

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
qtde_egos = 10 		#10, 50, 100, 500 ou full
######################################################################################################################
data_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"
output_dir =  "/home/amaury/statistics/n1/"
formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
for file in os.listdir(destino):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")

#Executa o método main
if __name__ == "__main__": main()