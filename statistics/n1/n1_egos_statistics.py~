# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
import powerlaw
import seaborn as sns

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Exibe estatísticas do ego.
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		friends_list = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_list.append(friend[0])
	return friends_list

######################################################################################################################################################################
# Powerlaw
######################################################################################################################################################################
def powerlaw_print(data,i):
	print ("PowerLaw\n")
	results = powerlaw.Fit(data) 
	print results.power_law.alpha 
	print results.power_law.xmin 
	R, p = results.distribution_compare('power_law', 'lognormal')
	#	plt.xlim([0, num_egos])
	powerlaw.plot_pdf(data)

######################################################################################################################################################################
# Seaborn
######################################################################################################################################################################
def seaborn_print(data,i):
	print ("Seaborn\n")
	sns.distplot(data, kde=False, rug=False,label=str(i))
	#	plt.xlim([0, num_egos])
	sns.plt.savefig(output_dir+str(qtde_egos)+"_seaaborn_"+str(num_egos)+".png")
#	sns.plt.show()
	
######################################################################################################################################################################
# Plot and Save
######################################################################################################################################################################
def plot_and_save(data,i):
	print ("Plot and Save\n")
	plt.hist(data, normed=0, facecolor='green', alpha=0.75)
#	plt.hist(data,label=str(i)+" egos")
	plt.xlabel ("Friends")
#	plt.xlim([0, num_egos])
	plt.ylabel ("Egos")
	plt.title ("Número de amigos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+str(qtde_egos)+"_plot_"+str(num_egos)+".png")
#	plt.show()

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	statistics={}
	n_users=[]
	n_friends=[]
	i=0
	for file in os.listdir(data_dir):
		friends_list = read_arq_bin(data_dir+file) # Função para converter o binário de volta em string em formato json.
		if friends_list:
			i+=1
			user_id = file.split(".dat")
			user_id = long(user_id[0])
			statistics[user_id] = {'n_of_friends':len(friends_list)}
			n_friends.append(statistics[user_id]['n_of_friends'])
	plot_and_save(n_friends,i)
	seaborn_print(n_friends,i)
#	powerlaw_print(n_friends,i)
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full' 		#10, 50, 100, 500 ou full
num_egos = 10000
######################################################################################################################
data_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"
output_dir =  "/home/amaury/statistics/n1/"
formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()