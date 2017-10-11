# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script que percorre a o conjunto de egos do dataset e seleciona e armazena suas listas em formato JSON separados por Ownership e Subscriptions.
##								- Também percorre o conjunto de Listas coletadas e adiciona os membros e inscritos nas listas de cada ego em um arquivo nomeado pelo ID do ego
##									onde cada linha representa uma Lista do Twitter
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
# Obtem as listas já coletadas do ego
#
######################################################################################################################################################################
def get_lists(ego,i):
	if not os.path.isfile(output_json+str(ego)+".json"):
		try:
			egos_lists_ownership = []
			egos_lists_subscription = []
			with open(lists_set, 'r') as lists_file:
				for line in lists_file:
					lists = json.loads(line)
					if ego == long(lists['user']):
						print ("Ego nº "+str(i)+" - Encontrado! Localizando listas...")
						for list in lists['owner']:
							egos_lists_ownership.append(list['id'])
						for list in lists['subscriptions']:
							egos_lists_subscription.append(list['id'])	
			lists_ego = {}
			lists_ego = {'owner':egos_lists_ownership, 'subs':egos_lists_subscription}
			with open(output_json+str(ego)+".json", 'w') as f:
				json.dump(lists_ego, f)				
			print ("Ego nº "+str(i)+" - Lists Ownership: "+str(len(egos_lists_ownership))+" - Lists Subscription: "+str(len(egos_lists_subscription))+" - Arquivo JSON salvo com sucesso!")
			m = len(egos_lists_ownership)+len(egos_lists_subscription)		
			if m < 2:
				print ("Ego nº "+str(i)+" - Número de LISTAS inferior a 2: "+str(m))
				shutil.copy(output_json+str(ego)+".json", output_json_fail+str(ego)+".json")
			return egos_lists_ownership,egos_lists_subscription
		except Exception as e:	
			save_error(ego,str(e))
			if os.path.exists(output_ground_truth+str(ego)+".txt"):
				os.remove(output_ground_truth+str(ego)+".txt")
				print ("Erro - Ego nº "+str(i)+" - Arquivo JSON removido com sucesso...")		
	else:
		print ("Ego nº "+str(i)+" - Listas já encontradas - Ignorando...")


######################################################################################################################################################################
#
# Salva as informações das listas do ego em formato de comunidades - Arquivo texto onde cada linha representa uma Lista (comunidade) do Twitter
#
######################################################################################################################################################################
def save_ground_truth(ego,i):
	if not os.path.isfile(output_ground_truth+str(ego)+".txt"):
		with open(output_json+str(ego)+".json", "r") as f:
			lists_ego = json.load(f)
			egos_lists_ownership = lists_ego['owner']
			egos_lists_subscription = lists_ego['subs']
			try:
				print ("Ego nº "+str(i)+" - Localizando membros e inscritos")
				n=0
				for list in egos_lists_ownership:
					n+=1
					print ("OWNERSHIP - Buscando por membros e inscritos da lista "+str(n)+"/"+str(len(egos_lists_ownership)))
					list_ground_truth_owner = set()
				
					if os.path.isfile(members_lists_collected+str(list)+".dat"):
						list_members_users = read_arq_bin(members_lists_collected+str(list)+".dat")
						if list_members_users is not None:
							list_ground_truth_owner.update(list_members_users)
						
					if os.path.isfile(subs_lists_collected+str(list)+".dat"):
						list_subs_users = read_arq_bin(subs_lists_collected+str(list)+".dat")	
						if list_subs_users is not None:
							list_ground_truth_owner.update(list_subs_users) 

					with open(output_ground_truth+str(ego)+".txt", 'a+') as f:
						if list_ground_truth_owner is not None:
							for item in list_ground_truth_owner:
								f.write(str(item)+" ")
							f.write("\n")	
				n=0
				for list in egos_lists_subscription:
					n+=1
					print ("SUBSCRIPTION - Buscando por membros e inscritos da lista "+str(n)+"/"+str(len(egos_lists_subscription)))		
					list_ground_truth_subs = set()
		
					if os.path.isfile(members_lists_collected+str(list)+".dat"):
						list_members_users = read_arq_bin(members_lists_collected+str(list)+".dat")
						if list_members_users is not None:
							list_ground_truth_subs.update(list_members_users)
		
					if os.path.isfile(subs_lists_collected+str(list)+".dat"):
						list_subs_users = read_arq_bin(subs_lists_collected+str(list)+".dat")	
						if list_subs_users is not None:
							list_ground_truth_subs.update(list_subs_users)
		
					with open(output_ground_truth+str(ego)+".txt", 'a+') as f:
						if list_ground_truth_subs is not None:
							for item in list_ground_truth_subs:
								f.write(str(item)+" ")
							f.write("\n")
			except Exception as e:	
				save_error(ego,str(e))
				if os.path.exists(output_ground_truth+str(ego)+".txt"):
					os.remove(output_ground_truth+str(ego)+".txt")
					print ("Erro - Ego nº "+str(i)+" - Arquivo TXT removido com sucesso...")
					
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
		get_lists(ego,i)
		save_ground_truth(ego,i)
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
fonte = "/home/amaury/dataset/n2/egos/bin/"																	# Lista de egos... qualquer rede no dataset serviria.
output_json = "/home/amaury/dataset/ground_truth/egos_lists_json/full/"								# Diretório com arquivos JSON com id das listas quem o ego é o dono ou está insctrito.
output_json_fail = "/home/amaury/dataset/ground_truth/egos_lists_json_fail/"						# Diretório com arquivos JSON com id das listas quem o ego é o dono ou está insctrito mas que contém menos de 02 listas.
output_ground_truth = "/home/amaury/dataset/ground_truth/lists_users_TXT_of_JSON/full/"		# Diretório que armazenará as comunidades
error_dir = "/home/amaury/dataset/ground_truth/lists_users_TXT_of_JSON_ERROR/"															# Diretório que armazenará erros na formatação das listas.
######################################################################################################################
lists_set = "/home/amaury/coleta/users_lists/ego_lists_overview_full.json"							# Diretório que contém o conjunto de listas de cada ego. 
members_lists_collected = "/home/amaury/coleta/ground_truth/members_lists_collected/bin/" 	# Diretório que contém o conjunto de listas COLETADAS de cada ego.
subs_lists_collected = "/home/amaury/coleta/ground_truth/subscribers_lists_collected/bin/" 	# Diretório que contém o conjunto de listas COLETADAS de cada ego. 
######################################################################################################################
formato = 'l'																											# Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) 																			# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(output_json):
	os.makedirs(output_json)
if not os.path.exists(output_ground_truth):
	os.makedirs(output_ground_truth)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)	
	
#Executa o método main
if __name__ == "__main__": main()