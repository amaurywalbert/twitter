# -*- coding: latin1 -*-
#
#Argumentos
#1 - Nome do arquivo de entrada
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
idtweet_fk = []

hashtags = []
symbols = []
urls = []
user_mentions = []

hashtags_full = []
symbols_full = []
urls_full = []
user_mentions_full = []


#contador
i = 0

##########################################################################################################
try:
	cnx = mysql.connector.connect(user='twitter', password='roma031205', host='127.0.0.1', database='twitter')

#Ler arquivo JSON
	file = open(sys.argv[1])

	try:
		for line in file:
			tweet.append(json.loads(line))

##########inserir dados no Banco		
			cursor = cnx.cursor()			

			idtweet_fk.append(tweet[i]['id'])
 			
##########################################################################################################
########## #Converter lista em String  - 1 entidade por inserção
##########################################################################################################
#			hashtags_full.append(tweet[i]['entities']['hashtags'])
#			if hashtags_full[i]:
#				for x in range(0, len(hashtags_full[i])):
#					hashtags.append(tweet[i]['entities']['hashtags'][x]['text'])
#					add_hashtags = ("INSERT INTO ENTITIES (idtweet_fk, hashtags) VALUES (%s, %s)")
#					cursor.execute(add_hashtags, (idtweet_fk[i], hashtags[x]))
#					cnx.commit()
			

#Falta localizar um tweet com um symbol para determinar qual entrada do arquivo JSON deve ser usada			
#			symbols_full.append(tweet[i]['entities']['symbols']) #Converter lista em String
#			if symbols_full[i]:
#				for x in range(0, len(symbols_full[i])):
#					symbols.append(tweet[i]['entities']['symbols'][x]) ##### Faltando determinar entrada...
#					add_symbols = ("INSERT INTO ENTITIES (idtweet_fk, symbols) VALUES (%s, %s)")
#					cursor.execute(add_symbols, (idtweet_fk[i], symbols[x]))
#					cnx.commit()
#			
#			
#			urls_full.append(tweet[i]['entities']['urls'])
#			if urls_full[i]:
#				for x in range(0, len(urls_full[i])):
#					urls.append(tweet[i]['entities']['urls'][x]['expanded_url'])
#					add_urls = ("INSERT INTO ENTITIES (idtweet_fk, urls) VALUES (%s, %s)")
#					cursor.execute(add_urls, (idtweet_fk[i], urls[x]))
#					cnx.commit()
#					
#					
#			user_mentions_full.append(tweet[i]['entities']['user_mentions'])
#			if user_mentions_full[i]:
#				for x in range(0, len(user_mentions_full[i])):
#					user_mentions.append(tweet[i]['entities']['user_mentions'][x]['id'])
#					add_user_mentions = ("INSERT INTO ENTITIES (idtweet_fk, user_mentions) VALUES (%s, %s)")
#					cursor.execute(add_user_mentions, (idtweet_fk[i], user_mentions[x]))
#					cnx.commit()
#			
##########################################################################################################
########## #Converter lista em String  - Várias entidades por inserção
##########################################################################################################
			hashtags_full.append(';'.join(map(str, tweet[i]['entities']['hashtags'])))			
			symbols_full.append(';'.join(map(str, tweet[i]['entities']['symbols'])))
			urls_full.append(';'.join(map(str, tweet[i]['entities']['urls'])))
			user_mentions_full.append(';'.join(map(str, tweet[i]['entities']['user_mentions'])))
			
			add_entities = ("INSERT INTO ENTITIES (idtweet_fk, hashtags, symbols, urls, user_mentions) VALUES (%s, %s, %s, %s,%s)")
			cursor.execute(add_entities, (idtweet_fk[i],hashtags_full[i], symbols_full[i], urls_full[i], user_mentions_full[i]))
			cnx.commit()
			print(idtweet_fk[i],': inserido com sucesso!')
		
			i = i+1
			
	except Exception as erro:
		print('Erro: {}'.format(erro))
	

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Algo errado com usuário ou senha!")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe!")
	else:
		print(err)
else:
	cnx.close()