	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Receber o conjunto de conjunto de comunidades e separar em conjunto sem singletons e conjunto de singletons.
##								
## # INPUT:
##		- Arquivos com as comunidades completas
## # OUTPUT:
##		- Arquivos com as comunidades sem singletons
######################################################################################################################################################################

######################################################################################################################################################################
#
# Salva os dados nas respectivas pastas
#
######################################################################################################################################################################
def save_data(graph):
	for net in range(10):
		net+=1
		print		
		print ("Separando comunidades da rede: n"+str(net))
		for threshold in range(20):
			threshold+=1

			source_dir="/home/amaury/communities/"+str(graph)+"/copra/raw/n"+str(net)+"/"+str(threshold)+"/"

			output_full="/home/amaury/communities/"+str(graph)+"/copra/full/n"+str(net)+"/"+str(threshold)+"/"
			output_singletons="/home/amaury/communities/"+str(graph)+"/copra/singletons/n"+str(net)+"/"+str(threshold)+"/"
			output_without_singletons="/home/amaury/communities/"+str(graph)+"/copra/without_singletons/n"+str(net)+"/"+str(threshold)+"/"

			if not os.path.isdir(source_dir):
				#print ("\nDiretório não encontrado para o threshold "+str(threshold)+"\n"+str(source_dir))
				print
			else:	
				if not os.path.exists(output_full):		
					os.makedirs(output_full)	
				if not os.path.exists(output_singletons):		
					os.makedirs(output_singletons)	
				if not os.path.exists(output_without_singletons):
					os.makedirs(output_without_singletons)	
						
				i=0
				for file in os.listdir(source_dir):		
					i+=1
					print (str(graph)+" - Verificando singletons para a - rede: "+str(net)+" - threshold: "+str(threshold)+" - ego: "+str(i))

					if os.path.isfile(output_full+file):									#Limpar diretórios
						os.remove(output_full+file)	
					if os.path.isfile(output_without_singletons+file):
						os.remove(output_without_singletons+file)
					if os.path.isfile(output_singletons+file):
						os.remove(output_singletons+file)				
						
					with open(source_dir+file, 'r') as f:
						ego_id = file.split(".edge_list")											# pegar o nome do arquivo que indica o threshold analisado
						ego_id = ego_id[0]
						ego_id = ego_id.split("clusters-")			
						ego_id = ego_id[1]
													
						for line in f:
							a = line.split(' ')
							with open(output_full+ego_id+".txt", 'a+') as g:
								for item in a:
									if item != "\n":											
										g.write(str(item)+" ")										# Escreve os ids das Listas separadas por espaço
								g.write("\n")															# Passa para a próxima linha de g

							if len(a) > 2:
								with open(output_without_singletons+".txt", 'a+') as g:
									for item in a:
										if item != "\n":											
											g.write(str(item)+" ")									# Escreve os ids das Listas separadas por espaço
									g.write("\n")														# Passa para a próxima linha
							else:			
								with open(output_singletons+str(ego_id)+".txt", 'a+') as g:
									for item in a:
										if item != "\n":
											g.write(str(item)+" ")									# Escreve os ids das Listas separadas por espaço
									g.write("\n")														
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')	
	graph1 = "graphs_with_ego"
	graph2 = "graphs_without_ego"
	save_data(graph1)
	save_data(graph2)

				
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

	
if __name__ == "__main__": main()