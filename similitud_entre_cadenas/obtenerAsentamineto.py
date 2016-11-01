#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata, requests ,json,pypyodbc, cadenasiguales



###   obtener datos de gobbienrno

payload = {"postalCode":"80000"}

def obtenerAsentamineto(payload):
    cabeceras = {
        "Host":"www.sistemaemprendedor.gob.mx",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"es-MX,es-ES;q=0.9,es;q=0.7,es-AR;q=0.6,es-CL;q=0.4,en-US;q=0.3,en;q=0.1",
        "Accept-Encoding":"gzip, deflate, br",
        "Referer":"https://www.sistemaemprendedor.gob.mx/emprende/",
        "X-XSRF-TOKEN":"/pSwWv6SNuMCmODNKcUBwA==",
        "X-Requested-With":"XMLHttpRequest",
        "Content-Type":"application/json;charset=utf-8",
        "Content-Length":"22",
        "Cookie":"rememberMe=7tCjJaQ7KGjSZENK3bSOZi6/ZxVyswV4AUZIy9TEVQ/i8cZYibCWs2K8EL7ZX1FLS/jhXYJ7zILUCDnke9kyklUn1Hw7s+Jsq5YRAfkGLrcyj8Ia0aHB2+1P1skLo5qczvTX4NI1N407pFZXdXKhiKxLq71SuvzX6s8dJMQQcvAEgnEYrj/j2vSNeBZq+FqsKGWGN3PTr4GzPP5ZTUqSrN4elm98MCe7CVJLsrO3pCvEDhQPfbyBZnfG3yVTV12ESrHMk/fzPVXgeoECnl7YUlUvIMUCGCSHEyc4kGWfK0WZssUybIKU5wht4nn+5K52GdzrDt0gWAamcoJjSUBpWMWVx0PLdIZwlU9hePPhV0WilGL7mAOQJyn2V00vziR1CDkhUxRFz3LONCHovVebEtidbxsYpyRkcTZspyrwJwyKX2elEre0uF5Dxwh7cZqTYxcXQ0QfiJIV41zlaR3+r26VCu2VoqOn/ZYK6UxOWCTqwGp6+iZOuOhU9hT4jpxk; JSESSIONID=c40a5f12-e7c0-4568-8e6f-22a8a274f7a8; __utma=192720424.444222433.1476813396.1477950801.1477953737.25; __utmz=192720424.1476813396.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=192720424; XSRF-TOKEN=%2FpSwWv6SNuMCmODNKcUBwA%3D%3D",
        "Connection":"keep-alive"
    }


    cookies = {
       "JSESSIONID":"c40a5f12-e7c0-4568-8e6f-22a8a274f7a8",
       "XSRF-TOKEN":"/pSwWv6SNuMCmODNKcUBwA==",
       "__utma":"192720424.444222433.1476813396.1477950801.1477953737.25",
       "__utmc":"192720424",
       "__utmz":"192720424.1476813396.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
       "rememberMe":"7tCjJaQ7KGjSZENK3bSOZi6/ZxVyswV4AUZIy9TEVQ/i8cZYibCWs2K8EL7ZX1FLS/jhXYJ7zILUCDnke9kyklUn1Hw7s+Jsq5YRAfkGLrcyj8Ia0aHB2+1P1skLo5qczvTX4NI1N407pFZXdXKhiKxLq71SuvzX6s8dJMQQcvAEgnEYrj/j2vSNeBZq+FqsKGWGN3PTr4GzPP5ZTUqSrN4elm98MCe7CVJLsrO3pCvEDhQPfbyBZnfG3yVTV12ESrHMk/fzPVXgeoECnl7YUlUvIMUCGCSHEyc4kGWfK0WZssUybIKU5wht4nn+5K52GdzrDt0gWAamcoJjSUBpWMWVx0PLdIZwlU9hePPhV0WilGL7mAOQJyn2V00vziR1CDkhUxRFz3LONCHovVebEtidbxsYpyRkcTZspyrwJwyKX2elEre0uF5Dxwh7cZqTYxcXQ0QfiJIV41zlaR3+r26VCu2VoqOn/ZYK6UxOWCTqwGp6+iZOuOhU9hT4jpxk"
       }
    try:
      url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/catalog/listPostalSettlements"
      r = requests.post(url,data=json.dumps(payload), headers=cabeceras, cookies=cookies,timeout=90)
    except Exception, e:
      print(e)
    datos = r.json()
    localidades = datos
    return localidades

 


#traer datos de la base de datos emprendedoressss --------------------------------------------------------------------------------------

try:
  conx = pypyodbc.connect('Driver={SQL Server};''Server=integrasrv3;''Database=emprendedores;''uid=sa;pwd=int3gr@')
except Exception, e:
  print(e)


try:
  cursor = conx.cursor()
  sql="select * from Captura2016 where cp = 80000"
  
  cursor.execute(sql)
  rows = cursor.fetchall()
  cursor.commit()
  cursor.close()    
  conx.close()
except Exception, e:
  print(e)


for row in rows:
  print(row["colonia"])



#------------------------------------------------------------------------------------------------------------------------------------------------
loc = obtenerAsentamineto(payload)
d = loc[1]
print(d["name"]) 