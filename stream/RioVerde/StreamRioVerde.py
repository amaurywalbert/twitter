# -*- coding: latin1 -*-
########################################################################
# Script que captura tweets de determinada região e armazena arquivos JSON com todos os dados dos Tweets
#
# Pode-se redireconar a saída para um arquivo texto.
#
# To run this code, first edit configRioVerde.py with your configuration, then:
#
# consumer_key = 'your-consumer-key'
# consumer_secret = 'your-consumer-secret'
# access_token = 'your-access-token'
# access_secret = 'your-access-secret'

import configRioVerde, tweepy, sys, random, time, json
from tweepy import OAuthHandler


class StreamRioVerde_Listener(tweepy.StreamListener):
#Inicializa a classe
	def __init__(self):
		self.counter = 0
		self.output  = open(time.strftime('RioVerde' + '%Y%m%d-%H%M%S') + '.json', 'w')

#retorna todos os dados do Tweet
	def on_data(self, data):
		self.on_status(data)
		print(data)
		return True # Não matar o stream 


#Grava o status do tweet em arquivos com XX tweets cada.
	def on_status(self, status):
		self.output.write(status)
		self.counter += 1
		if self.counter >= 10000: #Quantidade de tweets por arquivo.
			self.output.close()
			self.output = open('RioVerde' + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
			self.counter = 0
		return

	def on_error(self, status_code):
		print >> sys.stderr, 'Erro encontrado. Código:', status_code
		if status_code == 420: #Verifica se aconteceu algum erro na tentativa de conexão...
			return False #Desconectar o stream
		else:
			return True # Não matar o stream


	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		nsecs=random.randint(60,63) # Saída Anormal: espera entre 60 e 63 segundos e tenta novamente
		time.sleep(nsecs)
		return 

#################################################################################################
#################################################################################################
def main():
	auth = tweepy.OAuthHandler(configRioVerde.consumer_key, configRioVerde.consumer_secret)
	auth.set_access_token(configRioVerde.access_token, configRioVerde.access_secret)
	api = tweepy.API(auth)
	stream = tweepy.streaming.Stream(auth, StreamRioVerde_Listener())
	stream.filter(locations=[-50.967312,-17.844777,-50.886265,-17.750482], async=False) # RioVerde / false = apenas uma thread
#################################################################################################
#################################################################################################
if __name__ == '__main__':
    main()