# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth_n7
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Podar egos com mais de 5mil seguidores
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
		followers_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			follower = user_struct.unpack(buffer)
			followers_file.append(follower[0])
	return followers_file

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	k = 0																	#Exibe o número ordinal do ego que está sendo usado para a coleta dos seguidores
	for file in os.listdir(data_dir):							# Verifica a lista de egos coletados e para cada um, busca os seguidores dos egos.
		k+=1 
		followers_file = read_arq_bin(data_dir+file)
		if len(followers_file) > 5000:
			shutil.move(data_dir+file,acima_5000_dir)
			print ("Podado!"+str(len(followers_file)))
		else:
			pass
	
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

qtde_egos = 'full' #10,50,100,500,full

acima_5000_dir = "/home/amaury/coleta/n9/egos_followers/acima5000/"+str(qtde_egos)+"/bin/" ## Diretório para armazenamento dos arquivos
data_dir = "/home/amaury/coleta/n9/egos_followers/"+str(qtde_egos)+"/bin/" ## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n9/egos_followers/"+str(qtde_egos)+"/error/" # Diretório para armazenamento dos arquivos de erro

formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(acima_5000_dir):
	os.makedirs(acima_5000_dir)
	
#Executa o método main
if __name__ == "__main__": main()