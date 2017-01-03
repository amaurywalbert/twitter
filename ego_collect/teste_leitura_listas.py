# -*- coding: latin1 -*-
################################################################################################
# Script para testar a leitura das listas armazenadas
#
import tweepy, datetime, sys, time, json, os.path, shutil, time

reload(sys)
sys.setdefaultencoding('utf-8')


##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810


################################################################################################
##		Nota - As listas estão sendo salvas em um formato estruturado.
##
##		Teste 0 É possível ler o conteudo de cada campo lendo o arquivo e acessando list.campo. Ex. list.id, list.name??
################################################################################################

################################################################################################
#
# Obtem as listas de um usuário específico (owner+subscription)
#
################################################################################################

def search_lists(user):
	print("Exibindo listas do usuário: "+str(user))
	try:
		lists = []
		i = 0
		datafile = open("data/lists_info.txt", 'r')							# Arquivo com informações das listas salvas
		lists_info = datafile.readlines()
		for line in lists_info:
			if str(user) == line.id:
				print (line.id,line.user,line.user_count)
				i = i+1
		if i < 1:
			print (str(user)+" não possui listas!")
	
		lists_info.close()
	
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		lists_err = open("test/lists_collect.lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		lists_err.writelines(str(agora)+"[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+".\n")
		lists_err.close()
		print("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")

		

##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	try:
		shutil.copyfile('data/ego_list.txt', 'test/ego_collect.txt')
		
	except:
		print ("Impossível abrir arquivos!")
		sys.exit()
	ego_collect = open('test/ego_collect.txt','r')	
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		account = ego_collect.readline()													#Leia scren_name do usuário corrente		
		if (account == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True
		else:
			print("####################################################################################################")			
			search_lists(account)																#Inicia função de busca das listas
			print("####################################################################################################")
	ego_collect.close()
	print	
	print("Pesquisa finalizada!")
	
	

################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################


# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()