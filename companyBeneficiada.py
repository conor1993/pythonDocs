import requests ,json

cabeceras = {
        "Host":"www.sistemaemprendedor.gob.mx",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"es-MX,es-ES;q=0.9,es;q=0.7,es-AR;q=0.6,es-CL;q=0.4,en-US;q=0.3,en;q=0.1",
        "Accept-Encoding":"gzip, deflate, br",
        "Refere":"https://www.sistemaemprendedor.gob.mx/emprende/",
        "X-XSRF-TOKEN":"WWZ1OKUq+QlorGSpo1n0zg==",
        "X-Requested-With":"XMLHttpRequest",
        "Content-Type":"application/json;charset=utf-8",
        "Content-Length":"26",
        "Cookie":"JSESSIONID=4c00ab02-c692-4108-b81b-596b6b299384; rememberMe=KVutHJc8R6rrW7hIoj21u9W0RvSk38yHgtM/o7f5IKYC8L67pW7FNMpk8B/OmZDLRF21AZxyzqCQLZJr3gvE0TuJOtaY7+F5wOyKpuR/c+5ajGb4egXgDobgHedQyyVqVzwM2eWnO/MMhwCikmylQhNPqlSR4F2gZQ20gtPqpKdyF6q3DnLBmekD3Xy8cMylP0qVau/xUxgId2kO4XROeKp+LwqqqBEFZUZAn/lRdUgIf8R1JFJb8eoutaWfwXxVII75J9URrPanK5edGLsqHno9hvMcLA0Z8POVsFyHK9kpxkDRIkFih8XIHQrLpSEzxL6szugzfxGAfdvJejFMCqa7amFyuSHPN7Xk+tTJ5VYtTMSe0xHdmzJMs4XtLMKa48n9vIqrE99Ps5io8GfHxcX49nIEiQzj1ZOV9Sq4p1jZZRVM8KY32AT1x9zgjfX5KF12wwLZdP3XsE9JKhlrMQN5Djqfq+ThMKMyatKABA7zQZTMK2ODh23FINMtKNSm; __utmt=1; XSRF-TOKEN=WWZ1OKUq%2BQlorGSpo1n0zg%3D%3D; __utma=192720424.1395271006.1477070525.1477325894.1477329608.11; __utmb=192720424.3.10.1477329608; __utmc=192720424; __utmz=192720424.1477070525.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
        "Connection":"keep-alive"
    }

cookies = {
       "JSESSIONID":"4c00ab02-c692-4108-b81b-596b6b299384",
       "XSRF-TOKEN":"WWZ1OKUq%2BQlorGSpo1n0zg%3D%3D",
       "__utma":"192720424.1395271006.1477070525.1477325894.1477329608.11",
       "__utmb":"192720424.3.10.1477329608",
       "__utmc":"192720424",
       "__utmt":"1",
       "__utmz":"192720424.1477070525.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
       }


url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/tracking/getCompaniesBenefited"
r = requests.post(url, headers=cabeceras, cookies=cookies,timeout=900000000)




