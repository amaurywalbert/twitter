# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import networkx as nx

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Criar rede N1 (follow) a partir dos dados coletados e de acordo com as instruções a seguir:
##								
## # INPUT:
##		- Lista de Egos (egos)
##		- Lista Followee (alters) de cada Ego - Formação do conjunto de Alters
##		- Lista Followee (followees) de cada Alter (ids)
##
## # ALGORITMO
##					0 - Para cada ego[i]:
##					1 - 	Inicializa o ego_[i] e todos os seus amigos (alters[i][n]) como vértices de um grafo - (tabela hash - ego+alters - vertices)
##					2 - 	Cria uma aresta direcionada entre o ego[i] e todos os alters (alter[i][n])
##					3 - 	Para cada elemento no conjunto no conjunto de alters (alter[i][j]):
##					4 - 		Para cada elemento no conjunto de amigos do alter (followee[i][j][k]):
##					5 - 			Se alter[i][j] está no conjunto de vértices (tabela hash - ego+alters):
##					6 - 				Se não existe uma aresta direcionada entre alter[i][j] e followee[i][j][k]:
##					7 - 					Cria uma aresta direcionada entre alter[i][j] e followee[i][j][k]
##					8 - 				Senão:
##					9 -					Adiciona peso na aresta.
##
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

################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,alters,l):
	global errors
	G=nx.DiGraph()									# Inicia um grafo DIRECIONADO
	vertices = {}									# Inicia tabela hash - Conjunto de vértices - EGO + ALTERS
	m = 0 											# Conjunto de vértices
	te_i = datetime.datetime.now()
	vertices[ego] = ego							# Adiciona o Ego ao conjunto de vértices
	m+=1											
	for alter in alters_id:
		alter = long(alter)
		vertices[alter] = alter					# Adiciona cada Alter ao conjunto de vértices				
		G.add_edge(ego,alter,weight=1)		# Cria uma aresta entre o Ego e cada Alter com peso 1
		m+=1
	
	try:
		for alter in alters_id:
			followees = read_arq_bin(alters_dir+str(alter)+".dat")	# Recebe lista de amigos de cada alter
			if followees:
				for friend in followees:
					friend = long(friend)
					if dictionary.has_key(friend):							# Se amigo está na lista de alters
						if G.has_edge(alter,friend):							### Se existe uma aresta entre o alter e o amigo
							G[alter][friend]['weight']=+=1					##### Adiciona peso na aresta 
						else:															# Senão
							G.add_edge(alter,friend,weight=1)				# Cria aresta com peso 1

	except IOError as a:
		with open(output_dir_errors_alters+str(alter)+".json", 'a+') as outfile:
			if e.message:		
				error = {'ego':ego_id,'alter':alter,'reason': e.message}
			else:
				error = {'ego':ego_id,'alter':alter,'reason': str(e)}
			outfile.write(json.dumps(error)+"\n") 
			print ("ERROR: "+str(error))
			errors +=1
		
	te_f =  datetime.datetime.now()
	te	= te_f - te_i
	print ("Lista de arestas da grafo "+str(k)+" construído com sucesso. EGO: "+str(ego))
	print("Tempo para construir o grafo: "+str(te))
				
	return G
			
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	errors = 0
	l = 0															#Exibe o número ordinal do ego que está sendo usado para a coleta dos amigos dos alters
	tt_i =  datetime.datetime.now()
	for file in os.listdir(egos_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		l+=1
		ego = file.split(".dat")
		ego = long(ego[0])
		alters = read_arq_bin(egos_dir+file)
		if alters:
			print("######################################################################")
			print ("Construindo grafo do ego n: "+str(l))
			print alters			
			#G = ego_net(ego,alters, l)								#Inicia função de geração do grafo
			#print("Quantidade de usuários faltando: "+str(errors))
			print("######################################################################")
			print
		else:
			print ("ERROR - Impossível obter lista de alters para o ego: "+str(ego))
			errors +=1
	tt_f =  datetime.datetime.now()
	tt	= tt_f - tt_i
	print("Tempo total do script: "+str(tt))
	print("Quantidade total de usuários faltando: "+str(errors))
	print("######################################################################")
	print("Networks created!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
qtde_egos = 50 # 50, 100, 500, full
######################################################################################################################
######################################################################################################################
egos_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"######### Arquivo contendo a lista dos usuários ego já coletados
alters_dir = "/home/amaury/coleta/n1/alters_friends/"+str(qtde_egos)+"/bin/" #### Diretório para armazenamento dos arquivos
output_dir = "/home/amaury/redes/n1/"+str(qtde_egos)+"/graphs/" ################# Diretório para armazenamento dos arquivos das listas de arestas 
output_dir_errors_alters = "/home/amaury/redes/n1/"+str(qtde_egos)+"/errors/alters" # Diretório para armazenamento dos erros dos alters
formato = 'l'				######################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ############################################ Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_dir):
	os.makedirs(outup_dir)
if not os.path.exists(output_dir_errors_egos):
	os.makedirs(outup_dir_errors_egos)
if not os.path.exists(output_dir_errors_alters):
	os.makedirs(outup_dir_errors_alters)

#Executa o método main
if __name__ == "__main__": main()