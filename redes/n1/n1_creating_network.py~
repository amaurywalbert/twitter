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
##					3 - 	Para cada elemento no conjunto de alters (alter[i][j]):
##					4 - 		Para cada elemento no conjunto de amigos do alter (followee[i][j][k]):
##					5 - 			Se followee[i][j][k] está no conjunto de vértices (tabela hash - ego+alters):
##					6 - 				Se não existe uma aresta direcionada entre alter[i][j] e followee[i][j][k]:
##					7 - 					Cria uma aresta direcionada entre alter[i][j] e followee[i][j][k]
##					8 -#####			Senão:								##### Nessa rede não há peso nas arestas
##					9 -#####				Adiciona peso na aresta.	##### Nessa rede não há peso nas arestas
##
## 
######################################################################################################################################################################

################################################################################################
# Função para converter os arquivos binários em formato específico para ser usado na construção do grafo
#  - Aqui há o retorno da lista de amigos de um alter (alter = amigo do ego)
################################################################################################
def read_arq_bin(file):															# Função recebe o arquivo binário
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
#
# Converte formato data para armazenar em formato JSON
#
######################################################################################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object
        
################################################################################################
# Função para salvar os grafos em formato padrão para entrada nos algoritmos de detecção 
################################################################################################
def save_graph(ego, G):															# Função recebe o id do ego corrente e o grafo (lista de arestas)
	print
	print("Salvando o grafo...")

################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,alters_list,l):												# Função recebe o id do ego, a lista de alters e o número ordinal do ego corrente
	print ("Construindo grafo do ego n: "+str(l)+"/"+str(qtde_egos))
	ep = 0																			# Variável para armazenar os erros parciais - arquivos faltando referentes ao conjunto alters
	G=nx.DiGraph()																	# Inicia um grafo DIRECIONADO
	vertices = {}																	# Inicia tabela hash - Conjunto de vértices - EGO + ALTERS
	out=[]																			# Lista de usuários faltando
	ti = datetime.datetime.now()												# Tempo do inicio da construção do grafo 
	vertices[ego] = ego															# Adiciona o Ego ao conjunto de vértices
	for alter in alters_list:
		alter = long(alter)
		vertices[alter] = alter													# Adiciona cada Alter ao conjunto de vértices				
##		G.add_edge(ego,alter)													# Cria uma aresta entre o Ego e cada Alter - Adiciona alter com arquivo em branco
	
	for alter in alters_list:	
		try:
			friends = read_arq_bin(alters_dir+str(alter)+".dat")		# Recebe lista de amigos de cada alter
			if friends:
				G.add_edge(ego,alter)											# Cria uma aresta entre o Ego e cada Alter - NÃO Adiciona alter com arquivo em branco
				for friend in friends:											# Para cada amigo
					friend = long(friend)
					if vertices.has_key(friend):								# Se amigo está na lista de alters
						G.add_edge(alter,friend)								### Cria aresta

################################################################################################
######## Para os outros scripts - grafos ponderados
#						if G.has_edge(alter,friend):							### Se existe uma aresta entre o alter e o amigo
#							G[alter][friend]['weight']=+=1					##### Adiciona peso na aresta - Nesta rede não há adição de peso nas arestas... 
#						else:															# Senão
#							G.add_edge(alter,friend,weight=1)				# Cria aresta com peso 1
################################################################################################

		except IOError as e:															# Tratamento de exceção - caso falte algum arquivo de um amigo do alter, 
			ep +=1																		# Incrementa os erros parciais (do ego corrente)
			out.append(alter)															# Adiciona alter à lista com usuários faltando		
#			print ("ERROR: "+str(e))
		
	tf =  datetime.datetime.now()												# Tempo final da construção do grafo do ego corrente
	tp	= tf - ti																	# Cálculo do tempo gasto para a construção do grafo
	print ("Lista de arestas do grafo "+str(l)+" construído com sucesso. EGO: "+str(ego))
	print("Tempo para construir o grafo: "+str(tp))
				
	return G,ep,out																	# Função retorna o grafo, o número de erros parciais e o tempo gasto para a construção do grafo
			
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	errors = 0																		# Variável para armazenar o total de erros (arquivos faltando)	
	l = 0																				# Variável para exibir o número ordinal do ego que está sendo usado para a construção do grafo
	ti =  datetime.datetime.now()												# Tempo de início do processo de criação de todos os grafos
	with open(output_overview+"overview.json", 'w') as f:
		for file in os.listdir(egos_dir):									# Para cada arquivo de Ego no diretório
			l+=1																		# Incrementa contador do número do Ego
			ego = file.split(".dat")											# Separa a extensão do id do usuário no nome do arquivo
			ego = long(ego[0])													# recebe o id do usuário em formato Long
			alters_list = read_arq_bin(egos_dir+file)						# Chama função para converter o conjunto de amigos do ego do formato Binário para uma lista do python
			friends = len(alters_list)											# Variável que armazena o tamanho da lista do usuário corrente
			print("######################################################################")
			G, ep, out = ego_net(ego,alters_list, l)						# Inicia função de criação do grafo (lista de arestas) para o ego corrente
			print("Quantidade de usuários faltando: "+str(ep))
			save_graph(ego,G)
			print("######################################################################")
			print
			errors+=ep																			# Incrementa erros totais com erros parciais recebidos da criação do grafo do ego corrente
			overview = {'ego':ego,'friends':friends,'errors':ep,'out':out}		# cria dicionário python com informações sobre a criação do grafo do ego corrente
			f.write(json.dumps(overview)+"\n") 											# Escreve o dicionário python em formato JSON no arquivo overview
		tf =  datetime.datetime.now()														# Recebe tempo final do processo de construção dos grafos
		t = tf - ti																				# Calcula o tempo gasto com o processo de criação dos grafos
	print("Tempo total do script: "+str(t))
	print("Quantidade total de usuários faltando: "+str(errors))
	print("######################################################################")
	print("Networks created!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
qtde_egos = 10 # 50, 100, 500, full
######################################################################################################################
######################################################################################################################
egos_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"######### Diretório contendo os arquivos dos Egos
alters_dir = "/home/amaury/coleta/n1/alters_friends/"+str(qtde_egos)+"/bin/" #### Diretório contendo os arquivos dos Alters
output_dir = "/home/amaury/redes/n1/"+str(qtde_egos)+"/graphs/" ################# Diretório para armazenamento dos arquivos das listas de arestas 
output_dir_errors = "/home/amaury/redes/n1/"+str(qtde_egos)+"/errors/" ########## Diretório para armazenamento dos erros
output_overview = "/home/amaury/redes/n1/"+str(qtde_egos)+"/" ################### Diretório contendo arquivos com informações sobre a construção das redes. 
formato = 'l'				######################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ############################################ Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
if not os.path.exists(output_dir_errors):
	os.makedirs(output_dir_errors)
if not os.path.exists(output_overview):
	os.makedirs(output_overview)	

#Executa o método main
if __name__ == "__main__": main()