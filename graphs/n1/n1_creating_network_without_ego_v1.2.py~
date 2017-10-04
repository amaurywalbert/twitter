# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import networkx as nx
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Criar rede N1 (follow) a partir dos dados coletados e de acordo com as instruções a seguir:
##					Versão 1.1 - Tentar corrigir problema de elevado consumo de memória durante a criação das redes.
##									- Clear no grafo em 3 locais (deu certo - verificar qual dos 3??)
##					Versão 1.2 - Usar conjunto de dados com 500 egos aleatórios.
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
	with open(output_dir+str(ego)+".edge_list", 'wb') as graph:
		nx.write_edgelist(G, graph, data=False)
	G.clear()

################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,alters_list,l):												# Função recebe o id do ego, a lista de alters e o número ordinal do ego corrente
	G=nx.DiGraph()																	# Inicia um grafo DIRECIONADO
	G.clear()
	vertices = {}																	# Inicia tabela hash - Conjunto de vértices - ALTERS
	partial_missing=[]															# Lista de usuários faltando
	ti = datetime.datetime.now()												# Tempo do inicio da construção do grafo 
#	vertices[ego] = ego															# Adiciona o Ego ao conjunto de vértices
	for alter in alters_list:
		alter = long(alter)
		vertices[alter] = alter													# Adiciona cada Alter ao conjunto de vértices				
#		G.add_edge(ego,alter)													# Cria uma aresta entre o Ego e cada Alter - Adiciona alter com arquivo em branco
	i = 0
	for alter in alters_list:
		i+=1	
		try:
			friends = read_arq_bin(alters_dir+str(alter)+".dat")		# Recebe lista de amigos de cada alter
			for friend in friends:												# Para cada amigo
				if alter != friend:												### Remover self-loops				
					friend = long(friend)
					if vertices.has_key(friend):								# Se amigo está na lista de alters		
						G.add_edge(alter,friend)								### Cria aresta
		except IOError as e:															# Tratamento de exceção - caso falte algum arquivo de um amigo do alter, 
			partial_missing.append(alter)															# Adiciona alter à lista com usuários faltando		
		
	tf =  datetime.datetime.now()												# Tempo final da construção do grafo do ego corrente
	tp	= tf - ti																	# Cálculo do tempo gasto para a construção do grafo
	print ("Lista de arestas do grafo "+str(l)+" construído com sucesso. EGO: "+str(ego))
	print("Tempo para construir o grafo: "+str(tp))
				
	return G,partial_missing																	# Função retorna o grafo, o número de erros parciais e o tempo gasto para a construção do grafo
			
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	missing = set()																# Conjunto de usuários faltando faltando...	
	l = 0																				# Variável para exibir o número ordinal do ego que está sendo usado para a construção do grafo
	ti =  datetime.datetime.now()												# Tempo de início do processo de criação de todos os grafos
	for file in os.listdir(egos_dir):										# Para cada arquivo de Ego no diretório
		l+=1																			# Incrementa contador do número do Ego
		ego = file.split(".dat")												# Separa a extensão do id do usuário no nome do arquivo
		ego = long(ego[0])														# recebe o id do usuário em formato Long
		if not dictionary.has_key(ego):
			alters_list = read_arq_bin(egos_dir+file)							# Chama função para converter o conjunto de amigos do ego do formato Binário para uma lista do python
			n_friends = len(alters_list)											# Variável que armazena o tamanho da lista do usuário corrente

			print("######################################################################")
			print ("Construindo grafo do ego n: "+str(l)+" - Quantidade de amigos: "+str(n_friends))
			G, partial_missing = ego_net(ego,alters_list, l)							# Inicia função de criação do grafo (lista de arestas) para o ego corrente
			print("Quantidade de usuários faltando: "+str(len(partial_missing)))
			print
			print("Salvando o grafo...")

			save_graph(ego,G)
			G.clear()
			print("######################################################################")
			missing.update(partial_missing)																			# Incrementa erros totais com erros parciais recebidos da criação do grafo do ego corrente
			overview = {'ego':ego,'n_friends':n_friends,'errors':len(partial_missing),'missing':partial_missing}		# cria dicionário python com informações sobre a criação do grafo do ego corrente
			with open(output_overview, 'a+') as f:
				f.write(json.dumps(overview,separators=(',', ':'))+"\n")			# Escreve o dicionário python em formato JSON no arquivo overview

		else:
			print ("Lista de arestas já criada para o ego "+str(l)+": "+str(ego))

	print	
	tf =  datetime.datetime.now()													# Recebe tempo final do processo de construção dos grafos
	t = tf - ti																			# Calcula o tempo gasto com o processo de criação dos grafos
	print("Tempo total do script: "+str(t))
	print("Quantidade total de usuários faltando: "+str(len(missing)))
	print("######################################################################")
	print("Networks created!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
egos_dir = "/home/amaury/dataset/n1/egos_limited_5k/bin/"###### Diretório contendo os arquivos dos Egos
alters_dir = "/home/amaury/dataset/n1/alters_limited_5k/bin/" ## Diretório contendo os arquivos dos Alters
output_dir = "/home/amaury/graphs/n1/graphs_without_ego/" ################# Diretório para armazenamento dos arquivos das listas de arestas 
output_overview = "/home/amaury/graphs/n1/overview_without_ego.json" ########## Diretório contendo arquivos com informações sobre a construção das redes. 
formato = 'l'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

if os.path.isfile(output_overview):
	os.remove(output_overview)	

###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
for file in os.listdir(output_dir):
	user_id = file.split(".edge_list")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")

#Executa o método main
if __name__ == "__main__": main()