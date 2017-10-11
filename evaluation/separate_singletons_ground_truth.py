	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Receber o conjunto de conjunto de comunidades e o ground_truth e separar em conjunto completo e conjunto sem singletons.
##								
## # INPUT:
##		- Arquivos com as comunidades completas
## # OUTPUT:
##		- Arquivos com as comunidades sem singletons
######################################################################################################################################################################

######################################################################################################################################################################
#
# Salva os dados de cada algoritmo em formato JSON
#
######################################################################################################################################################################
def save_data(data,graph_type,metric,algorithm):
	print
	print ("Salvando dados... FUNÇÃO EM DESENVOLVIMENTO!")
	print
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')	
	if os.path.isdir(source_dir):	
		i=0												
		for file in os.listdir(source_dir):									# Para cada arquivo no diretório
			i+=1
			ego = file.split(".txt")											# pegar o nome do arquivo que indica o threshold analisado
			ego = int(ego[0])			
			with open(source_dir+file, 'r') as f:
				print ("Verificando singletons para o ego: "+str(i))
				if os.path.isfile(output_without_singletons+file):		# Removendo arquivos antigos...
					os.remove(output_without_singletons+file)
				if os.path.isfile(output_singletons+file):
					os.remove(output_singletons+file)				
				for line in f:
					a = line.split(' ')
					if len(a) > 2:
						with open(output_without_singletons+file, 'a+') as g:
							for item in a:
								if item != "\n": 
									g.write(str(item)+" ")										# Escreve os ids das Listas separadas por espaço
							g.write("\n")														# Passa para a próxima linha
					else:			
						with open(output_singletons+file, 'a+') as g:
							for item in a:
								if item != "\n":
									g.write(str(item)+" ")										# Escreve os ids das Listas separadas por espaço
							g.write("\n")														# Passa para a próxima linha								
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
source_dir="/home/amaury/dataset/ground_truth/lists_users_TXT/"
output_singletons="/home/amaury/dataset/ground_truth/lists_users_TXT_singletons/"
output_without_singletons="/home/amaury/dataset/ground_truth/lists_users_TXT_without_singletons/"

if not os.path.exists(output_singletons):		
	os.makedirs(output_singletons)
if not os.path.exists(output_without_singletons):
	os.makedirs(output_without_singletons)
	
if __name__ == "__main__": main()