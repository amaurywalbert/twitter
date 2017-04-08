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
## msc20160012_13
consumer_key.append("w9GvsiaQy9jcBDTKIaXomBjQT")
consumer_secret.append("H53rMVNGlrUvYFnN5f5ud1JzrGkhVpz2e335KBK413KrEK8Mwc")
access_token.append("813460676475842560-moOTo31XN8tbUbrKM3QOitihXsPD1Z9")
access_token_secret.append("aGuidWdVzC24kkUSJ6BNDxKRwUPchCz0LWtEnVINJShY3")
#
# msc20160012_17
consumer_key.append("HbJwp3WUsVjvBxHuDuKIQdc7q")
consumer_secret.append("uPflQdUndr8r95KPXpb9L3OmfFQ8HFJaB1XlsEEqka6L5Ytbqj")
access_token.append("813460676475842560-GQM6Bo4IHfmUUiRYln9VfqRQecOtBja")
access_token_secret.append("Je4QsyutTUTPhWkC9oA0ylviBKRywNKuu6IHO8B5CcB1W")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_271
consumer_key.append("tY71hkUKRrr9Bf94Bo1El5ozW")
consumer_secret.append("Xm3ZSg2zmCNSMJtx3sBeODkZkQqiLAFmkOi7KoTrcak00rLyHK")
access_token.append("822174289742925824-FzJqDAWIgRkJ8xR15BLQR9E8oJ7L3a3")
access_token_secret.append("bwD0p1lREYF9kSSiYp1vWXdKBM4jzAjW8ONJgCDXuT66n")
#
#msc20160012_275
consumer_key.append("RYBuA9GD4LjGphPHjwRUOKfWa")
consumer_secret.append("89Vbnb1D9SqaUT0ugJe26LHhibf9HhrOgajzPsxou0ZSCpKjym")
access_token.append("822174289742925824-ETWx8Dt4SOzDS0yadHUlMoPGcQu6nk8")
access_token_secret.append("DctJAd1giXTtzuGZiyVTxjkRN5ocVqD6Th6VCHZfrzIVK")
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001228 - user: msc2016001228 - e-mail: twitter28msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_282
consumer_key.append("4iIGM7yv8VWfMHegwrydaJlwS")
consumer_secret.append("9fGG9ZGEzFLYg2CI8ZLcFqBmairuPUhEGahf0mllfJNKP58srt")
access_token.append("822215581831151616-rhZZPCcgsWJcEC2tqqmLCBE8grxE79i")
access_token_secret.append("GftUoNM7AbsorZeHF5YyHWnqsMf1ZdWX2idjmklgSj3Xf")
#
#msc20160012_286
consumer_key.append("eHF55h3aBdampUfVFGxXB0qKs")
consumer_secret.append("38xGLPZRkBSZcSWVeLQAIzl6oB0wMjDl4evkuQr0Tn1QUP5Ghk")
access_token.append("822215581831151616-XX2uRNxv2L5n5wHIb28pfe1brDGumNr")
access_token_secret.append("gxEG8lb9cSmnDfXQtXrl2876sfcbg7BwPsfuiwCmlwtO1")
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001230 - user: msc2016001230 - e-mail: twitter30msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_303
consumer_key.append("u0iHmGkH4K1j4Fhax0QEHrx4Z")
consumer_secret.append("YkQ18k3TgaYELhMDAKM3hAZUyAqsrliNVY6DUivj6J7k4LrRxe")
access_token.append("822219154245779456-XAayNnIyExmRwTzeg3cR67vOi6CUeeP")
access_token_secret.append("dHTx0GsF2s2SXpQ7lJaV9w52xkBM7TiNmHncRdUM3wXdd")
#
#msc20160012_307
consumer_key.append("hvRRwKjz3hKFlco8U6KEiWPAE")
consumer_secret.append("q3GAS7dMZyzSpCMElAyeNUOnQD3FD1H7hTxbtFRrr6EfY64V6Q")
access_token.append("822219154245779456-fC4DjCERWsHeM9p998a7zxho099TkQU")
access_token_secret.append("Tuh1AmZ8NuYD35ySprM1fLOTIAjJNUKJxgQEsy9V69G2e")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001231 - user: msc2016001231 - e-mail: twitter31msc20160012@yahoo.com - senha: padrão
#
#msc20160012_3113
consumer_key.append("qqECHxNz8E0z3UXWENHKJRAhU")
consumer_secret.append("pv77SIwPwKgYByr6fjIrAvyXcj7xWep0ElmIY712WxRaapFkqE")
access_token.append("831843480565645314-7Z0ipwQwjfSBl3lb2c4C1iKtVS4aeOp")
access_token_secret.append("FNzO9FIkNpQfbKkcXUt0d7a2Oi8EuYZWthh88OtSTVNh8")
#

#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001232 - user: msc2016001232 - e-mail: twitter32msc20160012@yahoo.com - senha: padrão
#
#msc20160012_323
consumer_key.append("2mKNKdnpvcQ2bpMfY0DoYcNFl")
consumer_secret.append("s9rYvgCCUWzn4WP66zK0uKfImbdvNi0KHHkTHMJO0hPCJqwY8q")
access_token.append("831846189331005440-T9s3eslLBirsJ3chzjk3dU2vVxsQNKf")
access_token_secret.append("rsLeDdpNx9EsA78jy0jTY5X6bAGhcMjOh6udgndcqDd1F")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001233 - user: msc2016001233 - e-mail: twitter33msc20160012@yahoo.com - senha: padrão
#
#msc20160012_333
consumer_key.append("fkcEAzeKWqMEwZnX5cBP1QQth")
consumer_secret.append("FhtIIforvA6f9egJdftCKaG40xa42JqAvYqAgRoN8SzHrVG87y")
access_token.append("831849920944553984-c3qVnCicXPRAn9wnDbip3KMbRbKzdPu")
access_token_secret.append("GlGul4iMwYVGYrBQJsqQvtx9YUiOAw5plf1OSaBG0g8j5")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: walbert1810 - user: walbert1810 - e-mail: amaurywalbert@live.com - senha: padrão
#
#msc20160012_teste_23
consumer_key.append("VMkcoyd5vate9jLbW0ze6yp0a")
consumer_secret.append("XsDwoTCE2AhiXeRyNu38XhcxZChE44kl9ED10U5BA9vzKWFUpE")
access_token.append("786664983862083584-Zii8faTHCNUSLv9SjYNasYZfUFIMkZy")
access_token_secret.append("TFMiyIQfTv25M1UXdV8XUHO8La3Pk0F9BI2og8qAVPBhs")
#
#msc20160012_teste_27
consumer_key.append("QtsZOve6CEDxLpoZJCxqdchwh")
consumer_secret.append("0Odtl5Nxbc4TdPvsGrLXjBFsSQRuvdhsOBtrLAVMHN5Au3497F")
access_token.append("786664983862083584-t9tkoEiGm0IFi08bFCqucdDV1WqmNpV")
access_token_secret.append("AvvCPaMWEjbUrvTElIVM8DoD7vLaVQEdSQEFmtk9oSyqn")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: amaurywcarvalho - user: amaurywcarvalho - e-mail: amaurywalbert@hotmail.com - senha: padrão
#
#msc20160012_teste_31
consumer_key.append("8akQi5gDAevmAFZDyJmqx4TWH")
consumer_secret.append("4dYWFWKrFDLWm5hrZwuAlU3VmIiBt4PcHz4DooIfihW72yLWxg")
access_token.append("781627388329398273-vi5rfX2ML86Yp1NCYSED5IgzzGQ0JrD")
access_token_secret.append("kjgZ9eItetjXKd0JNt520bHXZj9NzYdD9TZnLytMm9sEO")
#
#msc20160012_teste_35
consumer_key.append("E6hDM7RUR80CSKAaB0sLBC9iN")
consumer_secret.append("m4vl1r3iHoF8ccTcgpBAE88Ifr48CICTOF3Tg7YmCximTb8jsv")
access_token.append("781627388329398273-pZ9X470f9us4YGI9VxxEgPCOaYzmHTh")
access_token_secret.append("o9tBTTLwHRmGZWPV7uVVIfkbP2vTeWKiQz8lBSeP6oXMV")
#
#msc20160012_teste_39
consumer_key.append("T4vg40L1Vj7kafKDfWKaXb6CT")
consumer_secret.append("1DCpL9yVvCJNZXcsDQbJ7jgjR7zQr1YZHbSkIfBx04MlsrzqGt")
access_token.append("781627388329398273-E3npXY8XgBC0H67EI95FVxAzFrrFSOG")
access_token_secret.append("SIi08DWgTRk9DzcaQu3XMIwXJFNpcyNFRH1lKuQTW3NXr")
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
