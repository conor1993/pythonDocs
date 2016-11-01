
class malware():
    def __init__(self,nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre

    def infectar():
        print ("infectado")

class gusano(malware):
    def propagarse(self):
        print ("infectado usb")

class troyano(malware):
    def propagarse(self):
        print("enviando email")
    
