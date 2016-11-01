import modulo1

def  imprimeNumeros():
      resultado = modulo1.suma(2,2)
      print (resultado)

#imprimeNumeros()

#ejemplo de range

def funRange():
    for x in range(0,11):
        print (x)
    
#funRange()

#conversion de datos a string

def  conversion():
    x =5
    y=2.2
    z=False

    print(str(x)+str(y)+str(z))

#conversion()

def tabladel5():
    i=0
    z=5
    for num in range(0,50,5):
         print ('5 x %2d = %-2d'%(i,num))
         i = i+1

#tabladel5()         

def ImprimirExadecimal():
    for num in range(1, 100):
        print('numero decimal %d, numnero exadecimal %x'%(num,num))


#ImprimirExadecimal()

def imprimeSueldos():
    sueldos =  [300.55,200.66,500.2]
    emo     =  ['juan','manuel','lugo']

    for i in range(0,len(sueldos)):
        print ('nombre %-20s  sueldo %10.2f'%(emo[i],sueldos[i]))

#imprimeSueldos()

##recorrido de tuplas

def tuplasRecorrer():
    puntos = [(1,2),(3,4),(5,6)]

    for x,y in puntos:
        print('valor de x:%d valor de y:%d'%(x,y))

##tuplasRecorrer()

def mayorEdad():
    persona = [('juan',200),('pedro',50),('miranbdin',66),('elena',10)]
    nombre, mayor = persona[0]

    for nom,edad in persona:
        if (edad > mayor):
            mayor =edad
            nombre = nom
            
    return(nombre, mayor) 


def imprimeNombre():
    nombre, edad = mayorEdad()
    print ('nombre: %10s edad: %2d '%(nombre,edad))


##imprimeNombre()

## parametros por default

def parDefault(dato,x=5,y=5):
    print('%s datouno = %d dato2 = %d'%(dato,x,y))

#parDefault('juan',10,50)    

#multiples parametros

def parametros(x1,x2, *xn):
    x3 = x1 + x2
    for num in xn:
         x3 = x3+num

    print (x3)
    
parametros(4,5,6,5)    








    


            
