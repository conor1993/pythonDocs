#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata

def covertirMinusculas(cadena1):
	cad1 = cadena1.lower()
	return cad1


def eliminarespacios(cadena):
	#nueva cadena sin espacios
	nuevaCadena=""
	for i  in range(0, len(cadena)):
		if cadena[i] != " ":
			nuevaCadena = nuevaCadena+cadena[i]
	return nuevaCadena		
			


#eliminar acentos
def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()

def normalizarCadena(cad):
	c = elimina_tildes(cad)
	c = eliminarespacios(c)
	c = covertirMinusculas(c)
	return c


def similitudCdenas(xx,yy):
	tam1 = len(xx)
	tam2 = len(yy)

	if tam1 > tam2:
		elmayor = tam1


ccadena ="CULIACAN Ú"
ccadena2 = "cÚLIACAN"
y = ccadena.decode('utf-8')
x = ccadena2.decode('utf-8')
xx = normalizarCadena(x)
yy = normalizarCadena(y)

similitudCdenas(xx,yy)




