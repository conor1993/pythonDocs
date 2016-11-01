import clasePrueba
class persona:
    
    perro = clasePrueba.perro()
    
    def inicio(self,nom):
        self.nombre = nom
        
    def imprime(self):
        print (self.nombre)

    def locos(perro):
        perro.inicio('mirandin')
        perro.imprime()
        

persona1 = persona()
persona1.inicio('juan')
persona1.imprime()
persona1.locos()
