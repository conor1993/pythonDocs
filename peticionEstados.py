import requests ,json 



payload = {"stateId":25}

cabeceras = {
"Host": "www.sistemaemprendedor.gob.mx",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
"Accept": "application/json, text/plain, */*",
"Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"X-XSRF-TOKEN": "m5yiKe5zRx+x22wWNm8YjA==",
"X-Requested-With": "XMLHttpRequest",
"Content-Type": "application/json;charset=utf-8",
"Referer": "https://www.sistemaemprendedor.gob.mx/emprende/",
"Content-Length": "14",
"Cookie": "JSESSIONID=7e2dbb77-5ff3-4296-a5f4-20f42e9297d2; rememberMe=qlSUKHkV7JHp59eJVgLZauZCRATlhG6ADcwurBHRJWXVtUkRtMk6T28r/K2qhhZ9uLuEfZTdc5KrAmA5+nkIow22BgHccceyNbo5XKLJZZZhvrMM6HSeReZxQCqViQOMQDPLFCW8ZXYlIGlUozQ07vHWE0Y+XkD1/bpCJS/OMn13wsLZKEjY3Z29z5N7LFHtLIGIIu5Iawbrw6JvBdw2K3VLWHgg2YYrMYWnzyezSuFcDqfwYKZm/UG3IUZQ8Rqf52yoZALZNQl6sgg1tDlrvEMlhY7JNgesgT7w5z5vPM/6Jnrh+p/Vo0KFX0febd3+ylVBuu0QFPy2d5rrbQC/XB8gaA7noAILK2w5F+3izttbVgKkXgRwOHLpVOx79i5SMd9q+oumF0oU0I5FjbPxo5fag41n7yey7RJOADSNH+KbBeBqpNCAHhKQoBnRQFjJxhivvzm5+MOhh8p8gY7UKZz6eyG4yiTROb54jCKmyapOIizcPP23MrA3h6MwGMiv; __utma=192720424.2011008773.1476478648.1476478648.1476482849.2; __utmc=192720424; __utmz=192720424.1476478648.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); XSRF-TOKEN=hsgM%2BtkRZ%2BuyU4pjXz0uJw%3D%3D",
"Connection": "keep-alive"
}

cookies = {
   "JSESSIONID": "c2300d3d-d665-4a53-8a5d-f90664d6ed27",
   "XSRF-TOKEN":"hsgM+tkRZ+uyU4pjXz0uJw==",
   "__utma":"192720424.1089191711.1476731220.1476731220.1476731220.1",
   "__utmb":"192720424.4.10.1476731220",
   "__utmc":"192720424",
   "__utmz":"192720424.1476731220.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
   "__utmt":"1",
   "rememberMe":"jNsZ0GCmBDSckCDF+0rMSlHdjp3m5lsBARHjkFi1PdM2pQF7sRycUwQoKLzr7rFQB0MTWrtXHoohrAXP1oqGkuX+gHHFhIlvbtW2tzfZ9mbdz1gY5IEPgcLhrTDkqHAKKKVXCn9kDoswWotlnSTiUmZdqWf6T97qcpLmyKEi4tCOuD5TQVNh6zXF+PojSxesVOAyqplUth/BwX20rYMSIUTVADug7dLnPgGcpWe5tzilqKRyMa/xicWTDFjC9GGMBVf1G1AWj7O/5H7ArFYgyhi5fp1dnMYZyjDDCgVIELM7klndOQwkxCZkWLZNwXBfinkSfsmh3xE76GoUUHO4PphgAB1Vzl3OAGSm+gHWvoO6CKxX63YJMeVZk8bt31IdgvH9TigE4msJ2x1fDlULmWHvJVIZsc6x50iv5wSgN/jU+5eZq6xApxO1gqKaOScx4coDRGQt/81PuaIfDFKFbHonemDBDE9iQ2e/Vkmbkrr0f5KiSnFrFRtWcncX/E9w"
}
 

 
url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/catalog/listStates"
r = requests.post(url,data=json.dumps(payload), headers=cabeceras, cookies=cookies) 

print(r.json())
