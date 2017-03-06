# -*- coding: latin1 -*-
################################################################################################
# Script para gerar grafos a partir dos arquivos coletados de cada ego e cada alter
#	Não precisa verificar e nem inserir nós... a biblioteca networkx já faz isso automaticamente.
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct
import networkx as nx
import matplotlib.pyplot as plt	

reload(sys)
sys.setdefaultencoding('utf-8')

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(f):
	f.seek(0,2)
	tamanho = f.tell()
	f.seek(0)
	friends_file = {}
	while f.tell() < tamanho:
		buffer = f.read(user_data.size)
		user, friends = user_data.unpack(buffer)
		friends = friends.split("\0")[0] # Como o C utiliza o \0 para terminar uma string no python precisamos tratar isso
		friends_file[user] = friends
	return friends_file


################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,k):
	G=nx.DiGraph()
	errors = 0
	try:
		te_i = datetime.datetime.now()

		with open(dir_data+str(ego)+".dat",'r') as ego_file:
			ego_friends = read_arq_bin(ego_file)

		for alter in ego_friends:
			alter = long(alter)
			G.add_edge(ego,alter)

			try:
				with open(dir_data+str(alter)+".dat",'r') as alter_file:
					alter_friends = read_arq_bin(alter_file)

				for friend in alter_friends:
					friend = long(friend) 
					G.add_edge(alter,friend)						

			except IOError as a:
				with open(dir_error+str(alter)+".json", 'a+') as outfile:
					if e.message:		
						error = {'alter':alter,'reason': e.message}
					else:
						error = {'alter':alter,'reason': str(e)}
					outfile.write(json.dumps(error)+"\n") 
				print error
				errors +=1

		print
		nx.draw(G)
#		plt.savefig(output_dir+str(ego)+".png")
#		plt.show()

#		print ("Exportando arquivo GEXF...")
#		nx.write_gexf(G, output_dir+str(ego)+".gexf")		
		
		print ("Gráfico da rede "+str(k)+" construído com sucesso. EGO: "+str(ego))
		
		te_f =  datetime.datetime.now()
		te	= te_f - te_i
		print("Tempo para construir o grafo do ego n "+str(k)+": "+str(te))
				
	except IOError as e:
		with open(dir_error+str(ego)+".json", 'a+') as outfile:
			if e.message:		
				error = {'ego':ego,'reason': e.message}
			else:
				error = {'ego':ego,'reason': str(e)}
			outfile.write(json.dumps(error)+"\n") 
		print error
	
	return G,errors
			
################################################################################################
# Método Principal do Script
################################################################################################
def main():
	tt_i =  datetime.datetime.now()
	errors_t = 0
	with open(users_list_file,'r') as users_list:		#Percorre o arquivo de usuários já verificados
		for k in range(0,ego_limit):
			user = users_list.readline()						#Leia id do usuário corrente
			print("######################################################################")
			print ("Construindo grafo do ego n: "+str(k))			
			G, errors = ego_net(long(user), k)								#Inicia função de geração do grafo
			print("Quantidade de usuários faltando: "+str(errors))
			print("######################################################################")
			print
			errors_t += errors
	tt_f =  datetime.datetime.now()
	tt	= tt_f - tt_i
	print("Tempo total do script: "+str(tt))
	print("Quantidade total de usuários faltando: "+str(errors_t))				
	print("Script finalizado!")

################################################################################################
#
# INÍCIO DO PROGRAMA
#
################################################################################################

################################ CONFIGURAR AS LINHAS A SEGUIR #################################
################################################################################################
output_dir = "/home/amaury/coleta/n1/egos/bin/graphs/" #################### Diretório para armazenamento das imagens das redes ego 
dir_data = "/home/amaury/coleta/n1/egos/bin/" #################### Diretório para armazenamento dos arquivos
dir_error = "/home/amaury/coleta/n1/egos/bin/graphs/error/" ############# Diretório para armazenamento dos arquivos de erro
users_list_file = "/home/amaury/coleta//n1/egos/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados
ego_limit = 10					####################################### Controla a quantidade de egos a serem pesquisados
formato = 'l150s'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
user_data = struct.Struct(formato) ############################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
################################################################################################
################################################################################################
#Cria os diretórios para armazenamento das redes ego (grafos)
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
if not os.path.exists(dir_error):
	os.makedirs(dir_error)

#Executa o método main
if __name__ == "__main__": main()	