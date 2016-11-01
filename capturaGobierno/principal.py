import guardarRegistro, parametros,obtenerDatosCp,json,pypyodbc, time


def obtenerLocalidad(municipality):
	try:
		conx = pypyodbc.connect('Driver={SQL Server};''Server=integrasrv3;''Database=emprendedores;''uid=sa;pwd=int3gr@')
		cursor = conx.cursor()
		sql="select id_localidad from municipios where idm = %s"%(municipality["id"])
		cursor.execute(sql)
		rows = cursor.fetchall()
		cursor.commit()
		cursor.close()    
		conx.close()
		for i in rows:
			id_as = i["id_localidad"]
			
        

	except Exception, e:
		raise e
	return id_as	


#crear la dana a guardar
def crearCdena(item,dress,settlementType,state,municipality,city,localities,m,v):
	localidad = obtenerLocalidad(municipality)
	empresaBeneficiada = {"benefitedCompany":{"companyLinkedNetwork":v,"companyDirectedWoman":m,"address":{"postalCode":int(item["codigopostal"]),"settlementType":settlementType["id"],"state":state["id"],"municipality":municipality["id"],"settlement":item["id_asent"],"mailingSettlement":105400,"locality":localidad,"streetRoadsType":42,"street":item["vialidad"],"externalNumber1":item[22],"externalNumber2":"","roadsType1":42,"roadsName1":item["nombre vialidad"],"roadsType2":42,"roadsName2":item["nombre vialidad2"],"backRoadsType":42,"backRoadsName":item["nombre vialidad posterior"]},"companyType":"INDIVIDUAL","stratification":"2","sector":"2","rfc":item["emprfc"].upper(),"name":item["nombre"]+" "+item["paterno"]+" "+item["materno"],"phone":item["telefono"],"individualName":item["nombre"],"individualLastName":item["paterno"],"individualSecondLastName":item["materno"]},"appId":235354}
	ejecutarPrincipal(empresaBeneficiada,item)
	



def ejecutarPrincipal(payload,item):
	cookies   = parametros.cookies()
	cabeceras = parametros.cabecera()
	respuesta = guardarRegistro.GuardarRegistro(cabeceras,cookies,payload)

	if respuesta["result"]==True:
		conx = pypyodbc.connect('Driver={SQL Server};''Server=integrasrv3;''Database=emprendedores;''uid=sa;pwd=int3gr@')
		cursor = conx.cursor()
		sql = "update [dbo].[captura2016] SET [Capturado] = 1 WHERE idreg = %s"%(item["idreg"])
		cursor.execute(sql)
		cursor.commit()
		cursor.close()
		conx.close()  
		print(respuesta)





try:
	conx = pypyodbc.connect('Driver={SQL Server};''Server=integrasrv3;''Database=emprendedores;''uid=sa;pwd=int3gr@')
except Exception, e:
	print(e)


try:
	cursor = conx.cursor()
	sql = "select  a.*,case when B.id_asent is null then '80000' else A.cp end as CodigoPostal, case when B.id_asent is null then (select top 1 x.id_asent from catAsent x where x.cp='80000' order by 1 desc) else B.id_asent end as id_asent from Captura2016 A  left join catAsent B on Convert(int,A.cp)=Convert(int,B.cp) and (substring(A.COLONIA,1,10) like '%'+ cast(B.nom_asent as nvarchar(500)) +'%'  or substring(A.COLONIA,4,10) like '%'+ cast(B.nom_asent as nvarchar(500)) +'%')  where tipo like '%fis%' and TAMANO like '%micro%' and (sector like '%comer%') and capturado = 0 and  estado = 'sinaloa' order by 1"
	cursor.execute(sql)
	rows = cursor.fetchall()
	cursor.commit()
	cursor.close()    
	conx.close()


#obtener  los datos de la consulta 
	for item in rows:
		try:

			id_asentamineto = item["id_asent"]
			idasentamineto = {"settlementId":id_asentamineto}
			datos_asentamiento = obtenerDatosCp.obtenerDatosCp(idasentamineto)
			dress = datos_asentamiento.json()
			settlementType  = dress["settlementType"]
			state = dress["state"]
			municipality = dress["municipality"]
			city = dress["city"]
			localities = dress["localities"]
			
			viculada=item["emp viculada"]
			mujer = item["empresa mujer"]
			viculada=item["emp viculada"]
			mujer = item["empresa mujer"]
			if mujer == "S":
				m=True
			else:
				m=False

			if viculada == "S":
				v = True
			else:
				v=False		

			crearCdena(item,dress,settlementType,state,municipality,city,localities,m,v)
			#print (item[22])
			print(item["idreg"])
			time.sleep(5)
		except Exception, e:
			print(e)		

except Exception, e:
	print(e)





    
#payload = {"benefitedCompany":{"address":{"postalCode":"80000","settlementType":1,"state":25,"municipality":1872,"settlement":105400,"mailingSettlement":105400,"locality":211519,"streetRoadsType":42,"street":"Sauces 904","externalNumber1":"708","externalNumber2":"","roadsType1":42,"roadsName1":"Sauces 904","roadsType2":42,"roadsName2":"Sauces 904","backRoadsType":42,"backRoadsName":"Sauces 904"},"companyType":"INDIVIDUAL","stratification":"1","sector":"2","rfc":"DUCA940909MSL","name":"Andrea GuadalupeDuarteCardenas","phone":"6672453523","individualName":"Andrea Guadalupe","individualLastName":"Duarte","individualSecondLastName":"Cardenas"},"appId":144950}
#ejecutarPrincipal(payload)
    




