# -*- coding: latin1 -*-
#
################################################################################################
# Função iniciar gerenciador de chaves com múltiplas contas:
# Lista com todas as chaves está disponível na conta no Evernote.
#
# IMPORTANTE -- criar um link (hardlink) para a pasta /usr/lib/python2.7	
#

import tweepy

consumer_key=[]
consumer_secret=[]
access_token=[]
access_token_secret=[]

consumer_key_test=[]
consumer_secret_test=[]
access_token_test=[]
access_token_secret_test=[]


##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app02 - user: msc2016002_app2 - e-mail: twitter02msc20160012@gmail.com - senha: padrão
#
## msc20160012_14
consumer_key.append("cqRzqBL0fV3URMEvxnXl2sIxV")
consumer_secret.append("8mX8egarv1Wyw6EuPbF6vfegOXFtF3gj395fKKkX19OitcxCAo")
access_token.append("813460676475842560-A7YnIIk13B0ezrqtEXdaEMOIF08qxdi")
access_token_secret.append("Qb2YgSaJFFypqPjRxaBFe7hQvM8GyMKUAArcCvyfLpbNE")
#
# msc20160012_18
consumer_key.append("mYw48LrblLQrVF6Y6rStxttas")
consumer_secret.append("66X76dJ7wUvTiHZSJq36ex7kLdaFzpfx1nJ6v7KwYe1HUtLuKu")
access_token.append("813460676475842560-m61gryMuRrvrk5mZS78pw8fwlVuev9L")
access_token_secret.append("Q9SDIHvf484Wq3KudGtnh9YsQHIOPnAKmbaYgQfXMJvbs")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padrão
#
#msc20160012_272
consumer_key.append("2uPnLUW64bSaYLoair7dNr8X3")
consumer_secret.append("YNMXQjcNfHwQoJaaJNT1yad2innQQhUDSHY9OMYpJs14lBEj48")
access_token.append("822174289742925824-F8AHoJGLyPl9CkzjbSM1hRmquVaXu1p")
access_token_secret.append("DGvVZ1srkgB1NHMnU5DIBKvPyNl4GnowDezv9dIodSxft")
#
#
#msc20160012_276
consumer_key.append("liqOsZ4kXMmEIoYfEa1TX6RVB")
consumer_secret.append("M7Cd9HrWSz5hVWkZfeKqLCGlCiTAkFwyKnjbk9LwAlD5WHyFhU")
access_token.append("822174289742925824-xMkpFnBZjiJ4XTlOoYAxOIQuKacinEp")
access_token_secret.append("dMQ3Y99jwmJr25Qr9nmOMhxzOoWSplMwiB7Mx7nG75IDO")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001228 - user: msc2016001228 - e-mail: twitter28msc20160012@yahoo.com - senha: padrão
#
#msc20160012_283
consumer_key.append("GDT3nVD2v0fJ1bJ7vjIW0gRYD")
consumer_secret.append("yUhEwcvVEvQiH5LuFTS6DrqdQeS4GjAQCIosjLcY0YpwUzQUxv")
access_token.append("822215581831151616-sPq3ZkL2cXEHhK0yF2lSxdT0Ghufv36")
access_token_secret.append("86XdzFKqKgkZIxIvVNd2RSCDToGlrGk2BnBN2TOTjS8UZ")
#
#msc20160012_287
consumer_key.append("WEx7V5xok4K0TYRkMQ74dWtQq")
consumer_secret.append("dHjUWSeSRC82wekeK7vnwTqOwRSe32w9l2K1TX1LdCOBK4WAN2")
access_token.append("822215581831151616-jTgyNDRYFlghFmK2qvcS8JIBc09kPJH")
access_token_secret.append("0Ja66Y4ZRgO2txQK4bgV2f3K737pisvcmEiKVabVDjFPu")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001230 - user: msc2016001230 - e-mail: twitter30msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_304
consumer_key.append("O1hwkBbbNlIf1TIldYKJe6GUr")
consumer_secret.append("6glvu4R6lqK0a73CwCcIIF98JHMcUXgtqpLOEQUkknvyOdC8Gd")
access_token.append("822219154245779456-DyPdIDEk8LWPkZPQM6OcKsvnTPo4xXL")
access_token_secret.append("sHOppRfzgYsk5nMro5oofmrJDXYzWtFFVnrsn863GNUZq")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001231 - user: msc2016001231 - e-mail: twitter31msc20160012@yahoo.com - senha: padrão
#
#msc20160012_3111
consumer_key.append("xqRDNkgLW9akJTbjB1F01yOaK")
consumer_secret.append("v44MFstC4IpjtSo3xPRw7zk5Vo4Kvj07fhgQOjIMRbTA2pLls3")
access_token.append("831843480565645314-tNEdOhZlV4ODJ468ENAHJeccupfofbW")
access_token_secret.append("RjCllDWZOHstKLgiCLMrXxXSfo1jRgl0XJiWPcNgwUFL1")
#
#msc20160012_3114
consumer_key.append("j0LEbsCX7fu8fg6gpyiqFZRvS")
consumer_secret.append("2NAi1awfnFTOy83rbrpUkmG3PUbgbwvAbQmx6qmemUmm826Hbt")
access_token.append("831843480565645314-V4amd6KuFTzqBhvgjd7o1pt4YIPCT80")
access_token_secret.append("Xzai0SsCjuKbJzjrGR16bq0TRyeIF882fqr5CnuphyKIs")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001232 - user: msc2016001232 - e-mail: twitter32msc20160012@yahoo.com - senha: padrão
#
#msc20160012_324
consumer_key.append("xQR02ECkUS82TaQE5tVP3QsyG")
consumer_secret.append("XQfpvVglRBLmAMOY1sHJ0dpY8F8bIMwegeUniGTVtMosftZ1Ad")
access_token.append("831846189331005440-9OSZvvmvjZNIdFsUyR4PZS8aL5XRAAw")
access_token_secret.append("aCVij0rShnTHuCZ7VSTOoyTauM9xcMbZgkqXjaG1KBCI2")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001233 - user: msc2016001233 - e-mail: twitter33msc20160012@yahoo.com - senha: padrão
#
#msc20160012_334
consumer_key.append("Vsm6Z9zcKIEJnJW8hXWipMnOr")
consumer_secret.append("A4OF8LPzWEx4yInB9pq4jVOj6OWKX48B0A8sEP4hbvVAzYFlHm")
access_token.append("831849920944553984-TiW3LH7UzOQzQkltjmPstjrbkLAcvfj")
access_token_secret.append("dtbbnTX90HTcGdabTnRUw5Xdva1U1OUNZRQyLqZ5OclCx")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: walbert1810 - user: walbert1810 - e-mail: amaurywalbert@live.com - senha: padrão
#
#msc20160012_teste_24
consumer_key.append("UNwhnaGwIzjeNIb9p796O4cBl")
consumer_secret.append("XkyvDXE9AiFdgd6bjiyeyvxgqgitIgsdRrRAZbcfGx74GHOWsN")
access_token.append("786664983862083584-BcES2YdF1jjCl7Hg2vumGfPidwyxZTT")
access_token_secret.append("iPkexY0o16DejWq5MfGs8uR6UeloY8koblw3cOVVP1FC6")
#
#msc20160012_teste_28
consumer_key.append("D3Pg6sKoqjcVse7JzOIVLCAsy")
consumer_secret.append("Fzy3SOcC2SKUDmEkqTohfTUjKfG9Q6jYoKweKjEaVs0C2Xxxfi")
access_token.append("786664983862083584-OAMMg0ibOvTK5x0xQYHohP6KUnkcXJu")
access_token_secret.append("TFRcnibofxuMlVsaRgtSqnY7NITFp47unbanD9COzM3Qe")
#
#msc20160012_teste_29
consumer_key.append("MnYDJIMKt0K3f8nLCaeOoPXwA")
consumer_secret.append("2wlRRmkkwkkhcbaTs61nivl77hWfxXb0sK9y9bJzYs12gBwS9b")
access_token.append("786664983862083584-aeT4o0PHidPXXs4ttEPXgFQg6RQRMIw")
access_token_secret.append("ErOvKqKjhltZ7u55ynhgg2p4MUYFB0LM0T9ya2RydpAIe")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: amaurywcarvalho - user: amaurywcarvalho - e-mail: amaurywalbert@hotmail.com - senha: padrão
#
#msc20160012_teste_32
consumer_key.append("U7NBO7duqO1aTZ81q63Hy61Er")
consumer_secret.append("kVKISoiaUrw1gBAZpTLPJ1op8GfONmHULeTMG01Ofj2OsAMkOg")
access_token.append("781627388329398273-lrXG081wRlkvHpYAPO0iS77p3fGnijs")
access_token_secret.append("cR71hKrAb4zZIyZqGIwDuH0HMnC1Z7BAwN7MKEfe7Uhg7")
#
#
#msc20160012_teste_36
consumer_key.append("mAeJK5IAQjo7JXvvze5twWZ1s")
consumer_secret.append("qWcO3E7igA6wASmM3lR7Rn0sYf6GMEZ2thCzM4nYPSqk9DBhxk")
access_token.append("781627388329398273-ODQGBx11UGaHfHkwdmPWQCq25zhGg2Q")
access_token_secret.append("SxwxnHaRKx7sXjAbdAJQSLIYDrVHSHJfAyi1rfnY2YCiv")
#
#msc20160012_teste_40
consumer_key.append("7OG74Se1CjFl6gyS2MLYPUEvn")
consumer_secret.append("B2uMc1Ieh1eyBhAhg7WddxeUXsrgHiE6qVA1fwvO3myFAlTOhO")
access_token.append("781627388329398273-xePNyHyK9hNMnrRgLnBcxCwrfWOJAfx")
access_token_secret.append("mTo67zDHgLd7DCV2jHv1WUWUCt6wJ4Cr38OUhMD0ryutF")
#
#
##############################################################################################################
##############################################################################################################
###############################################################################################################
##############################################################################################################
##############################################################################################################
#
#
##############################################################################################################
##############################################################################################################
#
#		Conta: msc2016001247 - user: msc2016001247 - e-mail: twitter47msc20160012@yahoo.com - senha: padrão cel 64 9 9215-0461
#
#
#msc20160012_47_test
consumer_key_test.append("gOa37Y85DcbM2Oi3IpvvFWMj9")
consumer_secret_test.append("Fh334ZT5fXKDTS8zGJR1N6RU3kDdLKhEAk2ZB97iKydCUCaMQp")
access_token_test.append("849270909034692608-YPMJReaqxI6oVdP7RQ2cfqJinlghtuD")
access_token_secret_test.append("A6g4aVqq17gAzNPmxsDFIPUo9PVb546JlGw0gK3agWgiM")
#
#
#msc20160012_48_test
consumer_key_test.append("6JURlBsCpoDnG97JcQXb1DVDq")
consumer_secret_test.append("8dzL2NSfOXg3QSBb97LWS4ChDb9ycUYGIDBuIKHXkKfdWYMccg")
access_token_test.append("849270909034692608-zZav8hfaWZtBwXIctKtK9FnhHiBS4eq")
access_token_secret_test.append("iarzO6gXEN7o260zesA9aVesLvZcElKsSZ2fomQKulzrQ")
#
#
##############################################################################################################
##############################################################################################################
def keys():
# create authentication handlers given pre-existing keys  

	auths = []
	auths_test = []

	j=0
	for i in consumer_key:	
		auth = tweepy.OAuthHandler(consumer_key[j], consumer_secret[j])
		auth.set_access_token(access_token[j], access_token_secret[j])

		auths.append(auth)
		j = j+1


	k=0
	for i in consumer_key_test:	
		auth = tweepy.OAuthHandler(consumer_key_test[k], consumer_secret_test[k])
		auth.set_access_token(access_token_test[k], access_token_secret_test[k])

		auths_test.append(auth)
		k = k+1

	return {'auths_ok':auths, 'auths_test':auths_test}
	
###########################################################   USAGE
#
#auths = keys()
#
#api = tweepy.API(auths['auths_ok'], wait_on_rate_limit=True)
#api = tweepy.API(auths['auths_test'], wait_on_rate_limit=True)
