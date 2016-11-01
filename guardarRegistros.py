import requests ,json


def GuardarRegistro(cabeceras,cookies,payload):
    url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/tracking/saveBenefitedCompany"
    r = requests.post(url, data=json.dumps(payload), headers=cabeceras, cookies=cookies) 
    return r.json()
