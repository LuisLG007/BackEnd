import mysql.connector

conexion1=mysql.connector.connect(host="5.196.110.172", user="root", passwd="ssa99&Dev#;", database="coronavirus")
cursor1=conexion1.cursor()
cursor1.execute("SELECT * FROM view_casos_municipios")
filas = cursor1.fetchall()
for fila in filas:
   print(fila)

conexion1.close()    