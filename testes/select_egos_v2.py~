# -*- coding: latin1 -*-
################################################################################################
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 2 - Avalia o conjunto de usuarios coletados e verifica quais atendem aos requisitos de ter pelo menos 02 listas com pelo menos 05 membros em cada.
##								ESSE SCRIPT VERIFICA E COMPLETA OS 50 EGOS
##								
## 							ESSE SCRIPT IGNORA EGOS COM MAIS DE 5 MIL AMIGOS
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
	global i										#controla a quantidade de egos a serem selecionados
	global dictionary
	q = 0											#QTDE total de egos
	l = 0											#QTDE de erros
	
	for file in os.listdir(origem):
		if i < qtde_egos:
			q+=1
			ego = file.split(".dat")
			ego = long(ego[0])
			if not dictionary.has_key(ego):
				try:
					friends_list = read_arq_bin(origem+file)
					if len(friends_list) < 5000:								#Ignora arquivos com mais de 5000
						shutil.copy(origem+file,destino)
						dictionary[ego] = ego									# Insere o usuário coletado na tabela em memória
						i+=1
						print ("Arquivo copiado com sucesso! - Quantidade de amigos: "+str(len(friends_list)))
				except Exception as e:
					print (e)
			else:
				print ("Já copiado!")
			print ("##############################################")
	print
	print ("QTDE de egos verificados: "+str(q))
			
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full' 		#10, 50, 100, 500 ou full
######################################################################################################################
origem = "/home/amaury/coleta_old_02/n1/egos_friends/"+str(qtde_egos)+"/bin/"
destino = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino):
	os.makedirs(destino)	

formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
	
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(destino):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")	
#Executa o método main
if __name__ == "__main__": main()