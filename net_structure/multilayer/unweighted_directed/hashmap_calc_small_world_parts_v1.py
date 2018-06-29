# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil
import networkx as nx


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular se as redes-ego são small-world.
##								- Considerar apenas redes-ego com a presença do ego.
##								- Calcula-se as métricas a partir da lista de arestas...
##
##								- Os egos estão separados em cinco conjuntos para facilitar o paralelismo
## 
##	INPUT: Redes-ego
##
## Output: arquivo texto. Formato:
##
##ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dir(x):
	if not os.path.exists(x):
		os.makedirs(x)		

######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(ego,dataset,out_file):
	out_file.write(json.dumps(dataset)+"\n")				# Salva linha com os dados calculados para o ego i
	ego = long(ego)
	egos_saved[ego] = ego										# Adiciona o id do ego na tabela hash dos já calculados
	
		
######################################################################################################################################################################
#
# Cálcular Métricas para verificar small world
#
######################################################################################################################################################################
def calc_metric(net,i,ego,G):
	nodes = G.nodes()
	edges = G.edges()
	print (str(net)+" "+str(i)+" - Gerando grafo aleatório com "+str(len(nodes))+" vertices e "+str(len(edges))+" arestas...")


	connected = False
	while not connected:
		print (str(net)+" "+str(i)+" - Testando se grafo é conectado...")		
		Gnm = nx.gnm_random_graph(len(nodes), len(edges), directed=True)	# Cria um grafo aleatório com as mesmas dimensões do original (nodes,edges)
		connected = nx.is_weakly_connected(Gnm)
	print (str(net)+" "+str(i)+" - Grafo conectado... OK")


	print (str(net)+" "+str(i)+" - Calculando transitividade...")
	transitivity_G = nx.transitivity(G)												# Calcula a transitividade do grafo.
	transitivity_Gnm = nx.transitivity(Gnm)										# Calcula a transitividade do grafo aleatório


	print (str(net)+" "+str(i)+" - Calculando média dos menores caminhos mínimos...")				
	avg_spl_G = nx.average_shortest_path_length(G)								# Calcula a média dos caminhos mínimos para todo o grafo.
	avg_spl_Gnm = nx.average_shortest_path_length(Gnm)							# Calcula a média dos caminhos mínimos para todo o grafo aleatório


	if transitivity_Gnm == 0:
		GAMMA = 0
	else:		
		GAMMA = float(transitivity_G)/float(transitivity_Gnm)					# Numerador da métrica S
	LAMBDA = float(avg_spl_G)/float(avg_spl_Gnm)									# Denominador da métrica S
	

	S = float(GAMMA)/float(LAMBDA)													# Métrica S de acordo com o artigo que o Prof. Thierson enviou
	return transitivity_G, transitivity_Gnm, avg_spl_G, avg_spl_Gnm, S

######################################################################################################################################################################
#
# Preparar os dados  
#
######################################################################################################################################################################
def prepare(net,out_file,egos_set,current_set):
	create_dir(output_dir)																					# Cria diretótio para salvar arquivos.	

	i=0																											# Contador do ego
	for ego in egos_set:
		i+=1
		if ego in egos_saved:
			print (str(net)+" "+str(i)+" - Métrica já calculada para o ego: "+str(ego))		
		else:	
			dataset = {}																						# Salvar Arquivos no Formato Json - linha por linha
			source = str(data_dir)+str(net)+"/graphs_with_ego/"+str(ego)+".edge_list"
			if not os.path.isfile(source):																# Verifica se diretório existe	
				print (str(net)+" "+str(i)+" - Impossível localizar arquivo com lista de arestas: "+str(source))
			else:
				G = nx.read_edgelist(source,create_using=nx.DiGraph())	
				transitivity_G,transitivity_Gnm, avg_spl_G, avg_spl_Gnm, S = calc_metric(net,i,ego,G) # Calcula Métrica
				dataset[ego] = {"transitivity_G":transitivity_G,"transitivity_Gnm":transitivity_Gnm,"avg_spl_G":avg_spl_G,"avg_spl_Gnm":avg_spl_Gnm,"S":S}			
				print net,i,ego,current_set,dataset[ego]
				print("\n###########################################################")
				print

				save_json(ego,dataset,out_file)										# Salvar arquivo no formato JSON com todos os dados calculados

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" Verificação de Small World"
	print"																											"
	print"#################################################################################"
	print
	print
	print"  1 - Follow"
#	print"  9 - Follwowers"
	print"  2 - Retweets"
	print"  3 - Likes"
	print"  4 - Mentions"
	
#	print " "
#	print"  5 - Co-Follow"
#	print" 10 - Co-Followers"				
#	print"  6 - Co-Retweets"
#	print"  7 - Co-Likes"
#	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))

	print("\n###########################################################\n")
	print"  1 - set 1 -->   1 - 100"
	print"  2 - set 2 --> 101 - 200"
	print"  3 - set 3 --> 201 - 300"
	print"  4 - set 4 --> 301 - 400"
	print"  5 - set 5 --> 401 - 500"
			
	print
	op2 = int(raw_input("Escolha uma opção acima: "))


	if op not in (1,2,3,4) or op2 not in (1,2,3,4,5):
		print ("Opção inválida...")
		sys.exit()
		
	if op2 == 1:
		egos_set = egos_sets["set1"]
		current_set = "set1"
	if op2 == 2:
		egos_set = egos_sets["set2"]
		current_set = "set2"
	if op2 == 3:
		egos_set = egos_sets["set3"]
		current_set = "set3"
	if op2 == 4:
		egos_set = egos_sets["set4"]
		current_set = "set4"
	if op2 == 5:
		egos_set = egos_sets["set5"]
		current_set = "set5"
	print("\n###########################################################")
	
	net = "n"+str(op)
		
	if os.path.exists(str(output_dir)+str(net)+".json"):
		print ("Arquivo de destino já existe! "+str(output_dir)+str(net)+".json - Fazendo leitura do arquivo...\n")
		out_file_total = open(str(output_dir)+str(net)+".json",'r')
		for line in out_file_total:
			data_saved = json.loads(line)
			for k,v in data_saved.iteritems():
				k = long(k)
				if not k in egos_saved:
					egos_saved[k] = k														#lê o arquivo e armazena uma tabela hash com o id dos egos já calculados

	if os.path.exists(str(output_dir)+str(net)+"_"+str(current_set)+".json"):
		print ("Arquivo de destino já existe! "+str(output_dir)+str(net)+"_"+str(current_set)+".json - Fazendo leitura do arquivo...\n")
		out_file = open(str(output_dir)+str(net)+"_"+str(current_set)+".json",'a+')
		for line in out_file:
			data_saved = json.loads(line)
			for k,v in data_saved.iteritems():
				k = long(k)
				if not k in egos_saved:
					egos_saved[k] = k														#lê o arquivo e armazena uma tabela hash com o id dos egos já calculados
	else:
		out_file = open(str(output_dir)+str(net)+"_"+str(current_set)+".json",'a+') # Se arquivo não existe então apenas abre o arquivo

	prepare(net,out_file,egos_set,current_set)													# Prepara os dados para cálculo e armazenamento dos dados
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

egos_ids = "/home/amaury/graphs_hashmap_infomap_without_weight/n1/graphs_with_ego/"										# Pegar a lista com os ids dos egos

data_dir = "/home/amaury/graphs_hashmap_infomap_without_weight/"																# Diretório com as redes-ego
output_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world/"	# Pegar a lista com os ids dos egos

metric = "small_world"
egos_saved = {}

egos_set_file = "/home/amaury/Dropbox/egos_in_five_sets.json"

f = open(egos_set_file, "r")
egos_sets = json.load(f)

	#Executa o método main
if __name__ == "__main__": main()