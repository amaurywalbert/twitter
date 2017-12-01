# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Coletar a modularidade da rede calculada durante o processo de detecçao de comunidades com o software 	
##					http://deim.urv.cat/~sergio.gomez/radatools.php#download
##								
## # INPUT:
##		- Arquivos com as comunidades completas
## # OUTPUT:
##		- Arquivos com a modularidade para cada rede.
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
			
		output = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/modularity_gn/"+str(graphs)+"/" # Aqui não tem without singletons pq o algoritmo calcula a modularidade para a rede.... aliás preciso ver se isso aqui não seria a qualidade da rede.
			
		if not os.path.isdir(source_dir):
			print ("\nDiretório não encontrado "+str(source_dir))
			print
		else:	
			if os.path.exists(output):
				shutil.rmtree(output)		
				os.makedirs(output)	
			else:
				os.makedirs(output)

			i=0
			modularity=[]
			for file in os.listdir(source_dir):					
				if not os.path.exists(source_dir+str(file)):
					print ("Diretório não encontrado: "+str(source_dir)+str(file))
				else:	
					print (str(graphs)+" - Verificando singletons para a - rede: "+str(net)+" - ego: "+str(i)+": "+str(file))
					i+=1
					j=0
					with open(source_dir+str(file), 'r') as f:							# Abre o arquivo gerado pelo algoritmo para o usuário "file"
						for line in f:
							j+=1
							if j == 3:
								a = line.split('= ')
								m = float(a[1])
								modularity.append(m)
			with open(str(output)+"n"+str(net)+".json", 'w') as f:
				f.write(json.dumps(modularity)+"\n")		
									
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
