class menu:
    n  = []
    e  = []

    def cargar(self,nom,et):
        self.e.append(et)
        self.n.append(nom)

    def mostrar(self):
        for i in range(0,len(self.n)):
            print ('%s  %s'%(self.n[i],self.e[i]))
            

menu1 = menu()

menu1.cargar('juan','www.mevalekeki.com')
menu1.cargar('lugo','no me valenada.com')
menu1.mostrar()
