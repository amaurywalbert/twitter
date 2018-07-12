	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, snap

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Receber os arquivos TXT com comunidades e verificar se todos os alters estão presentes, caso não estejam, adicioná-los como singletons.
##
######################################################################################################################################################################

######################################################################################################################################################################
#
# Prepara e salva os dados
#
######################################################################################################################################################################
def save_data(graphs,alg):
	for net in range(10):
		net+=1
		print		
		print ("Inserindo rótulos na rede: n"+str(net))
		for threshold in range(51):
			threshold+=1
			
			source_dir="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"/full/n"+str(net)+"/"+str(threshold)+"/"			
			graphs_dir="/home/amaury/graphs_hashmap/n"+str(net)+"/"+str(graphs)+"/"	
			
			if not os.path.isdir(source_dir):
				print ("\nDiretório não encontrado para o threshold "+str(threshold)+"\n"+str(source_dir))
				print
			elif not os.path.isdir(graphs_dir):
				print ("\nGrafo não encontrado:"+str(source_dir))
			else:	
				i=0
				for file in os.listdir(source_dir):
					ego_id = file.split(".txt")											# pegar o nome do arquivo que indica o threshold analisado
					ego_id = ego_id[0]					
					i+=1											
					alters_detected = set() 												# Armazena o conjunto de alters detectados pelo algoritmo
					alters = set()																# Conjunto de alters do grafo

					G = snap.LoadEdgeList(snap.PUNGraph, str(graphs_dir)+str(ego_id)+".edge_list", 0, 1) # Carregar grafo						 							
					for NI in G.Nodes():
						alters.add(long(NI.GetId()))
						
					print (str(graphs)+" - Verificando vértices sem rótulos para a - rede: "+str(net)+" - threshold: "+str(threshold)+" - ego: "+str(i))
					with open(source_dir+str(file), 'r') as f:							# Abre o arquivo gerado pelo algoritmo para o usuário "file"
						for line in f:
							if not "#" in line:
								a = line.split(' ')
								if a is not None and a[0] != "\n":
									for item in a:
										if item != "\n" and item !=" ":
											try:
												if long(item) > 0:
													alters_detected.add(long(item))
											except Exception:
												pass									
					alters_ignored = alters.difference(alters_detected)
					if alters_ignored is not None and len(alters_ignored) > 0:
						j = 0
						with open(source_dir+str(file), 'a+') as g:							# Abre o arquivo gerado pelo algoritmo para o usuário "file"
							for item in alters_ignored:
								if long(item) > 0:											
									g.write(str(item)+"\n")											# Escreve os ids os elementos que estavam sem rótulos
									j+=1
						print ("QTDE alters inseridos: "+str(j))
#####################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')	
	graphs1 = "graphs_with_ego"
	graphs2 = "graphs_without_ego"
	alg = "oslom_without_weight"
	save_data(graphs1,alg)
#	save_data(graphs2,alg)
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
	
if __name__ == "__main__": main()
