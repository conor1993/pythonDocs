import requests ,json


def GuardarRegistro(cabeceras,cookies,payload):
	try:
		pass
		url = "https://www.sistemaemprendedor.gob.mx/emprende/api/v1/tracking/saveBenefitedCompany"
		r = requests.post(url, data=json.dumps(payload), headers=cabeceras, cookies=cookies,timeout=90)
	except Exception, e:
		print(r.json())
	print(r.json())
