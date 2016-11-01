import requests ,json

payload = {"benefitedCompany":{"address":{"postalCode":"80000","settlementType":1,"state":25,"municipality":1872,"settlement":105400,"mailingSettlement":105400,"locality":211519,"streetRoadsType":42,"street":"Sauces 904","externalNumber1":"708","externalNumber2":"","roadsType1":42,"roadsName1":"Sauces 904","roadsType2":42,"roadsName2":"Sauces 904","backRoadsType":42,"backRoadsName":"Sauces 904"},"companyType":"INDIVIDUAL","stratification":"1","sector":"2","rfc":"DUCA940909MSL","name":"Andrea GuadalupeDuarteCardenas","phone":"6672453523","individualName":"Andrea Guadalupe","individualLastName":"Duarte","individualSecondLastName":"Cardenas"},"appId":144950}
 
cabeceras = {
"Host": "www.sistemaemprendedor.gob.mx",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
"Accept": "application/json, text/plain, */*",
"Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"X-XSRF-TOKEN": "hsgM+tkRZ+uyU4pjXz0uJw==",
"X-Requested-With": "XMLHttpRequest",
"Content-Type": "application/json;charset=utf-8",
"Referer": "https://www.sistemaemprendedor.gob.mx/emprende/",
"Content-Length": "653",
"Cookie": "JSESSIONID=7e2dbb77-5ff3-4296-a5f4-20f42e9297d2; rememberMe=qlSUKHkV7JHp59eJVgLZauZCRATlhG6ADcwurBHRJWXVtUkRtMk6T28r/K2qhhZ9uLuEfZTdc5KrAmA5+nkIow22BgHccceyNbo5XKLJZZZhvrMM6HSeReZxQCqViQOMQDPLFCW8ZXYlIGlUozQ07vHWE0Y+XkD1/bpCJS/OMn13wsLZKEjY3Z29z5N7LFHtLIGIIu5Iawbrw6JvBdw2K3VLWHgg2YYrMYWnzyezSuFcDqfwYKZm/UG3IUZQ8Rqf52yoZALZNQl6sgg1tDlrvEMlhY7JNgesgT7w5z5vPM/6Jnrh+p/Vo0KFX0febd3+ylVBuu0QFPy2d5rrbQC/XB8gaA7noAILK2w5F+3izttbVgKkXgRwOHLpVOx79i5SMd9q+oumF0oU0I5FjbPxo5fag41n7yey7RJOADSNH+KbBeBqpNCAHhKQoBnRQFjJxhivvzm5+MOhh8p8gY7UKZz6eyG4yiTROb54jCKmyapOIizcPP23MrA3h6MwGMiv; __utma=192720424.2011008773.1476478648.1476478648.1476482849.2; __utmc=192720424; __utmz=192720424.1476478648.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); XSRF-TOKEN=hsgM%2BtkRZ%2BuyU4pjXz0uJw%3D%3D",
"Connection": "keep-alive"
}

cookies = {
   "JSESSIONID": "7e2dbb77-5ff3-4296-a5f4-20f42e9297d2",
   "XSRF-TOKEN":"hsgM+tkRZ+uyU4pjXz0uJw==",
   "__utma":"192720424.2011008773.1476478648.1476478648.1476482849.2",
   "__utmc":"192720424",
   "__utmz":"192720424.1476478648.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
   "rememberMe":"qlSUKHkV7JHp59eJVgLZauZCRATlhG6ADcwurBHRJWXVtUkRtMk6T28r/K2qhhZ9uLuEfZTdc5KrAmA5+nkIow22BgHccceyNbo5XKLJZZZhvrMM6HSeReZxQCqViQOMQDPLFCW8ZXYlIGlUozQ07vHWE0Y+XkD1/bpCJS/OMn13wsLZKEjY3Z29z5N7LFHtLIGIIu5Iawbrw6JvBdw2K3VLWHgg2YYrMYWnzyezSuFcDqfwYKZm/UG3IUZQ8Rqf52yoZALZNQl6sgg1tDlrvEMlhY7JNgesgT7w5z5vPM/6Jnrh+p/Vo0KFX0febd3+ylVBuu0QFPy2d5rrbQC/XB8gaA7noAILK2w5F+3izttbVgKkXgRwOHLpVOx79i5SMd9q+oumF0oU0I5FjbPxo5fag41n7yey7RJOADSNH+KbBeBqpNCAHhKQoBnRQFjJxhivvzm5+MOhh8p8gY7UKZz6eyG4yiTROb54jCKmyapOIizcPP23MrA3h6MwGMiv"
}
 

 
url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/tracking/saveBenefitedCompany"
r = requests.post(url, data=json.dumps(payload), headers=cabeceras, cookies=cookies) 

print(r.json())
