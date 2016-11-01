import os

def ejemplosMetodosSistema():
    path = os.getcwd()
    print (path)
    #listar el contenido de la direccion
    lista = os.listdir(path)
    print (lista)
    
def File_o_archivo():
    direccion = os.getcwd()
    lista = os.listdir(direccion)
    
    for doc in lista:
       flag = os.path.isdir(doc)
       flag2 = os.path.isfile(doc)
       
       if (flag == True):
           print("es un directorio %s"%(doc))
       elif (flag2 == True):
           print ("es un archivo %s"%(doc))


                   


