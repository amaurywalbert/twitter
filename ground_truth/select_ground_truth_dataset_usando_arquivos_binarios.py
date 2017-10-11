# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script que percorre o conjunto de Listas coletadas ques está em formato binário e adiciona os membros e inscritos nas listas de cada ego em um arquivo nomeado pelo ID do ego
##									onde cada linha representa uma Lista do Twitter.
##								Já salva os ids das listas para cada ego em formato JSON - tudo misturado (as que ele é dono e as que ele está inscrito)
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids das listas
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		lists_ids = []
		while f.tell() < tamanho:
			buffer = f.read(list_struct.size)
			user = list_struct.unpack(buffer)
			lists_ids.append(user[0])
	return lists_ids

######################################################################################################################################################################
#
# Converte formato data para armazenar em formato JSON
#
######################################################################################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object
        
######################################################################################################################################################################
#
# Grava o erro num arquivo específco 
#
######################################################################################################################################################################
def save_error(user,reason):
	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	error={}
	with open(error_dir+str(user)+".err", "w") as outfile:													# Abre o arquivo para gravação no final do arquivo
		error = {'reason':str(reason) ,'date':agora}
		outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
	print error

######################################################################################################################################################################
#
# Salva as informações das listas do ego em formato de comunidades - Arquivo texto onde cada linha representa uma Lista (comunidade) do Twitter
#
######################################################################################################################################################################
def save_ground_truth(ego,i,lists_ids):
	if not os.path.isfile(output_ground_truth_txt+str(ego)+".txt"):
		print ("Ego nº "+str(i)+" - Localizando membros e inscritos")
		n=0
	 	for list_id in lists_ids:
			n+=1
			print ("Buscando por membros e inscritos da lista "+str(n)+"/"+str(len(lists_ids)))
			list_ground_truth = set()
			if os.path.isfile(members_lists_collected+str(list_id)+".dat"):
				list_members_users = read_arq_bin(members_lists_collected+str(list_id)+".dat")
				if list_members_users is not None:
					list_ground_truth.update(list_members_users)
						
			if os.path.isfile(subs_lists_collected+str(list_id)+".dat"):
				list_subs_users = read_arq_bin(subs_lists_collected+str(list_id)+".dat")	
				if list_subs_users is not None:
						list_ground_truth.update(list_subs_users)
		##################################################### Salvando Arquivo TXT #####################################################	
			try:		
				with open(output_ground_truth_txt+str(ego)+".txt", 'a+') as f:
					if list_ground_truth is not None:									# Verifica se a Lista não está vazia
						for item in list_ground_truth:									# 
							f.write(str(item)+" ")											# Escreve os ids das Listas separadas por espaço
						f.write("\n")															# Passa para a próxima linha
			except Exception as e:	
				save_error(ego,str(e))
				if os.path.exists(output_ground_truth_txt+str(ego)+".txt"):
					os.remove(output_ground_truth_txt+str(ego)+".txt")
					print ("Erro - Ego nº "+str(i)+" - Arquivo TXT removido com sucesso...")

		##################################################### Salvando Arquivo JSON #####################################################
			try:		
				with open(output_ground_truth_json+str(ego)+".json", 'a+') as f:
					if list_ground_truth is not None:									# Verifica se a Lista não está vazia
						f.write(json.dumps(list(list_ground_truth)))
						
			except Exception as e2:	
				save_error(ego,str(e2))
				if os.path.exists(output_ground_truth_json+str(ego)+".json"):
					os.remove(output_ground_truth_json+str(ego)+".json")
					print ("Erro - Ego nº "+str(i)+" - Arquivo JSON removido com sucesso...")

	else:
		print ("Ego nº "+str(i)+" - Membros e Inscritos já coletados - Ignorando...")						
	print("\n######################################################################")			

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	i = 0		# Ego verificado	
	for file in os.listdir(fonte):
		i+=1
		ego = file.split(".dat")
		ego = long(ego[0])
		lists_ids = read_arq_bin(fonte+file)
		save_ground_truth(ego,i,lists_ids)
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
fonte = "/home/amaury/dataset/ground_truth/bin/"															#Lista de egos... qualquer rede no dataset serviria.
output_ground_truth_txt = "/home/amaury/dataset/ground_truth/lists_users_TXT_of_bin/full/"			# Diretório que armazenará as comunidades em formato TXT
output_ground_truth_json = "/home/amaury/dataset/ground_truth/lists_users_JSON_of_bin/full/"		# Diretório que armazenará as comunidades em formato JSON tudo misturado (as que o ego é o dono e as que ele está inscrito)
error_dir = "/home/amaury/dataset/ground_truth/lists_users_JSON_of_bin_ERROR/"					# Diretório que armazenará erros na formatação das listas.
######################################################################################################################
lists_set = "/home/amaury/coleta/users_lists/ego_lists_overview_full.json"							# Arquivo que contém o conjunto de listas de cada ego. 
members_lists_collected = "/home/amaury/coleta/ground_truth/members_lists_collected/bin/" 	# Diretório que contém o conjunto de listas COLETADAS de cada ego.
subs_lists_collected = "/home/amaury/coleta/ground_truth/subscribers_lists_collected/bin/" 	# Diretório que contém o conjunto de listas COLETADAS de cada ego. 
######################################################################################################################
formato = 'l'																											# Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) 																			# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_ground_truth_txt):
	os.makedirs(output_ground_truth_txt)
if not os.path.exists(output_ground_truth_json):
	os.makedirs(output_ground_truth_json)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)	
#Executa o método main
if __name__ == "__main__": main()