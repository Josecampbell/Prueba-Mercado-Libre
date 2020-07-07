"""
creado el 04/07/2020
@uthor:José G Hernandez C

"""
#############################################################################################################
#------------------------ Librerias requeridas--------------------------------------------------------######
#############################################################################################################

import pandas as pd # la utilizo para crear una tabla de datos con con los requerimientos ( id,title, ategory_id,name)

import requests # Libreria requerida para hacer consultas a la api

import logging  #libreria requerida para crear el archivo  log

#############################################################################################################
#------------------------ Cuerpo principal -----------------------------------------------------------######
#############################################################################################################

seller_id=input('Ingrese el seller_id:') # esta linea le pide al usuario que introduzca el cualquier seller_id
#############################################################################################################
url_consulta_api1='https://api.mercadolibre.com/sites/MLA/search?seller_id='+str(seller_id)
#Esta linea de código  construyo el url
#############################################################################################################
consulta1 = requests.get(url_consulta_api1)
# Esta linea de código hago la consulta a la API
#############################################################################################################
jsom_consulta1=consulta1.json()
# Esta linea de código hago extraigo el archivo json
#############################################################################################################
list_id=[]
list_title=[]
list_category_id=[]
list_name=[]
# Estas lineas de código inicializo las listas con los requerimientos solicitados
#############################################################################################################
for i in range(0,len(jsom_consulta1["results"])):
            list_id=list_id+[jsom_consulta1["results"][i]['id']]
            list_title=list_title+[jsom_consulta1["results"][i]['title']]
            list_category_id=list_category_id+[jsom_consulta1["results"][i]['category_id']]
            params = jsom_consulta1["results"][i]['category_id']
            url_consulta_api2='https://api.mercadolibre.com/categories/'+params
            consulta2 = requests.get(url_consulta_api2, params=params)
            jsom_consulta2=consulta2.json()
            list_name=list_name+[jsom_consulta2["name"]]

# Estas lineas de código leo el archivo json, extrayendo ( id,title, category_id, name)
# Para conseguir "name" se hace otra consulta a la api y extraigo el archivo para conseguir los "names" de los
# "category_id"
#############################################################################################################
dictionary = {'id': list_id,
                'name':list_name,
                'category_id': list_category_id,
                'title': list_title}
# construyo un diccionario con los requerimientos solicitados
#############################################################################################################
df = pd.DataFrame(dictionary)
# construyo una tabla de tados con los requerimientos solicitados
#############################################################################################################
logger = logging.getLogger('ejemplo_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('Consulta_Mercado_Libre.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.info(df.to_string())
# construir el un archivo log
# el archivo se llama Consulta_Mercado_Libre
#############################################################################################################