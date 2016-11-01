def escritura():
    salida = open("texto.txt","w")
    for i in range(1,100):
         salida.write("%d "%(i))
    salida.close()     

escritura()

def leer():
    doc = open("texto.txt","r+")
    doc.read()
    pos = doc.tell()

    
    doc.seek(pos)
    for i in range(99,200):
         doc.write("%d "%(i))
    doc.close()     

leer()    


