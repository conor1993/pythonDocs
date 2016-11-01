#ejemplo con constructor por default
class pruebaConstructor:
    def __init__(self,nombre):
        self.nombre = nombre

    def imprimeNombre(self):
        print (self.nombre)
 
#ejemplo con erencia
class operacion:
    def cargar_var1(self,var_1):
        self.var1 = var_1
    def cargar_var2(self,var_2):
        self.var2 = var_2
    def imprimir(self):
        print (self.resultado)

class suma(operacion):
    def operar(self):
        self.resultado = self.var1 + self.var2

        
#sumas = suma()
#sumas.cargar_var1(2)
#sumas.cargar_var2(5)
#sumas.operar()
#sumas.imprimir()

class Persona:
    def __init__(self,nombre,apellido):
        self.nom = nombre
        self.ap  = apellido
    def __str__(self):
        cadena = self.nom+' '+self.ap
        return cadena

per1 = Persona("juan","lugo")
print(per1)



















        
    
