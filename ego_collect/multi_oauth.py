# -*- coding: latin1 -*-
#
################################################################################################
# Função iniciar gerenciador de chaves com múltiplas contas:
# Lista com todas as chaves está disponível na conta no Evernote.	
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
#     Conta: msc20160012_app01 - user: msc2016002_app1 - e-mail: twitter01msc20160012@gmail.com - senha: padrão
#
consumer_key.append("ffap5ENG3yu0u7phgdhQzIvJx")
consumer_secret.append("bFXgZjBUGMRoSfxbKLNZG8Y0IqjUPoc9O4vgKOtUCs0WSlkT6s")
access_token.append("813458922967302144-f3aEkz6OsueSD6eCkaN1yYXVcYXPGuZ")
access_token_secret.append("OG08x1kx6rgMHwwEcmQKeeEAot88UALSQAY96XlGnpRba")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app02 - user: msc2016002_app2 - e-mail: twitter02msc20160012@gmail.com - senha: padrão
#
consumer_key.append("O4t25YPnHGNm7B1i5qaN7Gu3s")
consumer_secret.append("v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR")
access_token.append("813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi")
access_token_secret.append("VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app01 - user: msc2016002_app3 - e-mail: twitter03msc20160012@gmail.com - senha: padrão
#
consumer_key.append("ykRNgT6LkUosDfvNRKPTzKdyC")
consumer_secret.append("NaY2Zet7YH1tWPHE13sl0JuW5rPfEg6hzZQFPCKiGmMNVbfvI2")
access_token.append("818810967400284160-jRZ7pSAkhOLohRr3ZMNN9QPWzfLDu8L")
access_token_secret.append("mxw9n10lJdQ0qEhsFaChkkj0rxm4zk3FDRyxx3IcU81jB")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app04 - user: msc2016002_app4 - e-mail: twitter04msc20160012@gmail.com - senha: padrão
#
consumer_key.append("ucydTwduaEHj7CEZtwhqPyoY8")
consumer_secret.append("2bJhRTsRQvFWyI7xLi97SByjdAcD563UcSEH2mzXWis11OUas5")
access_token.append("818814560941510657-YS7ZG8CdGOarEhialSGqZ3HR8RDsi8j")
access_token_secret.append("9sInZONslZMldFYpV5e0u7B7EyQVBERXgi15pCGir0wXL")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app05 - user: msc2016002_app5 - e-mail: twitter05msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("VNxFdDgMvx4Dge4Q2afZt7l45")
consumer_secret.append("o1mIoWrqmbTDbEhUZaG4VqSBGplSSZo9OlM4rwFn6SwqCFSlRm")
access_token.append("819401695310528512-JpY8ntd3tBrTNSFOBDill7p7bCHpKSU")
access_token_secret.append("WpqOpdGjlWpTu7nvrG1Yfsp0jCKah6kQrMDpeZCp7LxBw")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app06 - user: msc2016002_app6 - e-mail: twitter06msc20160012@gmail.com - senha: padrão
#
consumer_key.append("cWJz68mRioD4KYSMQm3F6PbCZ")
consumer_secret.append("Oa1N0HhN2Ifd4qzF09TGVflqDndvs77LlJHTH2XXk16gOs6TqJ")
access_token.append("817489865466122240-JCAuAIB404lQZqmMMLHLP7je2QtfzlA")
access_token_secret.append("7rQV42SnR3I2S3GISugRS6a9LI5WMdymlw5iSIf6QXc6v")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app07 - user: msc2016002_app7 - e-mail: twitter07msc20160012@gmail.com - senha: padrão
# 
consumer_key.append("4GpGgwHB3yeeZ8aQIZD4LLqre")
consumer_secret.append("McX6jmXUPHu4eSTJQ41U7VY2q24mLJP5ZUcqYB4ovc2EoviOXH")
access_token.append("817492701889392644-Wji7oss1KCawoGjpGyy1KzlBHmAFCW9")
access_token_secret.append("gxP3I5k0olOqEMSn5kynVfDuHgPNgo6ynLskobwj3P0wg")
#
#     
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app08 - user: msc2016002_app8 - e-mail: twitter08msc20160012@gmail.com - senha: padrão
#
consumer_key.append("UzOedM4QmOsM1xPsyPGLc2OI4")
consumer_secret.append("B1TeVvnDgzxvMSjpg5bldlmSTid7C1UusnPmss9tMfvQVgFiCu")
access_token.append("817494567599611904-fYac01KBzyq6vgvMHKkb0AkVHm7SBFS")
access_token_secret.append("9KnAZWjg3xq2mu5q3l6Hfqj9CM3neIzOFLdB4Fnb2ZLsZ")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app09 - user: msc2016002_app9 - e-mail: twitter09msc20160012@gmail.com - senha: padrão
#     
consumer_key.append("9sz6NkdPOIZyVM0W7qm5vpTqe")
consumer_secret.append("stQcxPa5gRCuyDPC4A4uvRNQxiVlV15D2cTZbyJ8Jo1wnj9HJo")
access_token.append("817495894312493057-ofFWm7CqEbvSPSOKNVHK66BNndGF8YR")
access_token_secret.append("13sJjnbfLcJZ76PxIC16bzg8GCSleImnuMRhB1D4TCf1x")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app10 - user: msc2016002_app10 - e-mail: twitter10msc20160012@gmail.com - senha: padrão
#     
consumer_key.append("u6Qh4L8oLDINTl743zps4jSmb")
consumer_secret.append("iZprT4mlxrKeKnp1WUAcyGjYfDYkEgC6FAzu7H1H68GYqZfMMX")
access_token.append("817497484285145093-cpyWNWhMvAUkAWu4opV96hNtxMSRQ4g")
access_token_secret.append("PEnlovnA9927h7NUVkt0YE5aYHUJqkHtPS3bBZhjYlvvM")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app11 - user: msc2016002_11 - e-mail: twitter11msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("x4qzrPEvZvWnTIu3X7rVFwEVQ")
consumer_secret.append("PqenEfheKBvGob3KHLNo19yT9wBE8uNrEb3b1zPIY2YLeKN5J8")
access_token.append("819405209613041664-c0GhzjbnZ0vHRDqcYxDPy4mxYzYjlwX")
access_token_secret.append("vdGJMLEHYAjbVVu0SArUhdhzJpYv5ItfPh6tpiDuONzeP")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app12 - user: msc2016002_12 - e-mail: twitter12msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("t7TVuq57clRC046ZmNoJUXhzb")
consumer_secret.append("GiXWW4zZixDDNE5cnHI6AeO99nEIPBuOUJZhMvk67sbsP1zqdk")
access_token.append("819407030817607683-1bbPqcbZA4ZlnaPizrrJpM8FETlYB8v")
access_token_secret.append("a0PKhTisi9oBTKmXsspv46t2lNrYoC9ewaOskZc0cuvRJ")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app13 - user: msc2016002_13 - e-mail: twitter13msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("4cxE0wJ6x1ZqjsNnjbBjQ1XxK")
consumer_secret.append("FDD292IWBEpk55sd41RehOxcC5sKAqXw4RXFsUmykTG08FWoPJ")
access_token.append("819408960520417280-Ia5yrwwWRJjZakhXDT6UkkZon2LpEgc")
access_token_secret.append("LsWru0bh8fnLXrho8jfJYbjEz0gYddqX4JOpUE57EsPL5")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app14 - user: msc2016002_14 - e-mail: twitter14msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("zf1f2P4AllifZhtIwVoPeXjHC")
consumer_secret.append("Y29dMvDHaxOwKYzWMDoItdswI5ksCNmS2gckwel9pCzLGkfIM2")
access_token.append("819410554259439616-1F87qpjOMkvQSYb6srkxDb9GxhfCPSo")
access_token_secret.append("HtNBwTixhcB6LcBX1V8vqvBiLvjkzMecv3eW6xSdUXcPB")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app15 - user: msc2016002_15 - e-mail: twitter15msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("5PDmwijPhMM05F2IbXSmaO7Wu")
consumer_secret.append("xZXYgKhNE2yTBp1Fdu0AD6eL6vAla9PJWbHWYOPamLo1rKYBzH")
access_token.append("819411941374431232-lgKyr48Ctu2smXLhpZR4ngO69U6wa4K")
access_token_secret.append("beF0ifThX0wnrzwSGIFMPES7Ip9BznNs5DEMMEddjBo3R")
#
#
###############################################################################################################
##############################################################################################################
##############################################################################################################
#
# 										TESTES
#############################################################################################################
#
#		Conta: amaurywalbert - user: amaurywalbert - e-mail: amaurywalbert@gmail.com - senha: padrão
#
consumer_key_test.append("JeSUTJXGauV6RY7i6RJDSRvoL")
consumer_secret_test.append("ZCOMtPUTAJPFuEwm8S50wPIGF0CpVVFRJIQauy1DcSZ4w6v6ox")
access_token_test.append("41112432-fRQMmcN5D6mSgg8kPy9oNZqDRSujUkCjAQcPgwHOb")
access_token_secret_test.append("FxU83OnYRfr6eU8IWuj5pP2SviFsyu2UHAaGMJqjyD6a4")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: walbert1810 - user: walbert1810 - e-mail: amaurywalbert@live.com - senha: padrão
#
consumer_key_test.append("qvmfyEldFvEmTCAvzFSBTP1wz")
consumer_secret_test.append("L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA")
access_token_test.append("786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0")
access_token_secret_test.append("in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: amaurywcarvalho - user: amaurywcarvalho - e-mail: amaurywalbert@hotmail.com - senha: padrão
#
consumer_key_test.append("U7NBO7duqO1aTZ81q63Hy61Er")
consumer_secret_test.append("kVKISoiaUrw1gBAZpTLPJ1op8GfONmHULeTMG01Ofj2OsAMkOg")
access_token_test.append("781627388329398273-lrXG081wRlkvHpYAPO0iS77p3fGnijs")
access_token_secret_test.append("cR71hKrAb4zZIyZqGIwDuH0HMnC1Z7BAwN7MKEfe7Uhg7")
#
#       

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
