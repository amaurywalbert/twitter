# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - verifica se os alters (amigos dos egos) já foram coletados e copia os arquivos deles para o diretório correto
##									Esse processo é apenas para agilizar e organizar os diretórios já coletados.
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
		alters_list = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			alter = user_struct.unpack(buffer)
			alters_list.append(alter[0])
	return alters_list

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	i = 0		# Ego verificado	
	j = 0		# Quantidade de arquivos copiados 
	k = 0		# Quantidade de arquivos não encontrados
	
	for file in os.listdir(fonte):
		n_alters_missing = 0		# Quantidade de arquivos não encontrados por ego	
		ego_id = file.split(".dat")
		ego_id = long(ego_id[0])
		alters_list = read_arq_bin(fonte+file) # Função para converter o binário de volta em string em formato json.
		if alters_list:
			for alter in alters_list:				
				user = long(alter)
				if not dictionary.has_key(user):
					if os.path.isfile(origem+str(user)+".dat"):
						shutil.copy(origem+str(user)+".dat",destino)
						dictionary[user] = user
						j+=1
#						print (str(j)+" - Arquivo copiado com sucesso!")						
					else:
						n_alters_missing+=1		# Quantidade de arquivos não encontrados por ego
						k+=1
		i+=1
		print ("Ego nº: "+str(i)+" - Verificado!")
		egos_overview={}
		with open(egos_output, "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			egos_overview = {'ego':ego_id,'n_alters_missing':n_alters_missing}
			outfile.write(json.dumps(egos_overview,separators=(',', ':'))+"\n")								

	with open(full_output, "a+") as outfile:								# Abre o arquivo para gravação
		full_overview = {'files_in_dir':len(dictionary),'missing_files':k}
		outfile.write(json.dumps(full_overview, separators=(',', ':')))

	print ("Arquivos copiados: "+str(j))
	print ("Arquivos no diretório: "+str(len(dictionary)))
	print ("Arquivos faltando: "+str(k))
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
fonte = "/home/amaury/dataset/n1/egos_limited_5k/bin/"
origem = "/home/amaury/coleta/n1/alters_friends/full/bin/"

destino = "/home/amaury/dataset/n1/alters/bin/"

egos_output = "/home/amaury/dataset/n1/alters/egos_overview.json"
full_output = "/home/amaury/dataset/n1/alters/full_overview.json"

formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário


#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino):
	os.makedirs(destino)

if os.path.isfile(egos_output):
	os.remove(egos_output)
	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
for file in os.listdir(destino):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")

#Executa o método main
if __name__ == "__main__": main()