import pypyodbc, time

try:
	conx = pypyodbc.connect('Driver={SQL Server};''Server=integrasrv3;''Database=emprendedores;''uid=sa;pwd=int3gr@')
except Exception, e:
	print(e)


try:
	cursor = conx.cursor()
	sql="select a.*,case when B.id_asent is null then '80000' else A.cp end as CodigoPostal, case when B.id_asent is null then (select top 1 x.id_asent from catAsent x where x.cp='80000' order by 1 desc) else B.id_asent end as id_asent from Datos1Copia A  left join catAsent B on Convert(int,A.cp)=Convert(int,B.cp) and (substring(A.COLONIA,1,10) like '%'+ cast(B.nom_asent as nvarchar(500)) +'%'  or substring(A.COLONIA,4,10) like '%'+ cast(B.nom_asent as nvarchar(500)) +'%') where tipo like '%fis%' and TAMANO like '%mic%'"
	cursor.execute(sql)
	rows = cursor.fetchall()
	cursor.commit()
	cursor.close()    
	conx.close()


#obtener  los datos de la consulta 
	for item in rows:
		print(item["id_asent"])
		print("\n")
		

except Exception, e:
	raise 
