# -*- coding: latin1 -*-
########################################################################
#Script para fazer parser dos arquivos JSON
#Argumentos
#1 - Nome do arquivo de entrada
#2 - Código do Local
#	1 - Goiânia
#	2 - São Paulo
#	3 - Salvador
#	4 - Rio Verde
#	5 - Catalão
#
#
#Ajustes da versão 02:
#
#OK - Manter o contador mas nao usar no dicionário... tá estourando a memória. Deixar apenas para contar linhas...
#OK - Uso do bloco TRY para ignorar erro de parser de Tweets "corrompidos" ou incompletos.
#OK - import time    -		time.strftime('%Y-%m-%d %H:%M:%S') pra armazenar a data de escrita do tweet no BD
#OK - Só pode inserir dados das tabelas entidades e location depois de inserir o tweet...
#OK - Filtro que elimina duplicade em tweets com código de local = "country" (id_place = Brasil)
#OK - Cria arquivos contendo códigos de erros de inserção no BD para possível geração de estatísticas.
#
import json, mysql.connector, sys, os.path, time
from mysql.connector import errorcode
from pprint import pprint

#############################################################################################################################
#############################################################################################################################

def valida_parametros(arquivo):
	if not os.path.isfile(arquivo):
		print "Arquivo não encontrado!"
		sys.exit()
	else:
		print " 1 - Goiânia"
		print " 2 - São Paulo"
		print " 3 - Salvador"
		print " 4 - Rio Verde"
		print " 5 - Catalão"
		op = raw_input("Escolha uma região: ")
		for letra in opcoes:
			if op not in opcoes:
				print "Região Inválida!"
				sys.exit()
	return(op)
	print "Iniciando..."


#############################################################################################################################
#############################################################################################################################

opcoes = "12345"
regiao = valida_parametros(sys.argv[1]) 

#############################################################################################################################
#############################################################################################################################

#contador
i = 0
#############################################################################################################################
#############################################################################################################################

try:
	cnx = mysql.connector.connect(user="twitter", password="roma031205", host="127.0.0.1", database="twitter")
#Ler arquivo JSON
	file = open(sys.argv[1])
#############################################################################################################################
#############################################################################################################################
#Realizar parser	
	for line in file:
		try:			
			tweet = json.loads(line, strict=False) #é pra tentar evitar o erro de delimitador...
#user			
			user_iduser = tweet['user']['id']
			user_created_at = tweet['user']['created_at']			
			user_description = unicode(tweet['user']['description'])
			user_favourites_count = tweet['user']['favourites_count']
			user_followers_count = tweet['user']['followers_count']
			user_following = tweet['user']['following']
			user_friends_count = tweet['user']['friends_count']
			user_geo_enabled = tweet['user']['geo_enabled']
			user_lang = tweet['user']['lang']
			user_listed_count = tweet['user']['listed_count']
			user_location = tweet['user']['location']
			user_name = unicode(tweet['user']['name'])
			user_profile_image_url = tweet['user']['profile_image_url']
			user_screen_name = tweet['user']['screen_name']
			user_statuses_count = tweet['user']['statuses_count']
			user_time_zone = tweet['user']['time_zone']
			user_url = tweet['user']['url']
#tweet
			tweet_idtweet = tweet['id']
			tweet_contributors = tweet['contributors']
			tweet_coordinates = tweet['coordinates']
			if tweet_coordinates:
				tweet_geo_latitude = tweet['coordinates']['coordinates'][0]
				tweet_geo_longitude = tweet['coordinates']['coordinates'][1]
			else:
				tweet_geo_latitude = tweet['coordinates']
				tweet_geo_longitude = tweet['coordinates']
			tweet_created_at = tweet['created_at']
			tweet_favorite_count = tweet['favorite_count']
			tweet_favorited = tweet['favorited']
			tweet_filter_level = tweet['filter_level']
			tweet_in_reply_to_status_id = tweet['in_reply_to_status_id']
			tweet_in_reply_to_user_id = tweet['in_reply_to_user_id']
			tweet_is_quote_status = tweet['is_quote_status']
			tweet_lang = tweet['lang']
			tweet_retweet_count = tweet['retweet_count']
			tweet_retweeted = tweet['retweeted']
			tweet_source = tweet['source']
			tweet_text = tweet['text']
			tweet_timestamp_ms = tweet['timestamp_ms']
			tweet_truncated = tweet['truncated']
			tweet_timestamp_db = time.strftime('%Y-%m-%d %H:%M:%S')
			tweet_iduser_fk = tweet['user']['id']
			tweet_idregion_fk = regiao
#entities	
			entities_idtweet_fk = tweet['id']
			entities_hashtags_full = ';'.join(map(str, tweet['entities']['hashtags']))			
			entities_symbols_full = ';'.join(map(str, tweet['entities']['symbols']))
			entities_urls_full = ';'.join(map(str, tweet['entities']['urls']))
			entities_user_mentions_full = ';'.join(map(str, tweet['entities']['user_mentions']))
#place
			place_idtweet_fk = tweet['id']
			place_bounding_box_full = tweet['place']['bounding_box']['coordinates']	
			if place_bounding_box_full:
				place_bounding_box = ','.join(map(str, place_bounding_box_full[0][0])) + ';' + ','.join(map(str, place_bounding_box_full[0][1])) + ';' + ','.join(map(str, place_bounding_box_full[0][2])) + ';' +','.join(map(str, place_bounding_box_full[0][3]))   
			else:
				place_bounding_box = tweet['place']['bounding_box']['coordinates']	
			place_country = tweet['place']['country']
			place_country_code = tweet['place']['country_code']
			place_full_name = tweet['place']['full_name']
			place_id_place = tweet['place']['id']
			place_name = tweet['place']['name']
			place_place_type = tweet['place']['place_type']
			place_url = tweet['place']['url']

#############################################################################################################################
#############################################################################################################################
##########inserir dados no Banco
			if place_id_place == '1b107df3ccc0aaa1': #OK - Filtro que elimina duplicade em tweets com código de local = "country" (id_place = Brasil)
				try:
					err_id_place = open(sys.argv[1] + '.err_id_place', 'a+') # Abre o arquivo para gravação no final do arquivo
					err_id_place.writelines("Linha " + str(i) + ". Ignorando tweet... idplace = " + place_id_place + " (" + place_full_name +")\n")
					err_id_place.close()				
				
					#print("Linha " + str(i) + ". Ignorando tweet... idplace = " + place_id_place + " (" + place_full_name +")") #Imprime na tela mensagem de erro de id_place na tela...
				except IOError:
					print("Erro ao abrir o arquivo!\n")

			else:

#############Tabela USER
				try:
					cursor = cnx.cursor()
					add_user = ("INSERT INTO USER VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")				
					cursor.execute(add_user, (user_iduser, user_created_at, user_description, user_favourites_count, user_followers_count, user_following, user_friends_count, user_geo_enabled, user_lang, user_listed_count, user_location, user_name, user_profile_image_url, user_screen_name, user_statuses_count, user_time_zone, user_url))
					cnx.commit()
				except Exception as erro:
					err_id_user = open(sys.argv[1] + ".err_id_user", "a+") # Abre o arquivo para gravação no final do arquivo
					err_id_user.writelines("Linha " + str(i) + ". Erro MySQL - Table USER: {}\n".format(erro))
					err_id_user.close()				
					print("Linha " + str(i) + ". Erro MySQL - Table USER: {}".format(erro))

#############Tabela TWEET							
				try:
					cursor = cnx.cursor()
					add_tweet = ("INSERT INTO TWEET VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
					cursor.execute(add_tweet, (tweet_idtweet, tweet_contributors, tweet_geo_latitude, tweet_geo_longitude, tweet_created_at, tweet_favorite_count, tweet_favorited, tweet_filter_level, tweet_in_reply_to_status_id, tweet_in_reply_to_user_id, tweet_is_quote_status, tweet_lang, tweet_retweet_count, tweet_retweeted, tweet_source, tweet_text, tweet_timestamp_ms, tweet_truncated, tweet_timestamp_db, tweet_iduser_fk, tweet_idregion_fk))
					cnx.commit()
#############Tabela ENTITIES
					try:
						cursor = cnx.cursor()
						add_entities = ("INSERT INTO ENTITIES (entities_idtweet_fk, entities_hashtags, entities_symbols, entities_urls, entities_user_mentions) VALUES (%s, %s, %s, %s,%s)")
						cursor.execute(add_entities, (entities_idtweet_fk, entities_hashtags_full, entities_symbols_full, entities_urls_full, entities_user_mentions_full))
						cnx.commit()
					except Exception as erro:
						err_id_entities = open(sys.argv[1] + ".err_id_entities", "a+") # Abre o arquivo para gravação no final do arquivo
						err_id_entities.writelines("Linha " + str(i) + ". Erro MySQL - Table ENTITIES: {}\n".format(erro))
						err_id_entities.close()										
						print("Linha " + str(i) + ". Erro MySQL - Table ENTITIES: {}".format(erro))
#############Tabela PLACE			
					try:
						cursor = cnx.cursor()
						add_place = ("INSERT INTO PLACE (place_idtweet_fk, place_bounding_box, place_country, place_country_code, place_full_name, place_id_place, place_name, place_place_type, place_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")				
						cursor.execute(add_place, (place_idtweet_fk, place_bounding_box, place_country, place_country_code, place_full_name, place_id_place, place_name, place_place_type, place_url))
						cnx.commit()
					except Exception as erro:
						err_id_place = open(sys.argv[1] + ".err_id_place", "a+") # Abre o arquivo para gravação no final do arquivo
						err_id_place.writelines("Linha " + str(i) + ". Erro MySQL - Table PLACE: {}\n".format(erro))
						err_id_place.close()										
						print("Linha " + str(i) + ". Erro MySQL - Table PLACE: {}".format(erro))		
				
				except Exception as erro:
					err_id_tweet = open(sys.argv[1] + ".err_id_tweet", "a+") # Abre o arquivo para gravação no final do arquivo
					err_id_tweet.writelines("Linha " + str(i) + ". Erro MySQL - Table TWEET: {}\n".format(erro))
					err_id_tweet.close()										
					print("Linha " + str(i) + ". Erro MySQL - Table TWEET: {}".format(erro))
			#Fim Else
			
		except Exception as erro_parser:
			err_parser = open(sys.argv[1] + ".err_parser", "a+") # Abre o arquivo para gravação no final do arquivo
			err_parser.writelines("Linha " + str(i) + ". Erro no parser do arquivo JSON: {}\n".format(erro_parser))
			err_parser.close()										
			print("Linha " + str(i) + ". Erro no parser do arquivo JSON: {}".format(erro_parser))
#############################################################################################################################
#############################################################################################################################
		i = i+1	
#############################################################################################################################
#############################################################################################################################
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Algo errado com usuário ou senha!")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe!")
	else:
		print(err)
else:
	cnx.close()