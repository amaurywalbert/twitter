# -*- coding: latin1 -*-
################################################################################################
#	
#
import sys, math
from math import*
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script auxiliar para calculos matemáticos
## 
######################################################################################################################################################################


######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calcular(valores=None):
	calculos = {}
	if valores:
		if valores.__class__.__name__ == 'list' and calculos.__class__.__name__ == 'dict':
			def somar(valores):
				soma = 0
				for v in valores:
					soma += v
				return soma
 
			def media(valores):
				soma = somar(valores)
				qtd_elementos = len(valores)
				media = soma / float(qtd_elementos)
				return media

			calculos['soma'] = somar(valores)
			calculos['media'] = media(valores)
			return calculos
			
def calcular_full(valores=None):
	calculos = {}
	if valores:
		if valores.__class__.__name__ == 'list' and calculos.__class__.__name__ == 'dict':
			def somar(valores):
				soma = 0
				for v in valores:
					soma += v
				return soma
 
			def media(valores):
				soma = somar(valores)
				qtd_elementos = len(valores)
				media = soma / float(qtd_elementos)
				return media
 
 			def variancia(valores):
 				_media = media(valores)
 				soma = 0
 				_variancia = 0
 
 				for valor in valores:
 					soma += math.pow( (valor - _media), 2)
 					_variancia = soma / float( len(valores) )
 					return _variancia
 
 			def desvio_padrao(valores):
 				return math.sqrt( variancia(valores) )

			calculos['soma'] = somar(valores)
			calculos['media'] = media(valores)
			calculos['variancia'] = variancia(valores)
			calculos['desvio_padrao'] = desvio_padrao(valores)
			return calculos