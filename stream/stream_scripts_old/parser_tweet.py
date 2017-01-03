# -*- coding: latin1 -*-
#
#Argumentos
#1 - Nome do arquivo de entrada
#2 - Código do Local
#	1 - Goiânia
#	2 - São Paulo
#	3 - Salvador
#	4 - Rio Verde
#	5 - Catalão
#
########################################################################
#Script para fazer parser dos arquivos JSON
import json
import mysql.connector
import sys
from mysql.connector import errorcode
# Import library which can print parsed data  
from pprint import pprint

#tabela
tweet = []

#Colunas
idtweet = []
contributors = []
coordinates = []
geo_latitude = []
geo_longitude = []
created_at = []
favorite_count = []
favorited = []
filter_level = []
in_reply_to_status_id = []
in_reply_to_user_id = []
is_quote_status = []
lang = []
retweet_count = []
retweeted = []
source = []
text = []
timestamp_ms = []
truncated = []
iduser_fk = []
idregion_fk = []


#contador
i = 0

##########################################################################################################
try:
	cnx = mysql.connector.connect(user='twitter', password='roma031205', host='127.0.0.1', database='twitter')

#Ler arquivo JSON
	file = open(sys.argv[1]) #Verificar como concatenar arquivos em Python...

	try:
		for line in file:
			tweet.append(json.loads(line))

			idtweet.append(tweet[i]['id'])
			contributors.append(tweet[i]['contributors'])
			coordinates.append(tweet[i]['coordinates'])
			if coordinates[i]:
				geo_latitude.append(tweet[i]['coordinates']['coordinates'][0])
				geo_longitude.append(tweet[i]['coordinates']['coordinates'][1])
			else:
				geo_latitude.append(tweet[i]['coordinates'])
				geo_longitude.append(tweet[i]['coordinates'])
			created_at.append(tweet[i]['created_at'])
			
			favorite_count.append(tweet[i]['favorite_count'])
			favorited.append(tweet[i]['favorited'])
			filter_level.append(tweet[i]['filter_level'])
			
			in_reply_to_status_id.append(tweet[i]['in_reply_to_status_id'])
			in_reply_to_user_id.append(tweet[i]['in_reply_to_user_id'])
			is_quote_status.append(tweet[i]['is_quote_status'])
			lang.append(tweet[i]['lang'])
			
			retweet_count.append(tweet[i]['retweet_count'])
			retweeted.append(tweet[i]['retweeted'])
			source.append(tweet[i]['source'])
			text.append(tweet[i]['text'])
			timestamp_ms.append(tweet[i]['timestamp_ms'])
			truncated.append(tweet[i]['truncated'])
			
			iduser_fk.append(tweet[i]['user']['id'])
			idregion_fk.append(sys.argv[2])
			print(idregion_fk[i])
			
##########inserir dados no Banco		
			try:			
				cursor = cnx.cursor()
				add_tweet = ("INSERT INTO TWEET VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
				cursor.execute(add_tweet, (idtweet[i], contributors[i], geo_latitude[i], geo_longitude[i], created_at[i], favorite_count[i], favorited[i], filter_level[i], in_reply_to_status_id[i], in_reply_to_user_id[i], is_quote_status[i], lang[i], retweet_count[i], retweeted[i], source[i], text[i], timestamp_ms[i], truncated[i], iduser_fk[i], idregion_fk[i]))
				cnx.commit()
				print(iduser_fk[i],': inserido com sucesso!')

			except Exception as erro:
				print("Linha " + str(i) + ". Erro na inserção dos dados no MySQL: {}".format(erro))		
			
			i = i+1				

	except Exception as erro2:
		print('Erro no parser do arquivo JSON: {}'.format(erro2))
	
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Algo errado com usuário ou senha!")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe!")
	else:
		print(err)
else:
	cnx.close()
