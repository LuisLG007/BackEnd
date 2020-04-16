from flask import Flask

import os
import urllib.request
from bs4 import BeautifulSoup
import pprint
import crud


app = Flask(__name__)

@app.route('/update')
def update():        
    CChis = []
    res = []
    details = []
    Municipio = ""
    Casos = ""
    Tasa = ""
    datos = urllib.request.urlopen('http://coronavirus.saludchiapas.gob.mx/casos-por-municipio').read().decode()

    soup = BeautifulSoup(datos)
    os.system("cls")
    ################################################## Detalles de Chiapas
    tags = soup.find_all('h5', class_='card-title')
    for itemC in tags:
        num = itemC.get_text()
        CChis.append({'num': num})  
    ################################################## Historial
    table = soup.find('table', class_='table')

    for fila in table.find_all("tr"):
        #if nroFila==2:
            nroCelda=0
            for celda in fila.find_all('td'):
                if nroCelda==0:
                    Municipio=celda.text                   
                    #print("Municipios:", Municipio)
                    
                if nroCelda==1:
                    Casos=celda.text               
                    #print("Casos:", Casos)
                    
                if nroCelda == 2: 
                    Tasa = celda.text                
                    res.append({
                    'Municipio': Municipio,
                    'Casos': Casos,
                    'Tasa': Tasa                
                    })                         
                    #print("Tasa", Tasa)
                                
                nroCelda=nroCelda+1
        #nroFila=nroFila+1


    if len(crud.read('History')) == len(res):
        print("No hay cambios")
    else:
        
        for itemD in crud.read('ActualChis'):
            crud.delete('ActualChis', itemD)
        for item in CChis:
            crud.create('ActualChis', item)    
    
        for itemD in crud.read('History'):
            crud.delete('History', itemD)
        for itemN in res:
            crud.create('History', itemN)
        print('Datos actualizados con exito')
        
    return 'Datos Actualizados'


if __name__ == '__main__':
    app.run(debug=True, port=4000)
#JSON Print Format       
#pprint.pprint(res, indent=2)  


#https://firebase.google.com/docs/firestore/quickstart
#https://firebase.google.com/docs/firestore/manage-data/delete-data
#https://firebase.google.com/docs/firestore/manage-data/add-data