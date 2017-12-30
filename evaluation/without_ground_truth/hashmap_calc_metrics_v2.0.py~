# -*- coding: latin1 -*-
################################################################################################
import snap,datetime, sys, time, json, os, os.path, shutil, time, struct, random
import metrics


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular métrica definida abaixo para avaliação sem ground truth
##					Versão 2 - Calcular todas as métricas métrica definidas abaixo para avaliação sem ground truth
## 
##			SALVA ARQUIVOS NOS DIRETÒRIOS:
##				RAW: conforme calculado - 
##				SEPARATE BY METRICS
## 							
## # INPUT: Arquivos com as comunidades detectadas, rede e o ground truth
## 
## # OUTPUT:
##			Resultados separados por métrica
######################################################################################################################################################################

		
######################################################################################################################################################################
#
# Recebe arquivo e devolve dicionário com as comunidades
#
######################################################################################################################################################################
def prepare_communities(community_file):
	i=0
	communities = {}
	for line in community_file:
		i+=1
		key="com"+str(i)																# Chave para o dicionário comm
		comm = []																		# Lista para armazenar as comunidades			
		a = line.split(' ')
		for item in a:
			if item != "\n":
				comm.append(long(item))
		communities[key] = comm														# dicionário communities recebe a lista de ids das comunidades tendo como chave o valor key
	return communities

######################################################################################################################################################################
#
# Criar diretórios
#
######################################################################################################################################################################
def create_dirs(out_ad,out_c,out_cut_r,out_d,out_e,out_normal_cut,out_s):
	
	if not os.path.exists(out_ad):
		os.makedirs(out_ad)	
	if not os.path.exists(out_c):
		os.makedirs(out_c)
	if not os.path.exists(out_cut_r):
		os.makedirs(out_cut_r)		
	if not os.path.exists(out_d):
		os.makedirs(out_d)
	if not os.path.exists(out_e):
		os.makedirs(out_e)
	if not os.path.exists(out_normal_cut):
		os.makedirs(out_normal_cut)		
	if not os.path.exists(out_s):
		os.makedirs(out_s)	

######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(singletons,net,uw,ud,g_type,alg):
	
	communities = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/" 
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type)+"/"
	
	out_ad = str(output_dir)+"average_degree/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"		
	out_c = str(output_dir)+"conductance/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"	
	out_cut_r = str(output_dir)+"cut_ratio/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_d = str(output_dir)+"density/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_e = str(output_dir)+"expansion/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_normal_cut = str(output_dir)+"normalized_cut/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_s = str(output_dir)+"separability/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	
	if not os.path.exists(communities):
		print ("Diretório com as comunidades não encontrado: "+str(communities)+"\n")

	else:
		print("\n######################################################################")

		for threshold in os.listdir(communities):
			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Threshold para a rede "+str(net)+" não encontrado: "+str(threshold))

			else:
				create_dirs(out_ad,out_c,out_cut_r,out_d,out_e,out_normal_cut,out_s)

				if os.path.exists(str(out_ad)+str(threshold)+".json") and os.path.exists(str(out_c)+str(threshold)+".json") and os.path.exists(str(out_cut_r)+str(threshold)+".json") and os.path.exists(str(out_d)+str(threshold)+".json") and os.path.exists(str(out_e)+str(threshold)+".json") and os.path.exists(str(out_normal_cut)+str(threshold)+".json") and os.path.exists(str(out_s)+str(threshold)+".json"):
					print ("Arquivo de destino já existe: "+str(threshold)+".json")
					
				else:	
					print("######################################################################")
							
					result_ad = []					
					result_c = []
					result_cut_r = []
					result_d = []
					result_e = []
					result_normal_cut = []
					result_s = []

					i=0 		#Ponteiro para o ego
					for file in os.listdir(str(communities)+str(threshold)+"/"):
						if os.path.isfile(str(communities)+str(threshold)+"/"+file):
							ego_id = file.split(".txt")
							ego_id = long(ego_id[0])
							i+=1

							if not os.path.isfile(str(graphs)+str(ego_id)+".edge_list"):
								print ("ERROR - EGO: "+str(i)+" - Arquivo com lista de arestas não encontrado:" +str(graphs)+str(ego_id)+".edge_list")

							else:
								with open(str(communities)+str(threshold)+"/"+file, 'r') as community_file:
									if ud is False:
										G = snap.LoadEdgeList(snap.PNGraph, str(graphs)+str(ego_id)+".edge_list", 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
									else:
										G = snap.LoadEdgeList(snap.PUNGraph, str(graphs)+str(ego_id)+".edge_list", 0, 1)						# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')

									print(str(g_type)+" - "+str(alg)+" - "+str(singletons)+" - Rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego("+str(i)+"): "+str(file))
									
									communities_dict = prepare_communities(community_file)							#Função para devolver um dicionário com as comunidades							
									
									avg_ad,avg_c,avg_cut_r,avg_d,avg_e,avg_normal_cut,avg_s = metrics.calc_metrics(communities_dict,G,ud)		# Calcular as métricas
									
#									result_ad.append(avg_ad['media'])  									# Salvar Métrica									
#									result_c.append(avg_c['media'])  									# Salvar Métrica
#									result_cut_r.append(avg_cut_r['media'])  									# Salvar Métrica
									result_d.append(avg_d['media'])  									# Salvar Métrica
#									result_e.append(avg_e['media'])  									# Salvar Métrica
#									result_normal_cut.append(avg_normal_cut['media'])  									# Salvar Métrica									
#									result_s.append(avg_s['media'])  									# Salvar Métrica
#
#									print ("Average Degree: "+str(result_ad[i-1])+" - Conductance: "+str(result_c[i-1])+" - Cut Ratio: "+str(result_cut_r[i-1])+" - Density: "+str(result_d[i-1]))
#									print ("Expansion: "+str(result_e[i-1])+" - Normalized Cut: "+str(result_normal_cut[i-1])+" - Separability: "+str(result_s[i-1]))
#									print 
#					print("######################################################################")	
#
#					with open(str(out_ad)+str(threshold)+".json", "w") as f:
#						f.write(json.dumps(result_ad, separators=(',', ':'))+"\n")
#						
#					with open(str(out_c)+str(threshold)+".json", "w") as f:
#						f.write(json.dumps(result_c, separators=(',', ':'))+"\n")
#
#					with open(str(out_cut_r)+str(threshold)+".json", "w") as f:
#						f.write(json.dumps(result_cut_r, separators=(',', ':'))+"\n")
#											
					with open(str(out_d)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(result_d, separators=(',', ':'))+"\n")
#
#					with open(str(out_e)+str(threshold)+".json", "w") as f:
#						f.write(json.dumps(result_e, separators=(',', ':'))+"\n")
#
#					with open(str(out_normal_cut)+str(threshold)+".json", "w") as f:
#						f.write(json.dumps(result_normal_cut, separators=(',', ':'))+"\n")
#
#					with open(str(out_s)+str(threshold)+".json", "w") as f:
#						f.write(json.dumps(result_s, separators=(',', ':'))+"\n")						

	print("######################################################################")		

######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" 			Avaliação de Comunidades - Amaury's Software										"
	print"																											"
	print"#################################################################################"
	print
	print
	print"  1 - Follow"
	print"  9 - Follwowers"
	print"  2 - Retweets"
	print"  3 - Likes"
	print"  4 - Mentions"
	
	print " "
	print"  5 - Co-Follow"
	print" 10 - Co-Followers"				
	print"  6 - Co-Retweets"
	print"  7 - Co-Likes"
	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))

	if op in (5,6,7,8,10):																						# Testar se é um grafo direcionado ou não
		ud = True
	elif op in (1,2,3,4,9):
		ud = False 
	else:
		print("Opção inválida! Saindo...")
		sys.exit()

	if op == 1 or op == 9:																						# Testar se é um grafo direcionado ou não
		uw = True
	else:
		uw = False
	print
	print ("\n")
######################################################################
	
	net = "n"+str(op)	

#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print 
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print"  3 - GN"		
	print"  4 - COPRA - Partition"						
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"
	elif op2 == 3:
		alg = "gn"
	elif op2 == 4:
		alg = "copra_partition"				
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()		
	print
	print ("\n")
#######################################################################
#######################################################################	

	print
	print ("Opção escolhida: "+str(net)+" - "+str(alg))
	print ("Aguarde...")
	time.sleep(5)
	
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"
	
	singletons1 = "full"
	singletons2 = "without_singletons"

	
######################################################################################################################
	os.system('clear')
	
	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type1)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,uw,ud,g_type1,alg)
	

#	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons2))
#	calculate_alg(singletons2,net,uw,ud,g_type1,alg)
	

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type3)+" - Algoritmo: "+str(alg)+" - "+str(singletons3))
	calculate_alg(singletons1,net,uw,ud,g_type2,alg)


#	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type4)+" - Algoritmo: "+str(alg)+" - "+str(singletons4))
#	calculate_alg(singletons2,net,uw,ud,g_type2,alg)
	

######################################################################################################################		

	print("######################################################################")
	print("\nScript finalizado!\n")
	print("######################################################################\n")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

output_dir = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/density_v2/"

######################################################################################################################
if __name__ == "__main__": main()
