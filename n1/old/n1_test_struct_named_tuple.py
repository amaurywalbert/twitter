# *-* coding:utf-8 *-*
import struct, sys, time
from collections import namedtuple

# como temos um inteiro para o código ('i') e depois o array de chars de 100 posições ('100s')
formato = 'i100s'

#definindo a estrutura com namedtuple
Pessoa = namedtuple("Pessoa", "codigo nome")

estrutura = struct.calcsize(formato) # Retorna o tamanho de um elemento no formato passado


#Gravando os dados
for i in range(0,2):
	with open("dados_named_tuple.dat", "a+b") as f:
		codigo = int(raw_input("Digite o codigo:"))
		nome = raw_input("Digite o nome:")
		pessoa = Pessoa(codigo=codigo, nome=str.encode(nome))
		f.write( struct.pack( formato, *pessoa )  )
		print(pessoa)


with open("dados_named_tuple.dat", "rb") as f:
	f.seek(0,2)
	tamanho = f.tell()
	f.seek(0) 
	while f.tell() < tamanho:
		print f.tell()
		buffer = f.read(estrutura)
		codigo, nome = struct.unpack( formato, buffer )
		nome = nome.split("\0")[0] # Como o C utiliza o \0 para terminar uma string no python precisamos tratar isso
		pessoa = Pessoa(codigo=codigo, nome=nome)
		print(pessoa)
	sys.exit(0)