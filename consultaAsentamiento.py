import requests ,json, pypyodbc

conx = pypyodbc.connect('Driver={SQL Server};''Server=integrasrv3;''Database=emprendedores;''uid=sa;pwd=int3gr@')





cabeceras = {
"Host":"www.sistemaemprendedor.gob.mx",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
"Accept":"application/json, text/plain, */*",
"Accept-Language":"es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"X-XSRF-TOKEN": "EFsJ+WIT9v8xk3cegJdsOg==",
"X-Requested-With":"XMLHttpRequest",
"Content-Type":"application/json;charset=utf-8",
"Referer":"https://www.sistemaemprendedor.gob.mx/emprende/",
"Content-Length":"22",
"Cookie":"JSESSIONID=29fc677e-d4e8-4de5-a7f1-3dfd1f85ceb0; rememberMe=pzRXcrzijw+f6ItNiOiAq2YK59KG8zsEysalUfHD7D15MTY44Xj8URgAJzj4DtA3nkm36HjPA+fQuHKrkGP51v1owVKVkbU5oTYgiZ3e8238djauwLv3QIqMmA39YDOj3WDV7Y/gTpkqpYUb0Ac9zsLrG5cwuMS0P5l/MPPpfLY32lEVnZ4wTuuyNht4oNuuBvphBTm5yFqZgawuZnSeL0JvWnySs4k1LtmnifmlgwD6u/9sfqduarTRZVOVTqWIuijjgrI6myA0p0ATzWp2tIQg/2e+U0KYLKtpju0afzIdjw4Q6J3IQ8pWB8Nnyl6MFFJ3RYHAwW5Kyf1H+Sa7Xh7kjBNh9xmF2L/Bwp647lmg0ZtfnccUG2FIaB9pdJ0a8W8OjHcW7ny4FCFxkV217LIeuLmP522QFtHxtnbu283lxzfTSiy4VI0uFaHj3yUd+KV+faXBsbwEGwneMDNtPei9FDp/v8NW5oLdUvByqEQ/QMBqKCWmt7FOrg/hSU7J; __utma=192720424.1136187985.1476742764.1476742764.1476742764.1; __utmc=192720424; __utmz=192720424.1476742764.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); XSRF-TOKEN=EFsJ%2BWIT9v8xk3cegJdsOg%3D%3D",
"Connection": "keep-alive"
}

cookies = {
 
    "SESSIONID":"9fc677e-d4e8-4de5-a7f1-3dfd1f85ceb0", 
    "rememberMe":"pzRXcrzijw+f6ItNiOiAq2YK59KG8zsEysalUfHD7D15MTY44Xj8URgAJzj4DtA3nkm36HjPA+fQuHKrkGP51v1owVKVkbU5oTYgiZ3e8238djauwLv3QIqMmA39YDOj3WDV7Y/gTpkqpYUb0Ac9zsLrG5cwuMS0P5l/MPPpfLY32lEVnZ4wTuuyNht4oNuuBvphBTm5yFqZgawuZnSeL0JvWnySs4k1LtmnifmlgwD6u/9sfqduarTRZVOVTqWIuijjgrI6myA0p0ATzWp2tIQg/2e+U0KYLKtpju0afzIdjw4Q6J3IQ8pWB8Nnyl6MFFJ3RYHAwW5Kyf1H+Sa7Xh7kjBNh9xmF2L/Bwp647lmg0ZtfnccUG2FIaB9pdJ0a8W8OjHcW7ny4FCFxkV217LIeuLmP522QFtHxtnbu283lxzfTSiy4VI0uFaHj3yUd+KV+faXBsbwEGwneMDNtPei9FDp/v8NW5oLdUvByqEQ/QMBqKCWmt7FOrg/hSU7J",
    "__utma":"192720424.1136187985.1476742764.1476742764.1476742764.1",
    "__utmc":"192720424",
    "__utmz":"192720424.1476742764.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "XSRF-TOKEN":"EFsJ%2BWIT9v8xk3cegJdsOg%3D%3D"

   }
 
cursor = conx.cursor()

sql=""

 
url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/catalog/listPostalSettlements"

for i in range(80180,82991):
    payload={"postalCode":i}
    r = requests.post(url,data=json.dumps(payload), headers=cabeceras, cookies=cookies)
    if(r.json() != []):
         data = r.json()
         for item in data:
             cp=i
             id_asent= item["id"]
             nombre = item["name"]
             sql="INSERT INTO [dbo].[catAsent]([cp]  ,[id_asent] ,[nom_asent]) VALUES(%s,%s,'%s')"%(cp,id_asent,nombre)
             cursor.execute(sql)
             cursor.commit()
             print(id_asent)

print("el finn")             
   
cursor.close()    
conx.close()



    

