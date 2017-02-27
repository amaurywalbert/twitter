# *-* coding:utf-8 *-*
import struct, sys, time
from collections import namedtuple

#Inteiro para o código ('i') e depois o array de chars de 100 posições ('100s')
formato = 'l150s'
user = struct.Struct(formato)

#Gravando os dados
def grava():
	for i in range(0,2):
		with open("dados_class.dat", "a+b") as f:
			uid = long(raw_input("Digite o codigo:"))
			nome = raw_input("Digite o nome:")
			f.write( user.pack(uid,nome)  )


def imprime():
	with open("dados_class.dat", "rb") as f:
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		while f.tell() < tamanho:
			buffer = f.read(user.size)
			codigo, nome = user.unpack(buffer)
			print codigo, nome

grava()
imprime()