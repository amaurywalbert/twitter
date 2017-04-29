# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - verifica se os alters (amigos dos egos) já foram coletados e copia os arquivos deles para o diretório correto
##									Esse processo é apenas para agilizar e organizar os diretórios de favoritos já coletados.
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
	j = 0		# Quantidade de arquivos copiados 
	k = 0		# Quantidade de arquivos não encontrados

	for file in os.listdir(fonte):
		friends_list = read_arq_bin(fonte+file) # Função para converter o binário de volta em string em formato json.
		if friends_list:
			for friend in friends_list:				
				user = long(friend)
				if not dictionary.has_key(user):
					if os.path.isfile(origem1+str(user)+".dat"):
						shutil.copy(origem1+str(user)+".dat",destino)
						dictionary[user] = user
						j+=1
						print (str(j)+" - Arquivo copiado com sucesso!")
					elif os.path.isfile(origem2+str(user)+".dat"):
						shutil.copy(origem2+str(user)+".dat",destino)
						dictionary[user] = user
						j+=1
						print (str(j)+" - Arquivo copiado com sucesso!")
					elif os.path.isfile(origem3+str(user)+".dat"):
						shutil.copy(origem3+str(user)+".dat",destino)
						dictionary[user] = user
						j+=1
						print (str(j)+" - Arquivo copiado com sucesso!")
					elif os.path.isfile(origem4+str(user)+".dat"):
						shutil.copy(origem4+str(user)+".dat",destino)
						dictionary[user] = user
						j+=1
						print (str(j)+" - Arquivo copiado com sucesso!")						
					else:
						k+=1
						
	print ("Arquivos copiados: "+str(j))
	print ("Arquivos no diretório: "+str(len(dictionary)))
	print ("Arquivos faltando: "+str(k))
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
qtde_egos = 100 		#10, 50, 100, 500 ou full
######################################################################################################################
fonte = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"

origem4 = "/home/amaury/coleta_old_01/n1/egos_and_alters_friends/bin/"
origem3 = "/home/amaury/coleta_old_01/n1/alters_friends/50/bin/"
origem2 = "/home/amaury/coleta_old_02/n1/alters_friends/50/bin/"
origem1 = "/home/amaury/coleta_old_02/n1/alters_friends/10/bin/"


destino = "/home/amaury/coleta/n1/alters_friends/"+str(qtde_egos)+"/bin/"


formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário


#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino):
	os.makedirs(destino)

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