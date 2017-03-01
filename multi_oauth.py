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
#     Conta: msc20160012_app01 - user: msc2016002_app1 - e-mail: twitter01msc20160012@gmail.com - senha: padrão
#
# msc20160012_01
consumer_key.append("ffap5ENG3yu0u7phgdhQzIvJx")
consumer_secret.append("bFXgZjBUGMRoSfxbKLNZG8Y0IqjUPoc9O4vgKOtUCs0WSlkT6s")
access_token.append("813458922967302144-f3aEkz6OsueSD6eCkaN1yYXVcYXPGuZ")
access_token_secret.append("OG08x1kx6rgMHwwEcmQKeeEAot88UALSQAY96XlGnpRba")
#
#
# msc20160012_02
consumer_key.append("L8LX4gmyLYpfaUDHPRTmAnO5E")
consumer_secret.append("pCte0UiHaPIBbReSTTFm3pGV8mlS9L7b28azjIZ8vr7Sv320m4")
access_token.append("813458922967302144-wgByKpL2mDieJRbLrMbKxDySesoSHSS")
access_token_secret.append("i81wWiwi6MWNUgg8CHz5Z0S9zTUWSq3cSvmy44nBCKPE6")
#
#
# msc20160012_03
consumer_key.append("io8o8D4rdUtPiJ2J5mhkkXFSb")
consumer_secret.append("hauZhqzQvh8uI7p66fy5ztn6IINJP3PecaqkoTob1EGOV23LB4")
access_token.append("813458922967302144-dk9pCS7wozrKR6kAUzqjayX3KkcB6Hv")
access_token_secret.append("g6dZ0iDxLRb1gGTjnrBKMjhB8FB7nnOBpu9XMkCNGBSAb")
#
#
# msc20160012_04
consumer_key.append("cFEDQtQtsib0TVq0EtvbBddl0")
consumer_secret.append("gCUAkk3VmplqhzTAtepo5kjFlVcr7LXz2vNsYLApMSh1ogF9O0")
access_token.append("813458922967302144-3MK8AazCmrtN7IMRnPxxZC56ax5R4Rk")
access_token_secret.append("L4Y8IdrHi44rRbcei5gFNoYbdU8C0TBADLFGFXZNu5IXB")
#
#
# msc20160012_05
consumer_key.append("low1J0YxOY1k2WRYOIt8z34T8")
consumer_secret.append("asMb1Gtp4xnQrMDDq2r2PPfxQKJV5iCN5zlU2giXn20JNhiHt4")
access_token.append("813458922967302144-FdwjetAGA5JRuGf8dKhTVpzlRFdsZYq")
access_token_secret.append("wF8txP7Fnd6ZTKT35EllN8Ei67PxSDkeHunE7UPRBcjRi")
#
#
# msc20160012_06
consumer_key.append("Tc60Yaylx3IxLHlYJCyeHSP7C")
consumer_secret.append("6WhSsg5uyZUx6HnNJqpsZqi44tkSKqWO5VQeDoC20cdKsk49za")
access_token.append("813458922967302144-hPrwvRvzIp9WtN8CoKMLWO5t42GSJrd")
access_token_secret.append("evzncdyFsUdRKbuyOd2W9peqw5AxQVlYg3k51goVzKbaZ")
#
#
# msc20160012_07
consumer_key.append("5iUqKfKFhZ1hzhUI4BD9mMzbb")
consumer_secret.append("XZhPHgSpyjJwkc33K9Co9myAQutq3ZAk4D9c9IwWiOsb4PoMqG")
access_token.append("813458922967302144-zL8yhYTF5EpVZ1RkjoOnuuMd1dXOPyZ")
access_token_secret.append("lussrypwzCzCbUGhmtOmSAAQdD3ZlQ0Y66wgH6OhivC2n")
#
#
# msc20160012_08
consumer_key.append("az5P7VWwgZ8QjrKgJXRkgvx3G")
consumer_secret.append("aFC4PirBD8sSCivUdAigin2NadWe72WSAzf54Sh9Ycn0mcj8Ty")
access_token.append("813458922967302144-ZDFxI0vTspgEJJAF5LSjWXc4mDZDYKm")
access_token_secret.append("HL3O2iMRyoPiz1kjlH20Bhl9j2npRY2XMrcarcHn5QTUR")
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
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app04 - user: msc2016002_app4 - e-mail: twitter04msc20160012@gmail.com - senha: padrão
#
#  msc20160012_411
consumer_key.append("ucydTwduaEHj7CEZtwhqPyoY8")
consumer_secret.append("2bJhRTsRQvFWyI7xLi97SByjdAcD563UcSEH2mzXWis11OUas5")
access_token.append("818814560941510657-YS7ZG8CdGOarEhialSGqZ3HR8RDsi8j")
access_token_secret.append("9sInZONslZMldFYpV5e0u7B7EyQVBERXgi15pCGir0wXL")
#
#
#  msc20160012_412
consumer_key.append("IF9G3dX79hJeJwOY8RKNnGGaa")
consumer_secret.append("Kc0V7fEj7UvOC6askVQIzcfNpHrsn9uGASFY6XJqVNKCZxCfH1")
access_token.append("818814560941510657-mWXynOOZYrSqfCACbNurPoq4ZXa54GL")
access_token_secret.append("s3oKz0Gm2ZqrgX1zw4vwmlurE7ZCVf7WlZpsmMosMsF5Y")
#
#
#  msc20160012_413
consumer_key.append("RBd7ANwMQySSlrgzFh32XSrb6")
consumer_secret.append("Ffc4dtyIdJwjlAZAZ8gMxdF2lpUV0jbshnjjIVg4P0U5FzOsjD")
access_token.append("818814560941510657-ZAL2O1CfoG1MbnZ9G7CRYeImbNQa2E0")
access_token_secret.append("H3gg6he5bZdQXrvvNHIKPkjhho5ixxnN09wY1v0eZCa9V")
#
#
#  msc20160012_414
consumer_key.append("wvilMdWL8Br79v9BF90D2vY0Y")
consumer_secret.append("kB5lG4TzcQh6LsIEqeZfIcTYMkyxn81U95HYJ9VKuKeypeW1LB")
access_token.append("818814560941510657-y6E8GtjkFzwHyNWPiTng2oYLJGGlJI6")
access_token_secret.append("UQUOTriTgLKazLlFr5EebwzJfmz7qegIWupOrITP0Ndo7")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app05 - user: msc2016002_app5 - e-mail: twitter05msc20160012@yahoo.com - senha: padrão
#
#msc20160012_511
consumer_key.append("VNxFdDgMvx4Dge4Q2afZt7l45")
consumer_secret.append("o1mIoWrqmbTDbEhUZaG4VqSBGplSSZo9OlM4rwFn6SwqCFSlRm")
access_token.append("819401695310528512-JpY8ntd3tBrTNSFOBDill7p7bCHpKSU")
access_token_secret.append("WpqOpdGjlWpTu7nvrG1Yfsp0jCKah6kQrMDpeZCp7LxBw")
#
#
#msc20160012_512
consumer_key.append("D9Q0PFfj9N1l8YZcDSl93s5Um")
consumer_secret.append("UdhEmTCCTU5hNaAgbNAqDLlIcHsRqfwRs2Urc2rXQF22isLRXs")
access_token.append("819401695310528512-3SBW4UNFvUX4gonqfc9X8ZpB8hpKR2n")
access_token_secret.append("aB36UQmpmNbk8ZaqVHNHUHXTF6ZDvjKNgnJ2NfoyUn5Vj")
#
#
#msc20160012_513
consumer_key.append("ZnunMyuwmk8ITZ4oZzjfkk197")
consumer_secret.append("uvvdaHcfAUrt9iFvcnVfa6Oe7zeg8ESXeKy0eOKokXVAegdI4z")
access_token.append("819401695310528512-OppPizwNthGiU3OCay7Iwdynjku57Bx")
access_token_secret.append("ENH7gMQqmu0VJrxUfFpTusNiOJGE0nf6C9iTJfRORQaAZ")
#
#
#msc20160012_514
consumer_key.append("KJrWByZQxJ3DpGsC6SzZlgiJR")
consumer_secret.append("sUh8RC1f6IK752SQlhx4KW14AfRpV7hp6netogNy0PCjPEh28Z")
access_token.append("819401695310528512-e9zuOFVhdIcA2ytfcjRwvvjmo8eLcDY")
access_token_secret.append("hNuXZmjJt68CsTwGy14m3pan5cTmTanFvvnVIwZFcz41x")
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
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app07 - user: msc2016002_app7 - e-mail: twitter07msc20160012@gmail.com - senha: padrão
#
#msc20160012_71
consumer_key.append("4GpGgwHB3yeeZ8aQIZD4LLqre")
consumer_secret.append("McX6jmXUPHu4eSTJQ41U7VY2q24mLJP5ZUcqYB4ovc2EoviOXH")
access_token.append("817492701889392644-Wji7oss1KCawoGjpGyy1KzlBHmAFCW9")
access_token_secret.append("gxP3I5k0olOqEMSn5kynVfDuHgPNgo6ynLskobwj3P0wg")
#
#
#msc20160012_72
consumer_key.append("5kXbObtiQSWpD8AMq6AonSfww")
consumer_secret.append("C8Tl82Ka5IUbTiYfDc3THPxpFjmBrAbdh7bT1P8mrBXsZTQNTl")
access_token.append("817492701889392644-0tk7HFpvsJVnpBRbbTHEdDN6Vp2t4lX")
access_token_secret.append("f8N6zT21l2P9uEy8KcZlVlsh6lHK9m3eHcoAYaGTMTxiI")
#
#
#msc20160012_73
consumer_key.append("DCh0S2Qx00tmOUBvkRGYWFjXy")
consumer_secret.append("WblZ2icD9SZoMbvIVJuq779tnBEWfUceHY05hDFAcXPVNhTyzi")
access_token.append("817492701889392644-bCXJTMAjYW8kwhVdFtYEBwR8b33uHX0")
access_token_secret.append("VujqULnMchv1sbUEJRW7I7jKhqFDsk4st6ulS5f9COnF8")
#
#
#msc20160012_74
consumer_key.append("o4RyHVvoR3MAJP7JxTFKOoP2p")
consumer_secret.append("fshwqvpyudhi2nO0rak5OAsVB0V4weEFtInY7l8dcyUkN7ET8m")
access_token.append("817492701889392644-OU6ioZRqv5gebFuGL95uA9A6Rl6T0Yd")
access_token_secret.append("5qqFXQirxTWRhJKg45E5eT0NhD9qRY2pIpJ0sdYhsJoj2")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app08 - user: msc2016002_app8 - e-mail: twitter08msc20160012@gmail.com - senha: padrão
#
#msc20160012_81
consumer_key.append("UzOedM4QmOsM1xPsyPGLc2OI4")
consumer_secret.append("B1TeVvnDgzxvMSjpg5bldlmSTid7C1UusnPmss9tMfvQVgFiCu")
access_token.append("817494567599611904-fYac01KBzyq6vgvMHKkb0AkVHm7SBFS")
access_token_secret.append("9KnAZWjg3xq2mu5q3l6Hfqj9CM3neIzOFLdB4Fnb2ZLsZ")
#
#
#msc20160012_82
consumer_key.append("CiYHYhjTOInNv5eQE0tsD8hFa")
consumer_secret.append("jDRC5JvoLCdcvlVmnjTTVakAQfxgFPQShSRlk9FGZqrPt71Jhp")
access_token.append("817494567599611904-2BeCsTgMbceM1GHq5C2dIga7NwmKKnU")
access_token_secret.append("oKNJfw3Z00dKAVsr2QcJD2GZombgqmK1rvMUKzrQYspIe")
#
#
#msc20160012_83
consumer_key.append("vbCJnYR5mEzZrX6JSN8UXyKEe")
consumer_secret.append("18gzHPCb3FWThN6tRqolP0z3w73PvsVEHkSv63Qq6GWhdNApOd")
access_token.append("817494567599611904-dmpxuyRRWKwqf4BJO2mCRCzhUbzH7gb")
access_token_secret.append("vyAAzoJ3hvo4DQ5On896vHrdCESulAYpaef0ogCRuEUCu")
#
#
#msc20160012_84
consumer_key.append("V2d9CnBHjRedL2h8lQTTF1jA7")
consumer_secret.append("IMEpHxhxZSG9QIgzTWI7menbXimTkK7NN3I8W9RtU6pDihoYrb")
access_token.append("817494567599611904-MLe4kUO59RjGemBZps6ES1nBIMhsLFL")
access_token_secret.append("gJIgjKhKotIeH3Mfvw4clMstAhNieEIYhq6g8CmHh5lzi")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app09 - user: msc2016002_app9 - e-mail: twitter09msc20160012@gmail.com - senha: padrão
#
#msc20160012_91     
consumer_key.append("9sz6NkdPOIZyVM0W7qm5vpTqe")
consumer_secret.append("stQcxPa5gRCuyDPC4A4uvRNQxiVlV15D2cTZbyJ8Jo1wnj9HJo")
access_token.append("817495894312493057-ofFWm7CqEbvSPSOKNVHK66BNndGF8YR")
access_token_secret.append("13sJjnbfLcJZ76PxIC16bzg8GCSleImnuMRhB1D4TCf1x")
#
#
#msc20160012_92     
consumer_key.append("PJeHbJMxNp1RbiC44i1Gsx4g3")
consumer_secret.append("UlloQmWHXPVqXNMbbMsJhi06cbaQR5ZjWsOF3fitoIUfSO7wWj")
access_token.append("817495894312493057-I15pzxX9tLr2XxhBAjrfMcB4v0qUdT3")
access_token_secret.append("xGrrEjtRoq7yrcXoF6ZnHr0IxRInRTim9Zd9b9uKKzxYg")
#
#
#msc20160012_93     
consumer_key.append("zooZ5ibIysPQUbWTl6jMP4rk8")
consumer_secret.append("kzs165AqHPH6ighm8NfM7epqNntKuPHul4tsEP9vryDkcUEMNk")
access_token.append("817495894312493057-7LxbU4GK0R9sJdOJuQPIJcKnSfZfnKG")
access_token_secret.append("BkPfW9peZ3h3bo4BqFBzt5zt77cHihlkk27RXBRmLYrQz")
#
#
#msc20160012_94     
consumer_key.append("0EjyRKu7LklLgZhomskGpxO9w")
consumer_secret.append("XCrLBMs1ibTDQn6iOUw3eJhLH9sPASVCs6Ao7QYBR6BvM4Bt7d")
access_token.append("817495894312493057-PM3qa63mpCsseaD5fQhFNEAjOaiQgpH")
access_token_secret.append("jW6ew9Rrke5ztMfHi1RXtUk1nD8DWsBXWndwJ2zWAerMQ")
#
#
##############################################################################################################
##############################################################################################################
#     Conta: msc20160012_app10 - user: msc2016002_app10 - e-mail: twitter10msc20160012@gmail.com - senha: padrão
#
#msc2016002_app101     
consumer_key.append("J7K2Q9iVzQQddGCnqvLObleBu")
consumer_secret.append("6NZUZVSN81EmFQrNmUAbJgIMcMRCDllZd728Px7oB4z8vdnvHV")
access_token.append("817497484285145093-aAm3Yu7lgIHkrf40bdKMvYBgBw8h0eN")
access_token_secret.append("Ob6AG1A44N851XOvPrXDDfUo5EjYM1W32kAGkIJEXrS9F")
#
#
#msc2016002_app102     
consumer_key.append("u6Qh4L8oLDINTl743zps4jSmb")
consumer_secret.append("iZprT4mlxrKeKnp1WUAcyGjYfDYkEgC6FAzu7H1H68GYqZfMMX")
access_token.append("817497484285145093-cpyWNWhMvAUkAWu4opV96hNtxMSRQ4g")
access_token_secret.append("PEnlovnA9927h7NUVkt0YE5aYHUJqkHtPS3bBZhjYlvvM")
#
#
#msc2016002_app103  
consumer_key.append("H5RMgw61jbOOM3SnJ5TJQCjnD")
consumer_secret.append("OmvpHkMOHUXdO7uwxxWqzCkIjbnqndXC4vuowmh9HVCcurvRfi")
access_token.append("817497484285145093-AzOaqc1LFq1pFZXp7eOcjShL40cBN9p")
access_token_secret.append("8FYI88ILqbTuJaOGbuqDvBRvKXk040LYku3rzMRSz3uKp")
#
#
#msc2016002_app104
consumer_key.append("g9xt0sgY2vGWFUwfJlYShvR0u")
consumer_secret.append("LUMT6WQv7ms2PdcrlfWclCq4A8pwQqwQqUlPIz2T6uSM2BtNNN")
access_token.append("817497484285145093-oYSvc8PvpOvdKLkncRiIgIkMIQdKagy")
access_token_secret.append("MKMADnoR8ER80ilBjckDdK9RcIgkDxst3QTf1ojl04sNO")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app11 - user: msc2016002_11 - e-mail: twitter11msc20160012@yahoo.com - senha: padrão
#
#msc20160012_111
consumer_key.append("x4qzrPEvZvWnTIu3X7rVFwEVQ")
consumer_secret.append("PqenEfheKBvGob3KHLNo19yT9wBE8uNrEb3b1zPIY2YLeKN5J8")
access_token.append("819405209613041664-c0GhzjbnZ0vHRDqcYxDPy4mxYzYjlwX")
access_token_secret.append("vdGJMLEHYAjbVVu0SArUhdhzJpYv5ItfPh6tpiDuONzeP")
#
#
#msc20160012_112
consumer_key.append("Ke8wkUNWxaI1oA0BfZdYum9V4")
consumer_secret.append("zyY0Bxq73NNmDsEguUZPwFXsKR633wvAyveKGAW9zFTcqvw8VI")
access_token.append("819405209613041664-2kzzMASDXnaJb4OvVyglQAPJ4rUYTtO")
access_token_secret.append("AFdlqtMxMVhaDi8B0efefsqEMrcbFHAz0moZ1UjImjQzj")
#
#
#msc20160012_113
consumer_key.append("KOTzHTGpxJVq9Nsmxcuc72EKL")
consumer_secret.append("CYdRuBwW3zJJH3qaTUAoojyBOEExvWwrWYflTGYhhnhowMuhqL")
access_token.append("819405209613041664-4WlhbAjU7Y7RXvRT1sagc2qCsnlhzip")
access_token_secret.append("qTJowQWKjc7ut0OC0WHlPbW5KYW0o3XoPKoHMWT327yby")
#
#
#msc20160012_114
consumer_key.append("svsWFcfmHY8WKrtj71Plg1KWD")
consumer_secret.append("g4ur4QOTCM2p5Rv6kLSOquHyXpBkeqrHmnDIwvl12U6wCrxVwi")
access_token.append("819405209613041664-nRGCLeg0Vos1k55C0PKPHGTdElHnyHS")
access_token_secret.append("ECzAoliijgg5LGY8nnnN48VSrujPZLfqKEy1r3b4pXG1q")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app12 - user: msc2016002_12 - e-mail: twitter12msc20160012@yahoo.com - senha: padrão
#
#msc20160012_121
consumer_key.append("t7TVuq57clRC046ZmNoJUXhzb")
consumer_secret.append("GiXWW4zZixDDNE5cnHI6AeO99nEIPBuOUJZhMvk67sbsP1zqdk")
access_token.append("819407030817607683-1bbPqcbZA4ZlnaPizrrJpM8FETlYB8v")
access_token_secret.append("a0PKhTisi9oBTKmXsspv46t2lNrYoC9ewaOskZc0cuvRJ")
#
#
#msc20160012_122
consumer_key.append("0YJxep6ewkNHPWuuPPlN88MGK")
consumer_secret.append("LOoMXd9amxCUqlRJqW7PhtgzdcTHboXuHUHKQg8bJsaMJ08U3i")
access_token.append("819407030817607683-lAX5dMEpwkJf0FSZcB3KvohntnUk0A2	")
access_token_secret.append("FOxe1Srk1TrqKF4vVPY9lsGQZLUTB2Tcm5f2QjMqZVTxZ")
#
#
#msc20160012_123
consumer_key.append("q2IAGohh8retpeCUWUY8uQeN8")
consumer_secret.append("SPMe7BuL2UKKBViHoTzf5ObNooYhucnUrFl95c3HYvUo3fIZNg")
access_token.append("819407030817607683-h0sAUuc6mAYOxGQPcVl35EEhBtcpAer")
access_token_secret.append("alsLOS08K9N4pzjQDC1315M8CcPMrlxBHISWEHbmhAl4S")
#
#
#msc20160012_124
consumer_key.append("eKCOQegT9C44bz7YcLWNiySuT")
consumer_secret.append("8vWgSR2CnntuZoTjys1IKWE5jNU6jkFiwgJwhmy3dcjKgrMhBB")
access_token.append("819407030817607683-ZnSg7orsEgG1yH87TsN3ClDRUpggSfv")
access_token_secret.append("fxwnWwVuhY4rz0cIu4uZ2YIQtZvtFiw1BIyvw4yotF4m3")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app13 - user: msc2016002_13 - e-mail: twitter13msc20160012@yahoo.com - senha: padrão
#
#msc20160012_131
consumer_key.append("4cxE0wJ6x1ZqjsNnjbBjQ1XxK")
consumer_secret.append("FDD292IWBEpk55sd41RehOxcC5sKAqXw4RXFsUmykTG08FWoPJ")
access_token.append("819408960520417280-Ia5yrwwWRJjZakhXDT6UkkZon2LpEgc")
access_token_secret.append("LsWru0bh8fnLXrho8jfJYbjEz0gYddqX4JOpUE57EsPL5")
#
#
#msc20160012_132
consumer_key.append("EVa6lC9BLlfbW2i8Pm2aYaPCh")
consumer_secret.append("qSwN6jOuRx69dz41utklLo4BSRvxdBdJnL6vwX3prY1KDoObG3")
access_token.append("819408960520417280-o5XlwBiRME5g0ox2tkbfJLXqATFoPpT")
access_token_secret.append("kMxXV5VSxgFYqSp2KWioL4yYq89RYuXpdBZfAzpn4WzGy")
#
#
#msc20160012_133
consumer_key.append("5zKxCmISZdpaxRPan6D6bNG1C")
consumer_secret.append("LSJmuMTpmBgqmEThkD7Ngt6hwzXT8T7pFeoTSzuD48R7tZFFrj")
access_token.append("819408960520417280-udiHF2kDovtfjE1GcZyk9MOZ3zzFF3d")
access_token_secret.append("UCfD0vOIXktZr7leSNlTniHAxgJo1R0zIS3sU0oV8T0gP")
#
#
#msc20160012_134
consumer_key.append("lkBxh1mWEPwfxIt3vBQKhWBnV")
consumer_secret.append("meTAVwFkzb5rrBiOHoxWgcn89VJtHzWkXNwIvR0kKPZWc7d3m2")
access_token.append("819408960520417280-jSoJTSIqHFJ6UevwRb8qDDzHHtiD7YC")
access_token_secret.append("8Xcqlv9ZsfuyjR5cFcMR9v0BI4mCGQUQKFsKt1gbOBlEn")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app14 - user: msc2016002_14 - e-mail: twitter14msc20160012@yahoo.com - senha: padrão
#
#msc20160012_141
consumer_key.append("zf1f2P4AllifZhtIwVoPeXjHC")
consumer_secret.append("Y29dMvDHaxOwKYzWMDoItdswI5ksCNmS2gckwel9pCzLGkfIM2")
access_token.append("819410554259439616-1F87qpjOMkvQSYb6srkxDb9GxhfCPSo")
access_token_secret.append("HtNBwTixhcB6LcBX1V8vqvBiLvjkzMecv3eW6xSdUXcPB")
#
#
#msc20160012_142
consumer_key.append("ZW9TU6BPwDJVmBWInka3qczhS")
consumer_secret.append("TeY8jP5Hj673nLKCuU1OzitDKX8pPs5anClEc91J3o1g00Cecb")
access_token.append("819410554259439616-nUtZ4wzBMD5jWxCDqpYpMBIwirC5kPa")
access_token_secret.append("wSVmqBgMIDORNsgGZLyMwk8oJQyE6c0GLS7Hiync99vL4")
#
#
#msc20160012_143
consumer_key.append("LlVwi6l6TfeA9TftkjV4mfRUT")
consumer_secret.append("EGtccwCgYZxhm4mtc9GOQ7p1O0gUG1kkaI6xrqsVcPw9sEcGBD")
access_token.append("819410554259439616-klTdm3hstpChKH3rmlIot5JbRui93MP")
access_token_secret.append("LOTxMFxS9JTA2vrS5gXttre5yXd7GUkCzIRkJctFrDaTE")
#
#
#msc20160012_144
consumer_key.append("q31nzWNGagFI5Z0nKZu6PMQy5")
consumer_secret.append("cYjTrMzVOaIHUnydStb7iMsMS9yCgZY2Y58HHpVQ9E8AOP1JqF")
access_token.append("819410554259439616-gwHoVkN3nDuK0FCNPx8SNTmgWFejA2N")
access_token_secret.append("xuhAx9CkgqFOUYrLo8OJ7rTHZfJ9Gb1kiswMw9ukduD2K")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app15 - user: msc2016002_15 - e-mail: twitter15msc20160012@yahoo.com - senha: padrão
#
#msc20160012_151
consumer_key.append("5PDmwijPhMM05F2IbXSmaO7Wu")
consumer_secret.append("xZXYgKhNE2yTBp1Fdu0AD6eL6vAla9PJWbHWYOPamLo1rKYBzH")
access_token.append("819411941374431232-lgKyr48Ctu2smXLhpZR4ngO69U6wa4K")
access_token_secret.append("beF0ifThX0wnrzwSGIFMPES7Ip9BznNs5DEMMEddjBo3R")
#
#
#msc20160012_152
consumer_key.append("X3ZYnx7Pydz0rI1xkhV73TP8J")
consumer_secret.append("DjWmkUgF2IDWb5vfoXpy7BkdJDk5qJ0oMT8BkTCbYszx5FXhNt")
access_token.append("819411941374431232-co95YUhS2WEgGVVjN3u8wXdZPpmeVI3")
access_token_secret.append("lMFJnQlH7cZxdabAlwgXt1g70KRXDWptErBn6BGUO9Zm0")
#
#
#msc20160012_153
consumer_key.append("CfVBY5o6bau5ZG5ffJ1HnPUQc")
consumer_secret.append("eHLtKBMwJbFCCHiuc9dlrRFXrvyPvHtb9QHTo1K2ampAEvq3Fm")
access_token.append("819411941374431232-laCiAKmq7M85oruoNoSyTBvbWQM9N7A")
access_token_secret.append("xKmuG7iJaMvAkZNHIGMoBfw0pNzE6Cf0Oiz47YSBFFNAd")
#
#
#msc20160012_154
consumer_key.append("WmuzkHYqYGfvWPqlEgbxk2MU5")
consumer_secret.append("g8HI2vvHPUsBWJQbrtRSf4Q77l9cH03iVwPdgVvkGA7jXTbijA")
access_token.append("819411941374431232-QlWJFI6398qgorIdWip5XgbZ9AtGpbT")
access_token_secret.append("XG0D6J5LKQTUuYz8YpzqFiVIG2daHHCHByt3n3Oq1QXnL")
#
#
###############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app16 - user: msc2016002_16 - e-mail: twitter16msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("6Q9zSQDuB2niWPP1tSqRmNHUq")
consumer_secret.append("ZcueGOjB3JX1OcHyfpH2l5md4MAjjZFuPp2yfG15HYCzooAfBq")
access_token.append("821791002180616193-CcNmQuwjKj804wq2ikTQbAMoNlrfz0o")
access_token_secret.append("D5DQK1XZ5qBKq8EKmeev87NhVb1yrcNcQuuqHyN1fOKiY")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app17 - user: @Msc20160012A - e-mail: twitter18msc20160012@twitter.com - senha: padrão
#
consumer_key.append("3gVxtQ0C2XDANOL4U0iTBgSIm")
consumer_secret.append("NkBSL1WTP9Xg3NlySKwf7An2NNdyjqPt31yBwEBqw1QsrgiKCE")
access_token.append("821796304296800256-p5eJvMW6abui1eYiuVFYlYWgJTJeyzS")
access_token_secret.append("nr17M8tDwK52FtBXV7SnzzoX4KIkd4ue72SBpMfrpP7WA")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc20160012_app18 - user: msc20160012app1 - e-mail: twitter18msc20160012@twitter.com - senha: padrão
#
consumer_key.append("deNrgSwdbzjPXk32dR5m69P2n")
consumer_secret.append("KRHdAHct41S8O2KT9CmXuaLvSQemlZnWpnwGoa2IRVggkek26o")
access_token.append("821797690401062913-yxZzVEqT2c2M5x2JyZIY2Clvs1lY9W5")
access_token_secret.append("6hssvAyXzO8r8zVdqG7qaYj9iHH9ptXkBEUQ6ZOj3fMkl")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001219 - user: msc2016001219 - e-mail: twitter19msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("EEkdXTiOIkKnQZcImRz0pQB3A")
consumer_secret.append("SHNlarOmFV2MOx9RhHC6NW1KVZcKp1QUhRbAqzB4tsNq1xz7lc")
access_token.append("822124565660893185-iQ0vqhYsHwQwWKA5Lj4tjILCQouA7GZ")
access_token_secret.append("czGKEmZB4U06d9NazwzBrOOXOfF3wsPyUjEzvoOn0kEpU")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001220 - user: msc2016001220 - e-mail: twitter20msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("EGVwGkgohKsP4hsl1ytM0BnCM")
consumer_secret.append("rVdWiMV3ZoUMZaIcrXBfCNPEWQxTI8llN9RiNpqArotxshRZv5")
access_token.append("822131424312643584-B5aRpo3hCkbvdTmmaPlvPkWyi0bEg8C")
access_token_secret.append("93sN2MhETrmymnG8gVVvz8p3KM6lhaHvASOmYESGVgRQq")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001221 - user: msc2016001221 - e-mail: twitter21msc20160012@gmail.com - senha: padrão
#
consumer_key.append("U2jr4RpNkCCcDmWMGMoz0CI1D")
consumer_secret.append("CArDCfDLPGeQZgTyyXXosyoUDEM4DbMUGA9dS7fffLYaSn2BQM")
access_token.append("822144740242100225-NnRDm6TH5f3vaBmdJQA0jhvmKHnqUyg")
access_token_secret.append("k0Ywd87LuyH5tLXTXzaQDVYTeIX1s57bF5gnp6pF7WZOV")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001222 - user: msc2016001222 - e-mail: twitter22msc20160012@gmail.com - senha: padrão
#
consumer_key.append("sYfeUClrSiuDMmOwzBQciW7cm")
consumer_secret.append("RrHamKKBvqMOLOlIKvEQFdT40qdLu89uKGu2myOs5kcdy3xLHK")
access_token.append("822153467997327360-2ESioDKQQRsoKnFRddkhXeen2PEoP0r")
access_token_secret.append("R4fQEtYsPbU9ytW6epd2Wc4f9htVTIi3JlVaq29NqDGoK")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001223 - user: msc2016001223 - e-mail: twitter23msc20160012@gmail.com - senha: padrão
#
consumer_key.append("F6NbD75tmqDCc5QoqhF6qwXNg")
consumer_secret.append("Ul0EctBf0pPybE9jlBxn78Tm13jNsTDBxC5yc4r885IXpw2ggT")
access_token.append("822158610381803520-eYnMQP9arTNsVNnPGVIWY6nVftDhAb0")
access_token_secret.append("iyUFyjRL4QOiIfvcob0ZWzfZqcynHTrEntjjZLxu24sNO")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001224 - user: msc2016001224 - e-mail: twitter24msc20160012@gmail.com - senha: padrão
#
consumer_key.append("dd6araE2xDVtVMGr3HPQ6JtnW")
consumer_secret.append("s95cHsSu2a7zbtTPyHJP7tBATMbalhOtLmqcY5fw0RA10LSbOu")
access_token.append("822169622141091841-UNkWXuDIIXOPa3Z8ZXTINCA7WTY8l67")
access_token_secret.append("k5gNflnUoFuWqPx5h8tPUJN1uER4tjdhrxJSGdQnq7iFN")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001225 - user: msc2016001225 - e-mail: twitter25msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("kpodmnsKnox8nc1LhLTkB7dFY")
consumer_secret.append("CpIRPQPGmmRWnZ4hmjY8cKQgvz8VcRtgXY9hLno4VSgPbfufBP")
access_token.append("822171677576536064-Z4JnhNl4NYrdzGQC4LOBR4StiWV2DCK")
access_token_secret.append("xYv37LdszQo0ez3tvSjwxlPtbmLK4TYZ7DdVHY2Nm1J6n")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001226 - user: msc2016001226 - e-mail: twitter26msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("5wb4ynE4wY3sySGwXZVlv526b")
consumer_secret.append("wfGRqCXNTuHd7SJJaBMvaUdAXXIoO0D0WyGOUOyYLRZrf8WSPC")
access_token.append("822173167502446592-DX4mcoFkbaFOWqG8vqc1RMJioUxfI0B")
access_token_secret.append("LcAn5J1LRoF94sTiIS2ObjTqmGDRgHUcVIkQ7JAcU1fPn")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("tY71hkUKRrr9Bf94Bo1El5ozW")
consumer_secret.append("Xm3ZSg2zmCNSMJtx3sBeODkZkQqiLAFmkOi7KoTrcak00rLyHK")
access_token.append("822174289742925824-FzJqDAWIgRkJ8xR15BLQR9E8oJ7L3a3")
access_token_secret.append("bwD0p1lREYF9kSSiYp1vWXdKBM4jzAjW8ONJgCDXuT66n")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001228 - user: msc2016001228 - e-mail: twitter28msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("1tvls7W6QObrPrSjGsqehSMgd")
consumer_secret.append("YILtV6oYSayKZtsdJhDIr7QKvtPSQdLxRlOn1vGyL2nudIBece")
access_token.append("822215581831151616-k9pPtsIYTvmqU9F3vyIzVn2qm2vgH6v")
access_token_secret.append("h0ATS5hOrXrIGwdML8jZkBGuh2hOYMBYmknMAFlAq9tpC")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001229 - user: msc2016001229 - e-mail: twitter29msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("a9QadNejWTtmI1FQeMGads8bW")
consumer_secret.append("1tfJGTXeXnaMdJaQtjwvRxtGe1WLGCV8BbrvIs6V3hqUukEUeb")
access_token.append("822217293006508033-Jj6Guy7R3v7TeghxadPWmEouRAn8YiW")
access_token_secret.append("jRhxUlWs57V1HF3Wdwp4cgGHg13nUGilsK3TxGbbpD3ee")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001230 - user: msc2016001230 - e-mail: twitter30msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("78FsYx3VnphiSmMeGYNbuk3CW")
consumer_secret.append("m0no952gbsWt5ZwoNjAHGZ5uF30pyIdbQuYK978IYZ2eC9esME")
access_token.append("822219154245779456-K9hBIl3xDDzclfiYKiop6dcKhrbOopF")
access_token_secret.append("eXoCbIOsKylGjoIq95G6HYfE6AndfbxWLS9mB7jNppsRJ")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001231 - user: msc2016001231 - e-mail: twitter31msc20160012@yahoo.com - senha: padrão
#
consumer_key.append("xqRDNkgLW9akJTbjB1F01yOaK")
consumer_secret.append("v44MFstC4IpjtSo3xPRw7zk5Vo4Kvj07fhgQOjIMRbTA2pLls3")
access_token.append("831843480565645314-tNEdOhZlV4ODJ468ENAHJeccupfofbW")
access_token_secret.append("RjCllDWZOHstKLgiCLMrXxXSfo1jRgl0XJiWPcNgwUFL1")
#
#
##############################################################################################################
##############################################################################################################
#		Conta: msc2016001232 - user: msc2016001232 - e-mail: twitter32msc20160012@yahoo.com - senha: padrão
#
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
consumer_key.append("3gdXCHZ8T43pOmZcBVt86ttBf")
consumer_secret.append("vnoo0P17s7iJ0Qh4jh08FRUzP3FF3cEr1fgcSQNndsFdYpxTTs")
access_token.append("831849920944553984-els3pI9zCLz1c8D3FIrfpHqo6i58b44")
access_token_secret.append("sRs5nE5F07k7Pw4LlWycPcIiNRgMYE94ti3zbVoNUerlW")
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
