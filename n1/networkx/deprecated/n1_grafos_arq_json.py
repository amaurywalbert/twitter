# -*- coding: latin1 -*-
################################################################################################
# Script para gerar os grafos a partir dos egos coletados
# Teste com 10 egos e arquivos JSON
#
#			ESTOURO DE MEMÓRIA!!!!!!!!!!!!!!!!	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct
import networkx as nx
import matplotlib.pyplot as plt	


reload(sys)
sys.setdefaultencoding('utf-8')


################################################################################################
# Gera as redes - grafos
################################################################################################
def ego_net(ego,k):
	errors = 0
	G=nx.DiGraph()
	nodes = {}
	G.add_node(ego)
	nodes[ego] = ego
	try:
		with open(dir_data+str(ego)+".json",'r') as ego_file:
			ego_data = ego_file.read()
			ego_friends = json.loads(ego_data)
			for alter in ego_friends:
				G.add_node(alter)
				nodes[alter] = alter
				G.add_edge(ego,alter)
				try:
					with open(dir_data+str(alter)+".json",'r') as alter_file:
						alter_data = alter_file.read()
						alter_friends = json.loads(alter_data)
						for friend in alter_friends																																																																																																																																																																																																																																																																																																																																																																																																																																						:
							node = nodes.get(friend) 
							if node:							#Consulta na tabela se o nó já foi adicionado																																																																							 
								G.add_edge(alter,friend)
							else:						
								G.add_node(friend)
								nodes[friend] = friend
								G.add_edge(alter,friend)						
				except IOError as a:
					print ("Arquivo não encontado. Alter: "+str(alter)+" - Erro: "+str(a))
					errors +=1
		print
		hub_ego=nx.ego_graph(G,ego)
		pos=nx.spring_layout(hub_ego)
		nx.draw(hub_ego,pos,node_color='b',node_size=0.2,with_labels=False)
		nx.draw_networkx_nodes(hub_ego,pos,nodelist=G.nodes(),node_size=10,node_color='r')
		plt.savefig(output_dir+str(ego)+".png")
		plt.show()		
#		print ("Exportando arquivo GEXF...")										
#		nx.write_gexf(G, output_dir+str(ego)+".gexf")
		print ("Gráfico da rede "+str(k)+" construído com sucesso. EGO: "+str(ego))	
	except IOError as e:
		print ("Arquivo não encontado. EGO: "+str(ego)+" - Erro: "+str(e))
	return G,errors
		
################################################################################################
# Método Principal do Script
################################################################################################
def main():
	tt_i =  datetime.datetime.now()
	errors_t = 0
	with open(users_list_file,'r') as users_list:		#Percorre o arquivo de usuários já verificados
		for k in range(0,ego_limit):
			te_i = datetime.datetime.now()
			user = users_list.readline()						#Leia id do usuário corrente
			print("######################################################################")
			print ("Construindo grafo do ego n: "+str(k))			
			G, errors = ego_net(long(user), k)								#Inicia função de geração do grafo
			te_f =  datetime.datetime.now()
			te	= te_f - te_i
			print("Tempo para construir o grafo do ego n "+str(k)+": "+str(te))
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
output_dir = "/home/amaury/coleta/n1_10egos/json/graphs/" #################### Diretório para armazenamento das imagens das redes ego 
dir_data = "/home/amaury/coleta/n1_10egos/json/files/json/" #################### Diretório para armazenamento dos arquivos
users_list_file = "/home/amaury/coleta//n1/egos/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados
ego_limit = 10					####################################### Controla a quantidade de egos a serem pesquisados
################################################################################################
################################################################################################
#Cria os diretórios para armazenamento das redes ego (grafos)
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()	