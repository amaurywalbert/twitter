# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##	2017-08-06
##		Status - Versão 1 - Faz leitura do binário e salva apenas o ID DOS AMIGOS em formato JSON.
##								Cria um ÙNICO ARQUIVO com todos os alters...
##								ARQUIVOS GERADOS PARA SEREM USADOS NO mytweetf0rm
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
		friends_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_file.append(friend[0])
	return friends_file

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	i = 0		# egos convertidos
	print ("Convertendo egos:")
	alters_set = set()

	for file in os.listdir(fonte):
		i+=1
		friends_list = read_arq_bin(fonte+file)
		ego = file.split(".dat")
		ego = long(ego[0])
		if friends_list:
			print i
			for user in friends_list:
				alters_set.add(user)

	alters_list = list(alters_set)	

	with open(output, 'w') as f:
		json.dump(alters_list, f)


#Teste de impressão dos alters para verificar integridade da conversão.
	with open(output, 'r') as f:	
		alters = json.load(f)
	for alter in alters:
		print alter			
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
fonte = "/home/amaury/dataset/n1/egos_limited_5k/bin/"
output = "/home/amaury/dataset/n1/egos_limited_5k/n1_500_egos_friends_alters_ids.json"

formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Executa o método main
if __name__ == "__main__": main()