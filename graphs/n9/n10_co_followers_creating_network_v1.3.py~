# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import networkx as nx
import matplotlib.pyplot as plt
from math import*

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Criar rede N10 (co-followers) a partir dos dados coletados e de acordo com as instruções a seguir:
##					Versão 1.1 - Tentar corrigir problema de elevado consumo de memória durante a criação das redes.
##									- Corrigido - Clear no grafo
##					Versão 1.2 - Usar conjunto de dados com 500 egos aleatórios.
##					Versão 1.3 - remover a parte de registrar arquivos faltando... "partial missing"
##									 Carregar dados dos alters em memória
##								
## # INPUT:
##		- Lista de Egos (egos)
##		- Conjunto Followers (alters) de cada Ego - Formação do conjunto de Alters
##		- Conjunto Followee (amigos) de cada Alter (ids)
##
## # ALGORITMO
##					0 - Para cada ego[i]:
##					1 - 	Inicializa o ego_[i] e todos os seus seguidores (alters[i][n]) como vértices de um grafo - (tabela hash - ego+alters - vertices)
##					2 - 	Para cada elemento i no conjunto de vertices (v[i]):
##					3 - 		Para cada elemento j no conjunto de vértices (v[j]):
##					4 -   		Com i != j:	
##					5 - 				Se não existe uma aresta (v[i],v[j]):
##					6 - 					Cria uma aresta entre (v[i],v[j]) com peso igual ao CSJ entre seus conjuntos de alters
##					7 - 	Remova arestas com peso igual a zero
##
##					OBS.: Consumo muito elevado de memória... corrigir na próxima versão.
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
		followers_set = set()
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			follower = user_struct.unpack(buffer)
			followers_set.add(long(follower[0]))
	return followers_set
	
################################################################################################
# Função para calcular o csj entre dois conjuntos de dados
################################################################################################         
def csj(a,b):
	intersection = len(a.intersection(b))
	union = len(a.union(b))
# Calcula o CSJ entre os dois conjuntos e atribui 0 caso a união dos conjuntos for 0	
	if union != 0:
		result = intersection/float(union)									# float(uniao) para resultado no intervalo [0,1]
	else:
		result = 0
	return result
 
################################################################################################
# Função para salvar os grafos em formato padrão para entrada nos algoritmos de detecção 
################################################################################################
def save_graph(ego, G):															# Função recebe o id do ego corrente e o grafo (lista de arestas)
	with open(output_dir+str(ego)+".edge_list", 'wb') as graph:
		nx.write_weighted_edgelist(G,graph)									# Imprimir lista de arestas COM PESO
	G.clear()

################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,alters_set,l):												# Função recebe o id do ego, a lista de alters e o número ordinal do ego corrente
	G=nx.Graph()																	# Inicia um grafo NÂO DIRECIONADO
	G.clear()
	ti = datetime.datetime.now()												# Tempo do inicio da construção do grafo
	########################################### # Criar tabela hash com o conjunto de dados (retweets) dos vértices (ego e todos os alters)
	vertices = {}
	vertices[ego] = alters_set															# Adiciona o Ego ao conjunto de vértices
	for alter in alters_set:
		try:
			alters_friends = read_arq_bin(alters_dir+str(alter)+".dat")	# Chama função para converter o conjunto de amigos dos alters do formato Binário para uma lista do python
			vertices[alter] = alters_friends										# Adiciona conjunto de dados do alter à tabela hash
		except IOError:																# Tratamento de exceção - caso falte algum arquivo do alter, 
			pass
	###########################################	
	print ("Construindo grafo do ego n: "+str(l)+" - Quantidade de vertices: "+str(len(vertices)))
	indice = 0
	########################################### # Criando arestas
	for i in vertices:	
		indice +=1
		print ("Ego: "+str(l)+" - Verificando arestas para alter: "+str(indice)+"/"+str(len(alters_set)))
		for j in vertices:
			if i != j:
				if not G.has_edge(i,j):												### Se ainda não existe uma aresta entre os dois vértices
					csj_i_j = csj(vertices[i],vertices[j])							# Calcula o CSJ entre os dois conjuntos
					G.add_edge(i,j,weight=csj_i_j)									# Cria aresta

	########################################### # Remove arestas com CJS igual a zero.
	########################################### # Deixar pra remover aqui pq a criação delas é interessante durante o processo de geração das redes...
	for (u,v,d) in G.edges(data='weight'):
		if d==0:
			G.remove_edge(u,v)
	###########################################
	tf =  datetime.datetime.now()												# Tempo final da construção do grafo do ego corrente
	tp	= tf - ti																	# Cálculo do tempo gasto para a construção do grafo
	print ("Lista de arestas do grafo "+str(l)+" construído com sucesso. EGO: "+str(ego))
	print("Tempo para construir o grafo: "+str(tp))
				
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
	missing = set()																# Conjunto de usuários faltando faltando...	
	l = 0																				# Variável para exibir o número ordinal do ego que está sendo usado para a construção do grafo
	ti =  datetime.datetime.now()												# Tempo de início do processo de criação de todos os grafos
	for file in os.listdir(egos_dir):										# Para cada arquivo de Ego no diretório
		l+=1																			# Incrementa contador do número do Ego
		ego = file.split(".dat")												# Separa a extensão do id do usuário no nome do arquivo
		ego = long(ego[0])														# recebe o id do usuário em formato Long
		if not dictionary.has_key(ego):
			alters_set = read_arq_bin(egos_dir+file)							# Chama função para converter o conjunto de seguidores do ego do formato Binário para uma lista do python
			n_friends = len(alters_set)											# Variável que armazena o tamanho da lista do usuário corrente

			print("######################################################################")
			print ("Construindo grafo do ego n: "+str(l)+" - Quantidade de alters: "+str(n_friends))
			G = ego_net(ego,alters_set,l)										# Inicia função de criação do grafo (lista de arestas) para o ego corrente
			print
			print("Salvando o grafo...")
			save_graph(ego,G)
			G.clear()
			print("######################################################################")

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
egos_dir = "/home/amaury/dataset/n9/egos_limited_5k/bin/"###### Diretório contendo os arquivos dos Egos
alters_dir = "/home/amaury/dataset/n9/alters_limited_5k/bin/" # Diretório contendo os arquivos dos Alters
output_dir = "/home/amaury/graphs/n10/graphs/" ################# Diretório para armazenamento dos arquivos das listas de arestas 
output_dir_errors = "/home/amaury/graphs/n10/errors/" ########## Diretório para armazenamento dos erros
formato = 'l'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

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