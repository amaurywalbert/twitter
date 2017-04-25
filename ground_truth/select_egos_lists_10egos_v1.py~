# -*- coding: latin1 -*-
################################################################################################
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - A partir do conjunto de egos, cria arquivos Binários contendo ids das listas de propriedade ou inscrição dos egos para uso de Ground Truth
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
		lists_file = []
		while f.tell() < tamanho:
			buffer = f.read(list_struct.size)
			lists = list_struct.unpack(buffer)
			lists_file.append(follower[0])
	return lists_file

######################################################################################################################################################################
#
# Obtem as listas já coletadas do ego
#
######################################################################################################################################################################
def get_lists(ego):
	egos_lists_ownership = []
	egos_lists_subscription = []
	eof = False
	with open(lists_set, 'r') as lists_file:
		for line in lists_file:
			lists = json.loads(line)
			if ego == long(lists['user']):
				print "Ego encontrado! Localizando listas..."
				for list in lists['owner']:
					egos_lists_ownership.append(list['id'])
				for list in lists['subscriptions']:
					egos_lists_subscription.append(list['id'])
				eof = True				
	return egos_lists_ownership,egos_lists_subscription
	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i										#controla a quantidade de egos a serrem selecionados
	global dictionary
	q = 0											#QTDE total de egos
	l = 0											#QTDE de erros
	
	for file in os.listdir(egos_set):
		q+=1 
		ego = file.split(".dat")
		ego = long(ego[0])
		if not dictionary.has_key(ego):

			egos_lists_ownership,egos_lists_subscription = get_lists(ego)

			print ("Ego nº "+str(i)+": "+str(ego)+" - Lists Ownership: "+str(len(egos_lists_ownership)))
			print ("Ego nº "+str(i)+": "+str(ego)+" - Lists Subscription: "+str(len(egos_lists_subscription)))

			try:			
				with open(all_egos_lists+str(ego)+".dat", 'a+b') as a:
					with open(owner_egos_lists+str(ego)+".dat", 'w+b') as f:			
						if egos_lists_ownership:
							for list in egos_lists_ownership:
								if os.path.isfile(lists_collected+str(list)+".dat"):
									a.write(list_struct.pack(list))	#Grava o id da lista no arquivo do ego que contem TODAS AS LISTAS.								
									f.write(list_struct.pack(list))	#Grava o id da lista no arquivo do ego que contem as listas que ele é o dono. 
			
				with open(all_egos_lists+str(ego)+".dat", 'a+b') as a:
					with open(subs_egos_lists+str(ego)+".dat", 'w+b') as g:			
						if egos_lists_subscription:
							for list in egos_lists_subscription:
								if os.path.isfile(lists_collected+str(list)+".dat"):
									a.write(list_struct.pack(list))
									g.write(list_struct.pack(list))
				dictionary[ego] = ego
				i+=1							
			except Exception as e:
				print e

	print ("##############################################")
	print ("QTDE de egos verificados: "+str(q))
	print ("QTDE de arquivos em cada diretório: "+str(i))
			
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
egos_set = "/home/amaury/coleta/n1/egos_friends/50/bin/" # Conjunto de egos - Apenas para pegar o id de cada ego em cada conjunto (50-100-500-full)

lists_set = "/home/amaury/coleta/users_lists/data/ego_lists_overview_full.json" # Diretório que contém o conjunto de listas de cada ego. 
lists_collected = "/home/amaury/coleta/ground_truth/members_lists_collected/bin/" # Diretório que contém o conjunto de listas COLETADAS de cada ego. Só pra pegar o id das listas 

all_egos_lists = "/home/amaury/coleta/ground_truth/egos_lists/50/all/bin/" 
owner_egos_lists ="/home/amaury/coleta/ground_truth/egos_lists/50/owner/bin/"
subs_egos_lists ="/home/amaury/coleta/ground_truth/egos_lists/50/subs/bin/"

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(all_egos_lists):
	os.makedirs(all_egos_lists)
if not os.path.exists(owner_egos_lists):
	os.makedirs(owner_egos_lists)
if not os.path.exists(subs_egos_lists):
	os.makedirs(subs_egos_lists)	
	
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(all_egos_lists):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")	

#Executa o método main
if __name__ == "__main__": main()