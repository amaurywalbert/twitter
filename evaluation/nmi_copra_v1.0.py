# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular NMI
##								
## # INPUT: Arquivos com as comunidades detectadas e o ground truth 
## # OUTPUT:
##		- Arquivos com os índices NMI
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def nmi_copra(communities,output,singletons,net,ground_truth):
	
	communities = communities+singletons+"/"+net+"/"
	ground_truth = ground_truth+singletons+"/"
	output = output+singletons+"/"+net+"/"
	if not os.path.exists(output):
		os.makedirs(output)

	print ("Os arquivos serão armazenados em: "+str(output))
	print("######################################################################")
	for threshold in range(20):	#Parâmetro do COPRA
		threshold+=1
		i=0 		#Ponteiro para o ego
		if os.path.isdir(str(communities)+str(threshold)):
			print("######################################################################")
			with open(str(output)+"/"+str(threshold)+".txt", 'w') as f:
				for file in os.listdir(str(communities)+str(threshold)):
					i+=1
					ego_file = file.split(".edge_list")											# pegar o nome do arquivo que indica o threshold analisado
					ego_file = ego_file[0]
					ego_file = ego_file.split("clusters-")			
					ego_file = ego_file[1]
				
					if os.path.isfile(str(ground_truth)+str(ego_file)+".txt"):
						print ("Calculando NMI para a rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" -  ego: "+str(i))
						execute = subprocess.Popen(["/home/amaury/algoritmos/Metricas/mutual3/mutual", str(communities)+str(threshold)+"/"+str(file),str(ground_truth)+str(ego_file)+".txt"], stdout=subprocess.PIPE)
						f.write(execute.communicate()[0])
					else:
						print ("ERROR - EGO: "+str(i)+" - Arquivo não encontrado!")
				print("######################################################################")
		else:
			print ("Diretório não encontrado: "+str(communities)+str(threshold))
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
	print "##########################################################################"
	print"																									"
	print" Algoritmo para cálculo da métrica NMI para resultados do algoritmo COPRA	"
	print"																									"
	print"###########################################################################"
	print
	print"Realizar o cálculo usando Singletons?"
	print 
	print" 01 - SIM"
	print" 02 - NÃO"
	print
	op = int(raw_input("Escolha uma opção acima: "))
	if op == 01:
		singletons = "full"
	elif op == 02:
		singletons = "without_singletons"
	else:
		singletons = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
#######################################################################
#######################################################################
	print("######################################################################")	
	for i in range(10):
		i+=1
		net = "n"+str(i)
		print ("Calculando NMI nas comunidades detectadas na rede: "+str(net)+" - SEM o ego")
		nmi_copra(communities1,output1,singletons,net,ground_truth)
		print ("Calculando NMI nas comunidades detectadas na rede: "+str(net)+" - COM o ego")
		nmi_copra(communities2,output2,singletons,net,ground_truth)
	print("######################################################################")
	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
#####Alterar as linhas para Dropbox quando executado em ambiente de produção
ground_truth = "/home/amaury/dataset/ground_truth/lists_users_TXT/"
communities1 = "/home/amaury/communities/graphs_with_ego/copra/"
communities2 = "/home/amaury/communities/graphs_without_ego/copra/" 
output1 = "/home/amaury/Dropbox/evaluation/graphs_with_ego/copra/nmi/"
output2 = "/home/amaury/Dropbox/evaluation/graphs_without_ego/copra/nmi/"
######################################################################################################################


if __name__ == "__main__": main()