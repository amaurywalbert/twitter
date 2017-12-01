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

		source_dir="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"/raw/n"+str(net)+"/"
			
		output_full="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"/full/n"+str(net)+"/1/"			
		output_singletons="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"/singletons/n"+str(net)+"/1/"
		output_without_singletons="/home/amaury/communities_hashmap/"+str(graphs)+"/"+str(alg)+"/without_singletons/n"+str(net)+"/1/"
			
		if not os.path.isdir(source_dir):
			print ("\nDiretório não encontrado "+str(source_dir))
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
				if not os.path.exists(source_dir+str(file)):
					print ("Diretório não encontrado: "+str(source_dir)+str(file))
				else:	
					i+=1
					print (str(graphs)+" - Verificando singletons para a - rede: "+str(net)+" - ego: "+str(i)+": "+str(file))
					
					j=0	
					with open(source_dir+str(file), 'r') as f:							# Abre o arquivo gerado pelo algoritmo para o usuário "file"
						ego_id = file.split(".pajek")											# pegar o nome do arquivo que indica o threshold analisado
						ego_id = str(ego_id[0])
										
						for line in f:
							j+=1
							if j > 7:
								b = line.split(': ')
								a = b[1].split(' ')
								with open(output_full+ego_id+".txt", 'a+') as g:
									for item in a:
										if item != "\n":
											if long(item) > 0:
												item = long(item)												
												g.write(str(item)+" ")										# Escreve os ids das Listas separadas por espaço
											else:
												print ("deu ruim "+str(item))	
									g.write("\n")															# Passa para a próxima linha de g
	
								if len(a) > 1:
									with open(output_without_singletons+ego_id+".txt", 'a+') as g:
										for item in a:
											if item != "\n":
												if long(item) > 0:
													item = long(item)																																				
													g.write(str(item)+" ")									# Escreve os ids das Listas separadas por espaço
										g.write("\n")														# Passa para a próxima linha
								else:
									with open(output_singletons+ego_id+".txt", 'a+') as g:
										for item in a:
											if item != "\n":
												if long(item) > 0:
													item = long(item)												
													g.write(str(item)+" ")									# Escreve os ids das Listas separadas por espaço
										g.write("\n")														
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
	alg = "gn"
	save_data(graphs1,alg)
	save_data(graphs2,alg)
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
	
if __name__ == "__main__": main()
