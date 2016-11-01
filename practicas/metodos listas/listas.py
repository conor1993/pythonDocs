import random

#agrega un elemneto al final de la lista
def agrear_elemnto():
    arreglo = ["d","b","a","c"]
    arreglo.append("p")
    print (arreglo)

#agrega un elemnto en la lista en la posicion en la k le iniquemos
def agregar_pos():
    arreglo = [0,2,1]
    arreglo.insert(0,5)
    print(arreglo)


#agrega los elemntos de iuna lista en otro
def agregarLista():
    lista1 = [1,2,3]
    lista2 = [3,4,5]

    lista1.extend(lista2)
    print(lista1)


# remueve un valor y lo mete en una variable
def extraer():
    lista1 = [1,2,3]
    el = lista1.pop(2)
    print(el)
    print(lista1)


# remuebe el valor
def remober():
    lista1 = [1,2,3]
    lista1.remove(2)
    print(lista1)

#cuenta los elemntos k se repiten en un arreglo
def contar():
    lista=[1,2,3]
    num = lista.count(2)
    print (num)



#retorna la pos del elemnto a buscar
def buscarel():
    lista = [2,45,1]
    pos = lista.index(1)
    print(pos) 

#ordena los elentos de menor a mayor
def ordena():
    li = [3,2,1]
    li.sort()
    print(li)


def ejercicio():
    arreglo=[]

    for i in (range(0,300)):
        arreglo.append(i)
    arreglo.remove(0)
    print(arreglo)    
    ult = len(arreglo)
    arreglo.remove(ult)
    print(arreglo)
    final=0
    for con in arreglo:
        final = final + con
    arreglo.insert(1,final)
    print(arreglo)








