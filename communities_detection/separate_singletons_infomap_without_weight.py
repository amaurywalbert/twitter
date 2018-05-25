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
# Prepara e salva os dados
#
######################################################################################################################################################################
def save_data(graphs,alg):
	for net in range(10):
		net+=1
		print		
		print ("Separando comunidades da rede: n"+str(net))
		for threshold in range(51):
			threshold+=1
			
			source_dir="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"_without_weight/raw/n"+str(net)+"/"+str(threshold)+"/"
			
			output_full="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"_without_weight/full/n"+str(net)+"/"+str(threshold)+"/"			
			output_singletons="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"_without_weight/singletons/n"+str(net)+"/"+str(threshold)+"/"
			output_without_singletons="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"_without_weight/without_singletons/n"+str(net)+"/"+str(threshold)+"/"
			
			if not os.path.isdir(source_dir):
				print ("\nDiretório não encontrado para o threshold "+str(threshold)+"\n"+str(source_dir))
				print
			else:	
				if os.path.exists(output_full):
					shutil.rmtree(output_full)		
					os.makedirs(output_full)	
				else:
					os.makedirs(output_full)

				if os.path.exists(output_singletons):
					shutil.rmtree(output_singletons)		
					os.makedirs(output_singletons)	
				else:
					os.makedirs(output_singletons)						

				if os.path.exists(output_without_singletons):
					shutil.rmtree(output_without_singletons)		
					os.makedirs(output_without_singletons)	
				else:
					os.makedirs(output_without_singletons)


				i=0
				for file in os.listdir(source_dir):	
					ego_id = file.split(".map")
					ego_id = ego_id[0]				
					if not os.path.exists(source_dir+str(file)):
						print ("Diretório não encontrado: "+str(source_dir)+str(file))
					else:	
						i+=1
						print (str(graphs)+" - Verificando singletons para a - rede: "+str(net)+" - threshold: "+str(threshold)+" - ego: "+str(i)+"  - "+str(file))

						if os.path.isfile(output_full+file):											#Limpar diretórios
							os.remove(output_full+file)	
						if os.path.isfile(output_without_singletons+file):
							os.remove(output_without_singletons+file)
						if os.path.isfile(output_singletons+file):
							os.remove(output_singletons+file)	

						with open(source_dir+str(file), 'r') as f:							# Abre o arquivo gerado pelo algoritmo para o usuário "file
							aux = 0
							i = 0
							elements = []
							hashmap = {}
							for line in f:
								if not "#" in line:
									if not "*" in line:
										if not "," in line:
											if "\"" in line:
												comm_id,a = line.split(':')
												b,c,d = a.split(" ")
												member_id = c[1:-1]
												
												if aux < int(b):
													aux = int(b)
													elements.append(member_id)
												else:
													aux = 0
													i+=1
													hashmap[i] = elements
													elements = []
													elements.append(member_id)
							i+=1
							hashmap[i] = elements

							with open(output_full+str(ego_id)+".txt", 'a+') as g:
								for k,v in hashmap.iteritems():
									for item in v:
										g.write(str(item)+" ")											# Escreve os ids das Listas separadas por espaço
									g.write("\n")															# Passa para a próxima linha de g

							if len(hashmap) > 2:
								with open(output_without_singletons+str(ego_id)+".txt", 'a+') as g:
									for k,v in hashmap.iteritems():
										for item in v:
											g.write(str(item)+" ")										# Escreve os ids das Listas separadas por espaço
										g.write("\n")														# Passa para a próxima linha de g
							else:
								with open(output_singletons+str(ego_id)+".txt", 'a+') as g:
									for k,v in hashmap.iteritems():
										for item in v:
											g.write(str(item)+" ")										# Escreve os ids das Listas separadas por espaço
										g.write("\n")														# Passa para a próxima linha de g
						
												
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
	alg = "infomap"
	save_data(graphs1,alg)
	save_data(graphs2,alg)
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
	
if __name__ == "__main__": main()
