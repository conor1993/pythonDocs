import mysql.connector

bd = mysql.connector.connect(user='root', password ='', host='localhost',database='clientes')

cur = bd.cursor()

cur.execute("select * from tblcliente")

for dato in cur.fetchall():
    print dato

bd.close()    
                    
