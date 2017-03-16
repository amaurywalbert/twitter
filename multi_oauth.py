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
#
# msc20160012_11
consumer_key.append("O4t25YPnHGNm7B1i5qaN7Gu3s")
consumer_secret.append("v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR")
access_token.append("813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi")
access_token_secret.append("VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB")
#
#
# msc20160012_12
consumer_key.append("R5iaxJ4FpLL6pcDOrr2osLNKr")
consumer_secret.append("PRNJxduOZgGsmjDlIeZIMuPF8qaauSxzYDlggdLWb1S3A5AOXO")
access_token.append("813460676475842560-2aJSRKgnhugK16w1T4AERo0pkoNtjxO")
access_token_secret.append("pSUfiFZmyb68U4YihPMFKWSQYKk2Js4cqGEgKNVbeS5xk")
#
#
# msc20160012_13
consumer_key.append("w9GvsiaQy9jcBDTKIaXomBjQT")
consumer_secret.append("H53rMVNGlrUvYFnN5f5ud1JzrGkhVpz2e335KBK413KrEK8Mwc")
access_token.append("813460676475842560-moOTo31XN8tbUbrKM3QOitihXsPD1Z9")
access_token_secret.append("aGuidWdVzC24kkUSJ6BNDxKRwUPchCz0LWtEnVINJShY3")
#
#
# msc20160012_14
consumer_key.append("cqRzqBL0fV3URMEvxnXl2sIxV")
consumer_secret.append("8mX8egarv1Wyw6EuPbF6vfegOXFtF3gj395fKKkX19OitcxCAo")
access_token.append("813460676475842560-A7YnIIk13B0ezrqtEXdaEMOIF08qxdi")
access_token_secret.append("Qb2YgSaJFFypqPjRxaBFe7hQvM8GyMKUAArcCvyfLpbNE")
#
#
# msc20160012_15
consumer_key.append("Bg18Yht35FNbKH153Xgh3awfQ")
consumer_secret.append("EA7s3UhtsbLBdo3srXwqciOOQtywUindvOXYoNQ0e3zOJk55JB")
access_token.append("813460676475842560-faCiUVzZ0k7lOVxEEiQLxAR9Te2jEdt")
access_token_secret.append("KBWpx4v2qYbpZcCOShDpFJCAzuHQHJtWlQtpyppjyDcx7")
#
#
# msc20160012_16
consumer_key.append("Qys38SRmmVBz90iioGWTSscJK")
consumer_secret.append("uhjDfaWQKkwHgwP4EiCx9XQD3egAkcAFF1dkIFQub6BFy2c2Nv")
access_token.append("813460676475842560-56PWNQlHVUYOlFw4tBBr5THeRD8ADlY")
access_token_secret.append("lrorUYCvBydihVI1gJytodrV3vYWuExjfQhALIAvzvWh5")
#
#
# msc20160012_17
consumer_key.append("HbJwp3WUsVjvBxHuDuKIQdc7q")
consumer_secret.append("uPflQdUndr8r95KPXpb9L3OmfFQ8HFJaB1XlsEEqka6L5Ytbqj")
access_token.append("813460676475842560-GQM6Bo4IHfmUUiRYln9VfqRQecOtBja")
access_token_secret.append("Je4QsyutTUTPhWkC9oA0ylviBKRywNKuu6IHO8B5CcB1W")
#
#
# msc20160012_18
consumer_key.append("mYw48LrblLQrVF6Y6rStxttas")
consumer_secret.append("66X76dJ7wUvTiHZSJq36ex7kLdaFzpfx1nJ6v7KwYe1HUtLuKu")
access_token.append("813460676475842560-m61gryMuRrvrk5mZS78pw8fwlVuev9L")
access_token_secret.append("Q9SDIHvf484Wq3KudGtnh9YsQHIOPnAKmbaYgQfXMJvbs")
#
#
# msc20160012_19
consumer_key.append("AbBex8ClaE7vEWOWG8C1WUtaq")
consumer_secret.append("X91do3pnXVp2UvaV183Ei04XDVS8CC3GNHwcHbDmJhQjgvKNzv")
access_token.append("813460676475842560-5Xj9GuFOcIGkiUL33wPs1eMcd90h5Oj")
access_token_secret.append("ICWDbDdnteGxxMP1OOAdtrPcfUYP4GXslPjR07eBGxKSx")
#
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
#		Conta: msc20160012_app01 - user: msc2016002_app3 - e-mail: twitter03msc20160012@gmail.com - senha: padrão
#
#
#  msc20160012_311
consumer_key.append("ykRNgT6LkUosDfvNRKPTzKdyC")
consumer_secret.append("NaY2Zet7YH1tWPHE13sl0JuW5rPfEg6hzZQFPCKiGmMNVbfvI2")
access_token.append("818810967400284160-jRZ7pSAkhOLohRr3ZMNN9QPWzfLDu8L")
access_token_secret.append("mxw9n10lJdQ0qEhsFaChkkj0rxm4zk3FDRyxx3IcU81jB")
#
#
#  msc20160012_312
consumer_key.append("7yN6pZvLxi7iTDq8pvD0bMiV1")
consumer_secret.append("7ITYoYSv2eWTDQxPIAZJk7jBD5Gm1iZ5gDl9QUMa3xk7b4QMMZ")
access_token.append("818810967400284160-PN3yDpaAXgnp46qECGG7nQslpkzMWVM")
access_token_secret.append("b0KmzeZVVu0aZLrSNVQqJlRz2FvMDmiU3ufwbifEKipQw")
#
#
#  msc20160012_313
consumer_key.append("pkCQIsm7ovuK9vsnc3AZ41WA4")
consumer_secret.append("yWM5M6CRq3zSCmwkmTrGPrVOfg09LKFwJX5EapAFwYtzpbT6Bz")
access_token.append("818810967400284160-dBOiPcMaMIuiFjAxCreWt2sBvorKEhx")
access_token_secret.append("XBA8HDkSamQJwIIiuQnaVlky74r5GozlfZgoETLxFaT7r")
#
#
#  msc20160012_314
consumer_key.append("3b5PGUUkR1kX90tbcZy4z3SWT")
consumer_secret.append("CaUGVUoFyUt22TzwuBD172CPZgxoe2xPcCIK6CACl8W8qy7g3C")
access_token.append("818810967400284160-CixkeUEz5Fe8dA9kdrj7dQlTUMSgZ5x")
access_token_secret.append("ptKyELguI7dlIpPMCSO5Y4338Cdt0QMfhQz0wafReQiug")
#
#
#  msc20160012_315
consumer_key.append("yLXjacffe6uLuonka5AXiEaAu")
consumer_secret.append("JP3h8Z1Zc3iRw1IibYE2aOv2x0BRMgAYuMdZnYY0nNz0aRAtS7")
access_token.append("818810967400284160-y8ertdAuwQsZJg01cN5b7sVmj1xGvd6")
access_token_secret.append("Vquwf49GKKaemroGSJZvbuYDHSRD1v2HCq4x3Zjr22AGI")
#
#
#  msc20160012_316
consumer_key.append("r1LoOuMAFXWPSnfoIUAksuOTi")
consumer_secret.append("jErxt6PyxtQ3ghej1OecwlpAWYJ1MB3LWQWfoxazQ8teBPfNQo")
access_token.append("818810967400284160-jQJaIZZraAiQHbzJPP1VAh1RtuBQnbx")
access_token_secret.append("712AEu6ZzFgjMhu91SMEjC9cVP3E7alByLtz0H9gAM8XH")
#
#
#  msc20160012_317
consumer_key.append("vNp26p6PA6cgrbPZg0gNtRnEW")
consumer_secret.append("0jbl3HVWQReVF3gCF2VEVDZOIDDIcGYx7b8vtAbUBXV9YF17cW")
access_token.append("818810967400284160-iGHMdbAON9ebEK1Hax4zhOi9EVcd8cm")
access_token_secret.append("xgyRO5k6No4ipLmOqliJmVMwkHjxH8CtxFKYV2rmCiEpY")
#
#
#  msc20160012_318
consumer_key.append("KiLZxnBOZcCUCcN0AesEHr9DZ")
consumer_secret.append("ztpur3OJCikJp7Ss4dmfcxS9cn2ntHu41dC0s5OUCecPQByT6k")
access_token.append("818810967400284160-gaQpQQZ6kBqVKUbdPQsK26vyoVqq5zp")
access_token_secret.append("0gzhPe0jagTpecol0ycID3Ev54UPGmrjDJkRxfQkbtv9E")
#
#
#  msc20160012_319
consumer_key.append("ODVMgFYI3qloClL9y13KBekYo")
consumer_secret.append("OZMoQNZDLs1feaqvPpgBw0zr3LrNt5lAxF8JY9tWcVDSEdXnL0")
access_token.append("818810967400284160-2wUIfov10ruLGLdIFNAC2lwaIF7Az8d")
access_token_secret.append("CFHFLmJG4SlHvBU9GVHlOH0LT5SFkNeaYMaUQBcpZg3Xk")
#
#
#  msc20160012_320
consumer_key.append("wBx27K0q8CnGPZHxi0Ayni3Lh")
consumer_secret.append("aarYF5ObrGm33izoPUnXP6J7eGAHMA5LloA7tUv4gnzxxbnhlN")
access_token.append("818810967400284160-7GTQ9cMWJzMGSQs4BNFRTrqcQGJPaqY")
access_token_secret.append("5Aqv4O21dnE3alufqo9Eb33OlqRSuCwXhJJg5svLr406n")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app06 - user: msc2016002_app6 - e-mail: twitter06msc20160012@gmail.com - senha: padrão
#
#msc20160012_61
consumer_key.append("cWJz68mRioD4KYSMQm3F6PbCZ")
consumer_secret.append("Oa1N0HhN2Ifd4qzF09TGVflqDndvs77LlJHTH2XXk16gOs6TqJ")
access_token.append("817489865466122240-JCAuAIB404lQZqmMMLHLP7je2QtfzlA")
access_token_secret.append("7rQV42SnR3I2S3GISugRS6a9LI5WMdymlw5iSIf6QXc6v")
#
#
#msc20160012_62
consumer_key.append("6ewIieHpVJoWVv9tTKWPDE5SH")
consumer_secret.append("41VrLkTMKVZQQlpBYCx1Gy0FRZUzHByTDzKcfJAhF4RPPHVxSD")
access_token.append("817489865466122240-YjJ4AOORTBK3NXt6ByrevyJW7pp4Nu7")
access_token_secret.append("74yrkCuTGmjxDq5mOMcFefuVCiuvXR2DKvpIMiGTG0ejM")
#
#
#msc20160012_63
consumer_key.append("TAhCnMYhMJ0WYDQTp7uOwgWle")
consumer_secret.append("DQ5Q1lCZba2QgpODrDwp4U5czVYxoDzufsFgn2Dh2kMaYgWcRA")
access_token.append("817489865466122240-UoZv0CH3zOShTuxwkMiEYdWqKBWuJEz")
access_token_secret.append("NpWqe0NBrpu0W8zU5Ia0ZNANtRxVdBkupx4zy9RYinNPG")
#
#
#msc20160012_64
consumer_key.append("fIDPTnu7qLmU6YrIMjkWMVCs0")
consumer_secret.append("4sPLcAYypmyjv6CQuj2tPppz1VTuO81NulwsWm2ep5RjLqs8Vj")
access_token.append("817489865466122240-gw5k153kyWx5n0CJcG4jGKc6NpKZJIL")
access_token_secret.append("w2b0koSevGiwoumLJqEuhxX6HkTu9b4t3WyBNEz17PKYj")
#
#
#msc20160012_65
consumer_key.append("BeCcqE6ipJqSYBhy7GnWGBcks")
consumer_secret.append("cJ6wSgYivxQx3O9a05oNhqc4kSYHZdoOgVS2OFSC16TmwOTXZQ")
access_token.append("817489865466122240-UXWudUm7B12ZvOgv9FLiHIo5vISfH36")
access_token_secret.append("7Tr0LMZNkHZuowNXv7Kl1gXzMwIaJCAO9ZfNOKdPGI0j1")
#
#
#msc20160012_66
consumer_key.append("6dBXMxR3IiYWOJGCvzbr3nNW2")
consumer_secret.append("af8aIJ7UnOMzZuc6UX4kRD2bDpdDRfI2iBl4Puv41sxdk3pIEb")
access_token.append("817489865466122240-4GVjnUtNtCAQFjTKbdyA2asmG31SfBO")
access_token_secret.append("zi5aIVCWEHb3SJdfpJcTQTY3o3ZnN6ESEzYqmNU6gh2Y1")
#
#
#msc20160012_67
consumer_key.append("ZIJI5WbVnKorxt91ri12XFTCE")
consumer_secret.append("mpHbISuDhsPNHvyGfdZcxXwEkyLahWa3HfjvjarXm2Y1vt0vq4")
access_token.append("817489865466122240-TcdJ0hWkTBMIi7h2Bddy0rfR4MzYoF8")
access_token_secret.append("nlOjHMktnck2cNg9cqEElO15tKMJw4zwXIFZzsOyRBnyp")
#
#
###############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app16 - user: msc2016002_16 - e-mail: twitter16msc20160012@yahoo.com - senha: padrão
#
#msc20160012_161
consumer_key.append("6Q9zSQDuB2niWPP1tSqRmNHUq")
consumer_secret.append("ZcueGOjB3JX1OcHyfpH2l5md4MAjjZFuPp2yfG15HYCzooAfBq")
access_token.append("821791002180616193-CcNmQuwjKj804wq2ikTQbAMoNlrfz0o")
access_token_secret.append("D5DQK1XZ5qBKq8EKmeev87NhVb1yrcNcQuuqHyN1fOKiY")
#
#
#msc20160012_162
consumer_key.append("gOneP6FyrqbEZ56E8lCci4PKB")
consumer_secret.append("8DM68yvq3ArctazNLLkYs3Y6Sa9FRenEfdvcdDCXEgv52zClpt")
access_token.append("821791002180616193-0YMau2WkvUdgZWAIsH97wOzmuohpVJo")
access_token_secret.append("cotwP5jKgcmu6t6PetJhzKINrGjuiySNSFTxwsWiUAZ1H")
#
#
#msc20160012_163
consumer_key.append("kw4IfkRywlDLpN9jnPsDzMs6f")
consumer_secret.append("8RcrhkhRbiDGF7TVkAEOl3jREOkRGvEuKIKbptmHYCPeurzLd6")
access_token.append("821791002180616193-Y8XI42vUsnhY1nbUaiQFHRsQQKCBAJ5")
access_token_secret.append("eun86FswGZ0Tl5rATmN7cKLnt4uxVyobUQekte0U1OJGd")
#
#
#msc20160012_164
consumer_key.append("wxlVclFSEa22LhVtHEyPhTJG0")
consumer_secret.append("366QCoLQypb7PqfBj9lGUuqtMs7Jup1JD8sTNRLm1a6VfuA9vE")
access_token.append("821791002180616193-p3O4838pUEjA3urMA7ARBwGLFZI3Tbw")
access_token_secret.append("tW9HiegHbWWpxzmoak8avtJVAbezBr4EOVYVC5SQMs1it")
#
#
#msc20160012_165
consumer_key.append("Cra7tO4yOm9qW9t9UL13Nkm3k")
consumer_secret.append("HqKf36lBsDAZAuZ6oQPUzRhzDHmzt7PWMYRPsEVzu35fizZEkc")
access_token.append("821791002180616193-K8pJSd2ruhkZRrFg3vQ1nNiVS8Zebv5")
access_token_secret.append("wVdMzafZd1P3c375XAJXj47mlZtC7qKvxCpvpag6DFeYF")
#
#
#msc20160012_166
consumer_key.append("M7brI84CQrt0HJ5PwOKS7rCva")
consumer_secret.append("p45NTNwpOJEFQZ8PdhEgo1UnLsVx9snqUCOfZnY8rHHzm9vhFh")
access_token.append("821791002180616193-N8rGfkPSViPvzQZFN38Sv13dUXlyLz4")
access_token_secret.append("GQh0qa7apkEHEkJqXEpihbwr0upKUcPZZrU3sy3o7CP1I")
#
#
#msc20160012_167
consumer_key.append("Opg58ZvVMasOz34vIA3pLUXY5")
consumer_secret.append("mT323A52OtKPkq78YZKf6Z0yihbntRuskopanmo9f3JcbZUmbE")
access_token.append("821791002180616193-lV9R1E0au7Po1vU7jZsXjF0lbswCmzb")
access_token_secret.append("tXgpU00dHYU0pGrlNAV5Ax27dMk8nLzM6ehyARtsyhuVg")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padrão
#
#msc20160012_271
consumer_key.append("tY71hkUKRrr9Bf94Bo1El5ozW")
consumer_secret.append("Xm3ZSg2zmCNSMJtx3sBeODkZkQqiLAFmkOi7KoTrcak00rLyHK")
access_token.append("822174289742925824-FzJqDAWIgRkJ8xR15BLQR9E8oJ7L3a3")
access_token_secret.append("bwD0p1lREYF9kSSiYp1vWXdKBM4jzAjW8ONJgCDXuT66n")
#
#
#msc20160012_272
consumer_key.append("2uPnLUW64bSaYLoair7dNr8X3")
consumer_secret.append("YNMXQjcNfHwQoJaaJNT1yad2innQQhUDSHY9OMYpJs14lBEj48")
access_token.append("822174289742925824-F8AHoJGLyPl9CkzjbSM1hRmquVaXu1p")
access_token_secret.append("DGvVZ1srkgB1NHMnU5DIBKvPyNl4GnowDezv9dIodSxft")
#
#
#msc20160012_273
consumer_key.append("PRBkeyXx8GntzlY1wprr0FmPZ")
consumer_secret.append("MY7wdyeyS9jwq0jk4NPKbOIr75AB0pnGJTkPzmyHd5SxF1o9Nz")
access_token.append("822174289742925824-mcHb7NDfPpMSibKgVKIC5KAxx622e4C")
access_token_secret.append("4g8U1XawXSlXmgaZwZnrEie3xecq78CEiV9OJeukdZmFE")
#
#
#msc20160012_274
consumer_key.append("mdue9ooyWiln1twkq3fevguEc")
consumer_secret.append("21hCCnT0XuWqByeGXaetNljMGZh6QCTJCCWmxIkDwSj7YcHiGV")
access_token.append("822174289742925824-K1gPcc6uueb594soemAg8b0FWf1fBsY")
access_token_secret.append("ZCz1kkRblLTrpBXG4LvkHbTnEnp4Upg1eTY8D35sKGbww")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001228 - user: msc2016001228 - e-mail: twitter28msc20160012@yahoo.com - senha: padrão
#
#msc20160012_281
consumer_key.append("1tvls7W6QObrPrSjGsqehSMgd")
consumer_secret.append("YILtV6oYSayKZtsdJhDIr7QKvtPSQdLxRlOn1vGyL2nudIBece")
access_token.append("822215581831151616-k9pPtsIYTvmqU9F3vyIzVn2qm2vgH6v")
access_token_secret.append("h0ATS5hOrXrIGwdML8jZkBGuh2hOYMBYmknMAFlAq9tpC")
#
#
#msc20160012_282
consumer_key.append("4iIGM7yv8VWfMHegwrydaJlwS")
consumer_secret.append("9fGG9ZGEzFLYg2CI8ZLcFqBmairuPUhEGahf0mllfJNKP58srt")
access_token.append("822215581831151616-rhZZPCcgsWJcEC2tqqmLCBE8grxE79i")
access_token_secret.append("GftUoNM7AbsorZeHF5YyHWnqsMf1ZdWX2idjmklgSj3Xf")
#
#
#msc20160012_283
consumer_key.append("GDT3nVD2v0fJ1bJ7vjIW0gRYD")
consumer_secret.append("yUhEwcvVEvQiH5LuFTS6DrqdQeS4GjAQCIosjLcY0YpwUzQUxv")
access_token.append("822215581831151616-sPq3ZkL2cXEHhK0yF2lSxdT0Ghufv36")
access_token_secret.append("86XdzFKqKgkZIxIvVNd2RSCDToGlrGk2BnBN2TOTjS8UZ")
#
#
#msc20160012_284
consumer_key.append("DRJbtfWrWCzYBwVBZI1Ab3pTv")
consumer_secret.append("BwN8tKYK3joF8ohQcSDronjOTjDrra9we6Ra1kfpyqESTZdsIx")
access_token.append("822215581831151616-0NMuIlNlLpEKPl7ODutzJux7ZnMxHjl")
access_token_secret.append("OMuhPznJRP9l7gTDAlJVKuhIFQArZ49vVK1qPdHTHcd1v")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001229 - user: msc2016001229 - e-mail: twitter29msc20160012@yahoo.com - senha: padrão
#
#msc20160012_291
consumer_key.append("a9QadNejWTtmI1FQeMGads8bW")
consumer_secret.append("1tfJGTXeXnaMdJaQtjwvRxtGe1WLGCV8BbrvIs6V3hqUukEUeb")
access_token.append("822217293006508033-Jj6Guy7R3v7TeghxadPWmEouRAn8YiW")
access_token_secret.append("jRhxUlWs57V1HF3Wdwp4cgGHg13nUGilsK3TxGbbpD3ee")
#
#
#msc20160012_292
consumer_key.append("C7k8eh4EjSh3VdoTBWrz4Ly8K")
consumer_secret.append("ACNkHDS2oEqp9psl4pWW2tPNdLeCqpIIEDd9k7sMkuiyCeIrqD")
access_token.append("822217293006508033-YViUgOdJSiAtJsFBR3I2redvkiiE97B")
access_token_secret.append("uuXMegPv60dhRKfNbknbQ3wMg2IwKDCYxmvCQiPWwhDAc")
#
#
#msc20160012_293
consumer_key.append("Yis0LeBkLT4ZBuh8IZSAfDWcS")
consumer_secret.append("NI7bk1zqypkRXEaSIdArdfKCOQ7lXyEaqgDWEaP1EjnvDgjWFh")
access_token.append("822217293006508033-34G9xsoCIviVmaYr4JTKrEDiVBoEuRM")
access_token_secret.append("veN3JgpOt6N66d8YwKyJe1LowQCvOjOglQ3JwA122XFk1")
#
#
#msc20160012_294
consumer_key.append("l7XognraVFg2gTmueSxZUriVV")
consumer_secret.append("RiYbqJ1iJkmZi4cFmJDUrph97lGtPru37BfIlaGiC9vjOw7YJv")
access_token.append("822217293006508033-XZKg5rWEQpZZjxFNW3wSmhntFaijyXv")
access_token_secret.append("Jxznb9SLpOBvI1FoZjAFekYvhF9XzW1EASJSUMwthVXMy")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001230 - user: msc2016001230 - e-mail: twitter30msc20160012@yahoo.com - senha: padrão
#
#msc20160012_301
consumer_key.append("78FsYx3VnphiSmMeGYNbuk3CW")
consumer_secret.append("m0no952gbsWt5ZwoNjAHGZ5uF30pyIdbQuYK978IYZ2eC9esME")
access_token.append("822219154245779456-K9hBIl3xDDzclfiYKiop6dcKhrbOopF")
access_token_secret.append("eXoCbIOsKylGjoIq95G6HYfE6AndfbxWLS9mB7jNppsRJ")
#
#
#msc20160012_302
consumer_key.append("xkIYFJprTE1sah8eP4DKzoHzJ")
consumer_secret.append("6pdEMTXZtPJas1A55EKcuEM3kRXZEo8GUf7ZGUTEFHYRP5Bo8O")
access_token.append("822219154245779456-pfBcFZFruanmEUk9ikuaHU2RBoPPgsi")
access_token_secret.append("qDB3P7rPexp8jcWns4BIKmOib2Cm4fR0eyFpKzMfSXOeB")
#
#
#msc20160012_303
consumer_key.append("u0iHmGkH4K1j4Fhax0QEHrx4Z")
consumer_secret.append("YkQ18k3TgaYELhMDAKM3hAZUyAqsrliNVY6DUivj6J7k4LrRxe")
access_token.append("822219154245779456-XAayNnIyExmRwTzeg3cR67vOi6CUeeP")
access_token_secret.append("dHTx0GsF2s2SXpQ7lJaV9w52xkBM7TiNmHncRdUM3wXdd")
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
#
#msc20160012_3112
consumer_key.append("gHi3JLS6iBI4m0c0UfmIHJ2as")
consumer_secret.append("bfswBVgKmSQXiVXx7gjbiNLmSF0g3BACObl920uP7eGSy7qXTW")
access_token.append("831843480565645314-7fdZiOYTK7gswBSWuZbrj48uNRTWOLT")
access_token_secret.append("snsI8xqdjEGc3HGBa5DWcZKRmUCWJtUujjbCDRfTiMPbO")
#
#
#msc20160012_3113
consumer_key.append("qqECHxNz8E0z3UXWENHKJRAhU")
consumer_secret.append("pv77SIwPwKgYByr6fjIrAvyXcj7xWep0ElmIY712WxRaapFkqE")
access_token.append("831843480565645314-7Z0ipwQwjfSBl3lb2c4C1iKtVS4aeOp")
access_token_secret.append("FNzO9FIkNpQfbKkcXUt0d7a2Oi8EuYZWthh88OtSTVNh8")
#
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
#msc20160012_321
consumer_key.append("9HwvjhRzlNWS16vZcNBg1VRI2")
consumer_secret.append("88xa1rZsxCH88PHNFYEOaGVyRKtEFRzGitCtKktafMZ1kO8U38")
access_token.append("831846189331005440-4G7Igh8nQ0Jaf8rBNG4nJCIODE69p7Q")
access_token_secret.append("yIYSFtIcP1TLCzDepD4JKx0CCUuinYMn1MP0EBNUDipq9")
#
#
#msc20160012_322
consumer_key.append("HTy8RMoXD0oR9nVnSHj2AEbe4")
consumer_secret.append("ypQU2m7mjh3QqveBamUOy48eqHghS2wdbJeMPqFttVgBVtVWxo")
access_token.append("831846189331005440-iBxfn6ARDriuaF46hkyVi75lVCbC6G7")
access_token_secret.append("HsnDEWILRGo2LyWaAFYxyaelw4DIM7eVfBufKyqVo96Ne")
#
#
#msc20160012_323
consumer_key.append("2mKNKdnpvcQ2bpMfY0DoYcNFl")
consumer_secret.append("s9rYvgCCUWzn4WP66zK0uKfImbdvNi0KHHkTHMJO0hPCJqwY8q")
access_token.append("831846189331005440-T9s3eslLBirsJ3chzjk3dU2vVxsQNKf")
access_token_secret.append("rsLeDdpNx9EsA78jy0jTY5X6bAGhcMjOh6udgndcqDd1F")
#
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
#msc20160012_331
consumer_key.append("3gdXCHZ8T43pOmZcBVt86ttBf")
consumer_secret.append("vnoo0P17s7iJ0Qh4jh08FRUzP3FF3cEr1fgcSQNndsFdYpxTTs")
access_token.append("831849920944553984-els3pI9zCLz1c8D3FIrfpHqo6i58b44")
access_token_secret.append("sRs5nE5F07k7Pw4LlWycPcIiNRgMYE94ti3zbVoNUerlW")
#
#
#msc20160012_332
consumer_key.append("xmj95uteaVOt77MHPC0q3LdUd")
consumer_secret.append("GKYTkFhdFuiN2V4lrmWi2cNKsjkO10NbITE7Wefm41YJoJXo99")
access_token.append("831849920944553984-agMie99QXOTuCNiJOY1F1MZVtF9f52e")
access_token_secret.append("PY0jXqmLz1M4HPUU2JOfi5halAWINlZmHIwPcW7s6QAKm")
#
#
#msc20160012_333
consumer_key.append("fkcEAzeKWqMEwZnX5cBP1QQth")
consumer_secret.append("FhtIIforvA6f9egJdftCKaG40xa42JqAvYqAgRoN8SzHrVG87y")
access_token.append("831849920944553984-c3qVnCicXPRAn9wnDbip3KMbRbKzdPu")
access_token_secret.append("GlGul4iMwYVGYrBQJsqQvtx9YUiOAw5plf1OSaBG0g8j5")
#
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
#msc20160012_teste_21
consumer_key.append("qvmfyEldFvEmTCAvzFSBTP1wz")
consumer_secret.append("L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA")
access_token.append("786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0")
access_token_secret.append("in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ")
#
#
#msc20160012_teste_22
consumer_key.append("pPHJxZodM0fJcqO6rNOpgSuKX")
consumer_secret.append("PDJBEaHi0A255Ku5P1fHJzLkwgzWNZdFrAdoNRtjtxuYnuquu3")
access_token.append("786664983862083584-0DPtb9gb0L0V86AahLzsVCX7maUWU48")
access_token_secret.append("CQATIM33fPHoq9uEVXVbkixdOmJnotkntLAHzpqLUGRw8")
#
#
#msc20160012_teste_23
consumer_key.append("VMkcoyd5vate9jLbW0ze6yp0a")
consumer_secret.append("XsDwoTCE2AhiXeRyNu38XhcxZChE44kl9ED10U5BA9vzKWFUpE")
access_token.append("786664983862083584-Zii8faTHCNUSLv9SjYNasYZfUFIMkZy")
access_token_secret.append("TFMiyIQfTv25M1UXdV8XUHO8La3Pk0F9BI2og8qAVPBhs")
#
#
#msc20160012_teste_24
consumer_key.append("UNwhnaGwIzjeNIb9p796O4cBl")
consumer_secret.append("XkyvDXE9AiFdgd6bjiyeyvxgqgitIgsdRrRAZbcfGx74GHOWsN")
access_token.append("786664983862083584-BcES2YdF1jjCl7Hg2vumGfPidwyxZTT")
access_token_secret.append("iPkexY0o16DejWq5MfGs8uR6UeloY8koblw3cOVVP1FC6")
#
#
#msc20160012_teste_25
consumer_key.append("sVAP0Oot5Oy9DGvjcwxQPRIPc")
consumer_secret.append("5R1p6nZe3n1akSUUz0rPfa8RakyKi7C7UnlBPs4NqgSi3IQxkt")
access_token.append("786664983862083584-8I0z6KT2Q9gifwhfRP7eBDBRLTtzlx7")
access_token_secret.append("BC2TxS8m4nxdaSm4KS2DVMyvCZwx4Tbhv95tMrvubaosl")
#
#
#msc20160012_teste_26
consumer_key.append("LLPgkLhjuofYvHyCx3fIKGtHy")
consumer_secret.append("YcZqLly88So4dw4ueRRB4wI0EBjjQeWcpw1kp5qC0FV3F5q0nJ")
access_token.append("786664983862083584-jDcOLSOAkNgEmrjbOjd8s5GrOrWLfFY")
access_token_secret.append("FOd7eHhgNw1PDYJgHSWaVaNrKgvAOr8R0r36pkooCD5fR")
#
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
#
#msc20160012_teste_32
consumer_key.append("U7NBO7duqO1aTZ81q63Hy61Er")
consumer_secret.append("kVKISoiaUrw1gBAZpTLPJ1op8GfONmHULeTMG01Ofj2OsAMkOg")
access_token.append("781627388329398273-lrXG081wRlkvHpYAPO0iS77p3fGnijs")
access_token_secret.append("cR71hKrAb4zZIyZqGIwDuH0HMnC1Z7BAwN7MKEfe7Uhg7")
#
#
#msc20160012_teste_33
consumer_key.append("k2X1NYSSfLxqbTElsaJoamTpA")
consumer_secret.append("ywBx5cyqHmKrFtziklEgtzAJKHTtz5ORXAFNvdEcIyyv6KH9uc")
access_token.append("781627388329398273-CkaxgovlocA4s2OVJdyyBwZh495uIZM")
access_token_secret.append("i0zSthAta9HIH6dNTSlVrLQnrsBt1fVM2cjpFQIpFmBx0")
#
#
#msc20160012_teste_34
consumer_key.append("4MuJwZbOxwNIMFGYlbxGp7dfO")
consumer_secret.append("pz9s4lUAFJm8y1ikEbHyPkgB1cFVg3jZiDV94TIwqpJ8hx34mD")
access_token.append("781627388329398273-VrkEYPxLhJp7wbv0rbVXuo3RxPqz5Wi")
access_token_secret.append("den2GRsGzlVng6l9TWcXGjE7pWhmXX7UHK2qauzqZyPwF")
#
#
#msc20160012_teste_35
consumer_key.append("E6hDM7RUR80CSKAaB0sLBC9iN")
consumer_secret.append("m4vl1r3iHoF8ccTcgpBAE88Ifr48CICTOF3Tg7YmCximTb8jsv")
access_token.append("781627388329398273-pZ9X470f9us4YGI9VxxEgPCOaYzmHTh")
access_token_secret.append("o9tBTTLwHRmGZWPV7uVVIfkbP2vTeWKiQz8lBSeP6oXMV")
#
#
#msc20160012_teste_36
consumer_key.append("mAeJK5IAQjo7JXvvze5twWZ1s")
consumer_secret.append("qWcO3E7igA6wASmM3lR7Rn0sYf6GMEZ2thCzM4nYPSqk9DBhxk")
access_token.append("781627388329398273-ODQGBx11UGaHfHkwdmPWQCq25zhGg2Q")
access_token_secret.append("SxwxnHaRKx7sXjAbdAJQSLIYDrVHSHJfAyi1rfnY2YCiv")
#
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
###############################################################################################################
##############################################################################################################
##############################################################################################################
#
# 										TESTES
#############################################################################################################
#
#		Conta: amaurywalbert - user: amaurywalbert - e-mail: amaurywalbert@gmail.com - senha: ----
#
consumer_key_test.append("JeSUTJXGauV6RY7i6RJDSRvoL")
consumer_secret_test.append("ZCOMtPUTAJPFuEwm8S50wPIGF0CpVVFRJIQauy1DcSZ4w6v6ox")
access_token_test.append("41112432-fRQMmcN5D6mSgg8kPy9oNZqDRSujUkCjAQcPgwHOb")
access_token_secret_test.append("FxU83OnYRfr6eU8IWuj5pP2SviFsyu2UHAaGMJqjyD6a4")
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
