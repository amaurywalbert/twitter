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
## msc20160012_11
consumer_key.append("O4t25YPnHGNm7B1i5qaN7Gu3s")
consumer_secret.append("v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR")
access_token.append("813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi")
access_token_secret.append("VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB")
#
# msc20160012_15
consumer_key.append("Bg18Yht35FNbKH153Xgh3awfQ")
consumer_secret.append("EA7s3UhtsbLBdo3srXwqciOOQtywUindvOXYoNQ0e3zOJk55JB")
access_token.append("813460676475842560-faCiUVzZ0k7lOVxEEiQLxAR9Te2jEdt")
access_token_secret.append("KBWpx4v2qYbpZcCOShDpFJCAzuHQHJtWlQtpyppjyDcx7")
#
# msc20160012_19
consumer_key.append("AbBex8ClaE7vEWOWG8C1WUtaq")
consumer_secret.append("X91do3pnXVp2UvaV183Ei04XDVS8CC3GNHwcHbDmJhQjgvKNzv")
access_token.append("813460676475842560-5Xj9GuFOcIGkiUL33wPs1eMcd90h5Oj")
access_token_secret.append("ICWDbDdnteGxxMP1OOAdtrPcfUYP4GXslPjR07eBGxKSx")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padrão
#
#msc20160012_273
consumer_key.append("PRBkeyXx8GntzlY1wprr0FmPZ")
consumer_secret.append("MY7wdyeyS9jwq0jk4NPKbOIr75AB0pnGJTkPzmyHd5SxF1o9Nz")
access_token.append("822174289742925824-mcHb7NDfPpMSibKgVKIC5KAxx622e4C")
access_token_secret.append("4g8U1XawXSlXmgaZwZnrEie3xecq78CEiV9OJeukdZmFE")
#
#msc20160012_277
consumer_key.append("x74CsIkiFaw1ETgvSsg0aEe6P")
consumer_secret.append("I5eR17iro7el6nsXuRb8obRuWF8pbMegxixEtZ6LZqaWGYLexn")
access_token.append("822174289742925824-2OPxE2joQfKxYRkDln20jODExWX1Mm0")
access_token_secret.append("9kROGMa66BW0pUgjs7j05YX9ElMsI0hxkMEX5Yp201sUs")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001228 - user: msc2016001228 - e-mail: twitter28msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_284
consumer_key.append("DRJbtfWrWCzYBwVBZI1Ab3pTv")
consumer_secret.append("BwN8tKYK3joF8ohQcSDronjOTjDrra9we6Ra1kfpyqESTZdsIx")
access_token.append("822215581831151616-0NMuIlNlLpEKPl7ODutzJux7ZnMxHjl")
access_token_secret.append("OMuhPznJRP9l7gTDAlJVKuhIFQArZ49vVK1qPdHTHcd1v")
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001230 - user: msc2016001230 - e-mail: twitter30msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_301
consumer_key.append("78FsYx3VnphiSmMeGYNbuk3CW")
consumer_secret.append("m0no952gbsWt5ZwoNjAHGZ5uF30pyIdbQuYK978IYZ2eC9esME")
access_token.append("822219154245779456-K9hBIl3xDDzclfiYKiop6dcKhrbOopF")
access_token_secret.append("eXoCbIOsKylGjoIq95G6HYfE6AndfbxWLS9mB7jNppsRJ")
#
#msc20160012_305
consumer_key.append("rKRqw0RLuuZUgEecPfs4RJ7xS")
consumer_secret.append("S1QHsIZjTvtxxQU0b2e4BHdMAVQjuWCnJ00jPzxp6pzh6ng93z")
access_token.append("822219154245779456-HnOmzoAMB3q2YSenNOZXrGtVBqo5G4H")
access_token_secret.append("fMKVst9Yc7BsxsxXpYcr4XSu69FRbYG1kRIc8153MYFlq")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001231 - user: msc2016001231 - e-mail: twitter31msc20160012@yahoo.com - senha: padrão
#
#msc20160012_3112
consumer_key.append("gHi3JLS6iBI4m0c0UfmIHJ2as")
consumer_secret.append("bfswBVgKmSQXiVXx7gjbiNLmSF0g3BACObl920uP7eGSy7qXTW")
access_token.append("831843480565645314-7fdZiOYTK7gswBSWuZbrj48uNRTWOLT")
access_token_secret.append("snsI8xqdjEGc3HGBa5DWcZKRmUCWJtUujjbCDRfTiMPbO")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001232 - user: msc2016001232 - e-mail: twitter32msc20160012@yahoo.com - senha: padrão
#
#msc20160012_321
consumer_key.append("9HwvjhRzlNWS16vZcNBg1VRI2")
consumer_secret.append("88xa1rZsxCH88PHNFYEOaGVyRKtEFRzGitCtKktafMZ1kO8U38")
access_token.append("831846189331005440-4G7Igh8nQ0Jaf8rBNG4nJCIODE69p7Q")
access_token_secret.append("yIYSFtIcP1TLCzDepD4JKx0CCUuinYMn1MP0EBNUDipq9")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001233 - user: msc2016001233 - e-mail: twitter33msc20160012@yahoo.com - senha: padrão
#
#msc20160012_331
consumer_key.append("3gdXCHZ8T43pOmZcBVt86ttBf")
consumer_secret.append("vnoo0P17s7iJ0Qh4jh08FRUzP3FF3cEr1fgcSQNndsFdYpxTTs")
access_token.append("831849920944553984-els3pI9zCLz1c8D3FIrfpHqo6i58b44")
access_token_secret.append("sRs5nE5F07k7Pw4LlWycPcIiNRgMYE94ti3zbVoNUerlW")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: walbert1810 - user: walbert1810 - e-mail: amaurywalbert@live.com - senha: padrão
#
#msc20160012_teste_21
consumer_key.append("qvmfyEldFvEmTCAvzFSBTP1wz")
consumer_secret.append("L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA")
access_token.append("786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0")
access_token_secret.append("in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ")
#
#msc20160012_teste_25
consumer_key.append("sVAP0Oot5Oy9DGvjcwxQPRIPc")
consumer_secret.append("5R1p6nZe3n1akSUUz0rPfa8RakyKi7C7UnlBPs4NqgSi3IQxkt")
access_token.append("786664983862083584-8I0z6KT2Q9gifwhfRP7eBDBRLTtzlx7")
access_token_secret.append("BC2TxS8m4nxdaSm4KS2DVMyvCZwx4Tbhv95tMrvubaosl")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: amaurywcarvalho - user: amaurywcarvalho - e-mail: amaurywalbert@hotmail.com - senha: padrão
#
#msc20160012_teste_33
consumer_key.append("k2X1NYSSfLxqbTElsaJoamTpA")
consumer_secret.append("ywBx5cyqHmKrFtziklEgtzAJKHTtz5ORXAFNvdEcIyyv6KH9uc")
access_token.append("781627388329398273-CkaxgovlocA4s2OVJdyyBwZh495uIZM")
access_token_secret.append("i0zSthAta9HIH6dNTSlVrLQnrsBt1fVM2cjpFQIpFmBx0")
#
#msc20160012_teste_37
consumer_key.append("h4iMaoyE4Ouzv8BZu34Eluya0")
consumer_secret.append("GFBDJJT7JECENeCheEirsXr2Y2iDk1nB9b99akvQBRNFKFekka")
access_token.append("781627388329398273-0ZKJJjT2HFIAdTZbpO6Fl6bJv60ihtz")
access_token_secret.append("bOzBwAKUBpyiSHWASoEOWGE5VAQ40IFa90zUq47tFyEHe")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app02 - user: msc2016002_app2 - e-mail: twitter02msc20160012@gmail.com - senha: padrão
#
## msc20160012_12
consumer_key.append("R5iaxJ4FpLL6pcDOrr2osLNKr")
consumer_secret.append("PRNJxduOZgGsmjDlIeZIMuPF8qaauSxzYDlggdLWb1S3A5AOXO")
access_token.append("813460676475842560-2aJSRKgnhugK16w1T4AERo0pkoNtjxO")
access_token_secret.append("pSUfiFZmyb68U4YihPMFKWSQYKk2Js4cqGEgKNVbeS5xk")
#
# msc20160012_16
consumer_key.append("Qys38SRmmVBz90iioGWTSscJK")
consumer_secret.append("uhjDfaWQKkwHgwP4EiCx9XQD3egAkcAFF1dkIFQub6BFy2c2Nv")
access_token.append("813460676475842560-56PWNQlHVUYOlFw4tBBr5THeRD8ADlY")
access_token_secret.append("lrorUYCvBydihVI1gJytodrV3vYWuExjfQhALIAvzvWh5")
#
# msc20160012_20
consumer_key.append("hcDQsLpPwzCqbP15gcAXWy9wm")
consumer_secret.append("CAySoYt5us0FcEz2iDxg2EDFr1nYcPeLp6Omt6r0Zk9wlTUlvm")
access_token.append("813460676475842560-eSu92Sq1nR2V1UXfuHGsd4RTn9m0Pbh")
access_token_secret.append("4SpKiJwRMUvbNI5AgDAel51zZBzVkC1OOn84Z9ShwZMlO")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_274
consumer_key.append("mdue9ooyWiln1twkq3fevguEc")
consumer_secret.append("21hCCnT0XuWqByeGXaetNljMGZh6QCTJCCWmxIkDwSj7YcHiGV")
access_token.append("822174289742925824-K1gPcc6uueb594soemAg8b0FWf1fBsY")
access_token_secret.append("ZCz1kkRblLTrpBXG4LvkHbTnEnp4Upg1eTY8D35sKGbww")
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001228 - user: msc2016001228 - e-mail: twitter28msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_281
consumer_key.append("1tvls7W6QObrPrSjGsqehSMgd")
consumer_secret.append("YILtV6oYSayKZtsdJhDIr7QKvtPSQdLxRlOn1vGyL2nudIBece")
access_token.append("822215581831151616-k9pPtsIYTvmqU9F3vyIzVn2qm2vgH6v")
access_token_secret.append("h0ATS5hOrXrIGwdML8jZkBGuh2hOYMBYmknMAFlAq9tpC")
#
#msc20160012_285
consumer_key.append("exZlkyy3hKbb9qLesEJY4pp5q")
consumer_secret.append("3l6KCCwyK10dvxiItk7C3UmXVor93iCrv8rZ2rtTJ3kIabQoUg")
access_token.append("822215581831151616-v7UNAXUVU2k0M1oSHqoW0RZWXnFrw88")
access_token_secret.append("M7mPc1exhD2V0epzg1p24XDyo3BpUvDIuIHKjOIfnpNxU")
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001230 - user: msc2016001230 - e-mail: twitter30msc20160012@yahoo.com - senha: padrão
#
#
#msc20160012_302
consumer_key.append("xkIYFJprTE1sah8eP4DKzoHzJ")
consumer_secret.append("6pdEMTXZtPJas1A55EKcuEM3kRXZEo8GUf7ZGUTEFHYRP5Bo8O")
access_token.append("822219154245779456-pfBcFZFruanmEUk9ikuaHU2RBoPPgsi")
access_token_secret.append("qDB3P7rPexp8jcWns4BIKmOib2Cm4fR0eyFpKzMfSXOeB")
#
#msc20160012_306
consumer_key.append("nO41xjSRfFROyLVtqpu4ClVFO")
consumer_secret.append("h6CgfN2ZBd80792HQ3PRDwWdT8i62KHQucS8elVqWFQHVFGATY")
access_token.append("822219154245779456-L7dv1ojypj2Fc9sYfo8C5cKzEw8eQk7")
access_token_secret.append("ddm6ONs4m24wOUXFqvmgp1umthTEW0MTrBfHPIdfLRoMm")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001231 - user: msc2016001231 - e-mail: twitter31msc20160012@yahoo.com - senha: padrão
#
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001232 - user: msc2016001232 - e-mail: twitter32msc20160012@yahoo.com - senha: padrão
#
#msc20160012_322
consumer_key.append("HTy8RMoXD0oR9nVnSHj2AEbe4")
consumer_secret.append("ypQU2m7mjh3QqveBamUOy48eqHghS2wdbJeMPqFttVgBVtVWxo")
access_token.append("831846189331005440-iBxfn6ARDriuaF46hkyVi75lVCbC6G7")
access_token_secret.append("HsnDEWILRGo2LyWaAFYxyaelw4DIM7eVfBufKyqVo96Ne")
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001233 - user: msc2016001233 - e-mail: twitter33msc20160012@yahoo.com - senha: padrão
#
#msc20160012_332
consumer_key.append("xmj95uteaVOt77MHPC0q3LdUd")
consumer_secret.append("GKYTkFhdFuiN2V4lrmWi2cNKsjkO10NbITE7Wefm41YJoJXo99")
access_token.append("831849920944553984-agMie99QXOTuCNiJOY1F1MZVtF9f52e")
access_token_secret.append("PY0jXqmLz1M4HPUU2JOfi5halAWINlZmHIwPcW7s6QAKm")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: walbert1810 - user: walbert1810 - e-mail: amaurywalbert@live.com - senha: padrão
#
#msc20160012_teste_22
consumer_key.append("pPHJxZodM0fJcqO6rNOpgSuKX")
consumer_secret.append("PDJBEaHi0A255Ku5P1fHJzLkwgzWNZdFrAdoNRtjtxuYnuquu3")
access_token.append("786664983862083584-0DPtb9gb0L0V86AahLzsVCX7maUWU48")
access_token_secret.append("CQATIM33fPHoq9uEVXVbkixdOmJnotkntLAHzpqLUGRw8")
#
#msc20160012_teste_26
consumer_key.append("LLPgkLhjuofYvHyCx3fIKGtHy")
consumer_secret.append("YcZqLly88So4dw4ueRRB4wI0EBjjQeWcpw1kp5qC0FV3F5q0nJ")
access_token.append("786664983862083584-jDcOLSOAkNgEmrjbOjd8s5GrOrWLfFY")
access_token_secret.append("FOd7eHhgNw1PDYJgHSWaVaNrKgvAOr8R0r36pkooCD5fR")
#
#msc20160012_teste_30
consumer_key.append("PPmcT6Xr2rJu8o1n1cou4VuTf")
consumer_secret.append("LZLilaFA7NfGLNHT6fGlftIinrAtAtE1oIO0LJbZTe9vdhtNUj")
access_token.append("786664983862083584-v0oIbG2X7O8faRF0gPwrXkDlm1wU4Cq")
access_token_secret.append("p0Yo2r0kUey0N4cp6gQHaA1d5J8QTD9AtQ6w3KMts7Sry")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: amaurywcarvalho - user: amaurywcarvalho - e-mail: amaurywalbert@hotmail.com - senha: padrão
#
#msc20160012_teste_34
consumer_key.append("4MuJwZbOxwNIMFGYlbxGp7dfO")
consumer_secret.append("pz9s4lUAFJm8y1ikEbHyPkgB1cFVg3jZiDV94TIwqpJ8hx34mD")
access_token.append("781627388329398273-VrkEYPxLhJp7wbv0rbVXuo3RxPqz5Wi")
access_token_secret.append("den2GRsGzlVng6l9TWcXGjE7pWhmXX7UHK2qauzqZyPwF")
#
#msc20160012_teste_38
consumer_key.append("MDB1ZN9DiyysIgseJoxk8l4pC")
consumer_secret.append("27jRcMFQBd7DlKbQiYat3sEW3qIUCS19QYo8AmVOqHlJLfjaSf")
access_token.append("781627388329398273-DU6fZlQw3QyL5QTam5EYWAq09Q6llfP")
access_token_secret.append("P58l4fIJk2fb9qpJetQxvjOmGEaPeWeQ8O6TNU0ygDWXG")
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
