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
##		Status - Versão 1 - Criar rede N5 (co-follow) a partir dos dados coletados e de acordo com as instruções a seguir:
##					Versão 1.1 - Tentar corrigir problema de elevado consumo de memória durante a criação das redes.
##									- Corrigido - Clear no grafo
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
##					2 - 	Para cada elemento i no conjunto de vertices (v[i]):
##					3 - 		Para cada elemento j no conjunto de vértices (v[j]):
##					4 - 			Se não existe uma aresta (v[i],v[j]):
##					5 - 				Cria uma aresta entre (v[i],v[j]) com peso igual ao CSJ entre seus conjuntos de alters
##					6 - 	Remova arestas com peso igual a zero
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
		friends_set = set()
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_set.add(friend[0])
	return friends_set
	
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
# Função para calcular o csj entre dois conjuntos de dados
################################################################################################         
def csj(a,b):
 intersection = len(a.intersection(b))
 union = len(a.union(b))
 return intersection/float(union)
 
################################################################################################
# Função para salvar os grafos em formato padrão para entrada nos algoritmos de detecção 
################################################################################################
def save_graph(ego, G):															# Função recebe o id do ego corrente e o grafo (lista de arestas)
	with open(output_dir+str(ego)+".edge_list", 'wb') as graph:
#		nx.write_edgelist(G, graph, data=False)							# Imprimir lista de arestas SEM PESO
		nx.write_weighted_edgelist(G,graph)									# Imprimir lista de arestas COM PESO
	G.clear()

################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,alters_list,l):												# Função recebe o id do ego, a lista de alters e o número ordinal do ego corrente
	G=nx.Graph()																	# Inicia um grafo NÂO DIRECIONADO
	G.clear()
	vertices = {}																	# Inicia tabela hash - Conjunto de vértices - EGO + ALTERS
	ti = datetime.datetime.now()												# Tempo do inicio da construção do grafo 
	partial_missing = set()
	vertices[ego] = ego															# Adiciona o Ego ao conjunto de vértices
	for alter in alters_list:
		alter = long(alter)
		vertices[alter] = alter													# Adiciona cada Alter ao conjunto de vértices				

	indice = 0

	for i in vertices:
		indice +=1
		for j in vertices:
			if i != j:
				if not G.has_edge(i,j):													### Se ainda não existe uma aresta entre os dois vértices
					try:
						if i == ego:
							i_friends = read_arq_bin(egos_dir+str(i)+".dat")		# Recebe conjunto de amigos do ego
							j_friends = read_arq_bin(alters_dir+str(j)+".dat")		# Recebe conjunto de amigos do alter i
						elif j == ego:
							i_friends = read_arq_bin(alters_dir+str(i)+".dat")		# Recebe conjunto de amigos do alter i
							j_friends = read_arq_bin(egos_dir+str(j)+".dat")		# Recebe conjunto de amigos do ego
						else:
							i_friends = read_arq_bin(alters_dir+str(i)+".dat")		# Recebe conjunto de amigos do alter i
							j_friends = read_arq_bin(alters_dir+str(j)+".dat")		# Recebe conjunto de amigos do ego
					
						csj_i_j = csj(i_friends,j_friends)								# Calcula o CSJ entre os dois conjuntos

						print ("Verificando arestas para alter "+str(indice)+" - CSJ: ("+str(i,j)+") - "+str(csj_i_j))

						G.add_edge(i,j,weight=csj_i_j)									# Cria aresta

					except IOError:															# Tratamento de exceção - caso falte algum arquivo de um autor do alter, 
						partial_missing.add(i)												# Adiciona ao conjunto de usuários faltando
						partial_missing.add(j)												# Adiciona ao conjunto de usuários faltando

	for (u,v,d) in G.edges(data='weight'):
		if d==0:
			print u,v,d
			print('(%d, %d, %.3f)'%(n,nbr,d))
#			G.remove_edge(u,v)															# Remove arestas com CJS igual a zero. Deixar pra remover aqui pq a criação delas é interessante durante o processo de geração das redes...
#			G.remove_edge(n,nbr)															# Remove arestas com CJS igual a zero. Deixar pra remover aqui pq a criação delas é interessante durante o processo de geração das redes...
	tf =  datetime.datetime.now()												# Tempo final da construção do grafo do ego corrente
	tp	= tf - ti																	# Cálculo do tempo gasto para a construção do grafo
	print ("Lista de arestas do grafo "+str(l)+" construído com sucesso. EGO: "+str(ego))
	print("Tempo para construir o grafo: "+str(tp))
				
	return G,list(partial_missing)
			
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

		print
		missing.update(partial_missing)																			# Incrementa erros totais com erros parciais recebidos da criação do grafo do ego corrente
		overview = {'ego':ego,'n_friends':n_friends,'errors':len(partial_missing),'missing':partial_missing}		# cria dicionário python com informações sobre a criação do grafo do ego corrente
		with open(output_overview+str(ego)+".json", 'w') as f:
			f.write(json.dumps(overview)) 											# Escreve o dicionário python em formato JSON no arquivo overview
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
alters_dir = "/home/amaury/dataset/n1/alters_limited_5k/bin" ## Diretório contendo os arquivos dos Alters
output_dir = "/home/amaury/graphs/n5/graphs/" ################# Diretório para armazenamento dos arquivos das listas de arestas 
output_dir_errors = "/home/amaury/graphs/n5/errors/" ########## Diretório para armazenamento dos erros
output_overview = "/home/amaury/graphs/n5/overview/" ########## Diretório contendo arquivos com informações sobre a construção das redes. 
formato = 'l'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
if not os.path.exists(output_overview):
	os.makedirs(output_overview)	

#Executa o método main
if __name__ == "__main__": main()