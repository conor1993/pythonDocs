#devuelbe una lista con todas las llaves del diccionario
def llaves():
    dic = {'1':'ola','2':'io'}
    yaves = dic.keys()
    print(yaves)
#retorna una lista cobn todos los valores
def valores():
    dic = {'1':'ola','2':'io'}
    valoress = dic.values()
    print(valoress)

#devuelbe una lista de tuplas
def tuplas():
    dic = {'1':'ola','2':'io'}
    tu = dic.items()
    print(tu)

#saca un valor de el diccionario y lo almacena en una variable depues elimina ese elemnto del diccionario
def sacar():    
    dic = {'1':'ola','2':'io'}
    valor = dic.pop('1')
    print(dic)
    print(valor)
    
#retorna true si la llave se encuntra en el diccionario
def buscar():
    dic = {'1':'ola','2':'io'}
    if(dic.has_key('1')):
        print("si se encuantra")
    else:
        print("no se encuntra")

#elimina todos los elemntos de la lista
def elimina():
    dic={1:'menos'}
    dic.clear()
    print(dic)

#copia una lista
def copia():
    dic={1:'menos'}
    dic2  = dic.copy()
    print(dic2)

def actualiza():
    dic={1:'ola'}
    dic2={1:'olis',2:'olas'}
    dic.update(dic2)
    print(dic)

#erroes captura de esepciones
def erroresKey():
    dic={1:'juan',2:'lugo'}
    try:
        print(dic[5])
    except KeyError:
        print('error no existe')






    









        

