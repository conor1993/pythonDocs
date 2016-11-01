#retorna  el string con la primera letra en mayuscula
def primerLetraM():
    cadenaO = "cadenas"
    cadena2 = cadenaO.capitalize()
    print (cadena2)

# convertir a mayusculas una cadena       
def mayCadena():
    palabra = "elenano"
    palabra2 = palabra.upper()
    print (palabra2)
    
#devuelbe cadena en minisculas
def minus():
    cadena = "HOLA"
    cadena2 = cadena.lower()
    print (cadena2)

#devuelbe truwe si todas las letras son mayusculas
def esMyuscula():
    cadena="OLAo"

    if (cadena.isupper() == True):
        print("todas las letras son mayusculas")
    else:
        print("no todas son  mayusculas")

#debuelbe verdadero so todas las eletras son minusculas
def sonMinusculas():
    cadena="o"
    if (cadena.islower() == True):
        print("todas las letras son minusculas")
    else:
        print("no todas son  minusculas")
        
#debuelve truwe si todos los elemntos de una cadena son mueros
def esDigito():
    cadena="123"

    if(cadena.isdigit() == True):
        print("todos los caracteres son digitos")
    else:
        print("notodos son digitos")

#debuelbe true si  todos son alfabeticos
def esAlfabetico():
    cadena = "letr5as"
    if(cadena.isalpha() == True):
        print(" son alfabeticos")
    else:
        print("no son alfabeticos")


#son espacios debuelbe true si todos son espacios
def sonEspacios():
    cadena = "  s"
    if(cadena.isspace() == True):
        print("son espacios")
    else:
        print("no  tods son espacios")

#debuelbe true si los caracteres son numeros o letras
def sonletrasNumeros():
    cadena="23"
    if(cadena.isalnum() == True):
        print("contiene numeros y letras")
    else:
        print("no los contiene")

#retorna la poscision de el paramentro en la cadena
def posCaracterfinal():
    cadena="innovamparo"
    pos = cadena.rfind('v')
    print (pos)

#retorna la poscision de el paramentro en la cadena
def posCaracterinicio():
    cadena="innovamparo"
    pos = cadena.find('v')
    print (pos)

#cantidad de beses k una cadena se repite en un string
def contador():
    cadena = "ola olasola"
    cant = cadena.count("ola")
    print(cant)


#reemplasa una cane por otra
def rem():
    cadena="ola amigos ola"
    cadenas2 = cadena.replace('ola','menos')
    print(cadenas2)


#retorna una lista con los elemntos de una string separados por un caracte
def retornaLista():
     cadena= ("no/ma/mes")
     lista= cadena.split("/")
     print(lista)

#retorna una cadena cons letras en mayusculas convertidas en minuscula y viseversa

def cadenaViseversa():
    cadena ="aA"
    cadena2 = cadena.swapcase()
    print(cadena2)

# se justifica a la derecha y se agrega un caracter
def cadenaJustificada():
    cadena="1200"
    cade2 = cadena.rjust(5 , '$')
    print(cade2)

# se justifica a la IZQUIERDA y se agrega un caracter
def cadenaJustificadai():
    cadena="1200"
    cade2 = cadena.ljust(5 , '$')
    print(cade2)

# se justifica al centro y se agrega un caracter
def cadenaJustificadac():
    cadena="1200"
    cade2 = cadena.center(5 , '$')
    print(cade2)



#cofencione una funcion k reciva una oracion y reciva la palabar mayor alfabeticamente
def mayor_alfabeticamente(cadena):
    lista = cadena.split(" ")
    mayor = lista[0]
    for i in range(1,len(lista)):
        if(mayor > lista[i]):
            print(lista[i])
            mayor = lista[i]
    print(mayor)    
    

#eliminar acentos
def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()

string_acentos = "juan"

elimina_tildes(string_acentos)





















    
















        


















        




