from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid

#---INSTANCIO EL SERVICIO-----
app=FastAPI()

#----SQL LITE------
#----ARREGLO QUE CONTENDRA LOS REGISTROS----
lista=[]

#---ENTIDAD---
class Post(BaseModel):
    id:Optional[str]
    titulo:str
    autor:str
    contenido:str
    fecha_creacion: datetime=datetime.now()
    publicado_por: Optional[datetime]
    estaPublicado:bool=False


#---PANTALLA INICIO----
@app.get('/')
def Inicio():
    return {"Bienvenido a FastApi"}


@app.get('/posts')
def ConsultaGeneral():
    return lista


#----PARA GRABAR REGISTROS------
@app.post('/posts')
def save_post(post:Post):
    #print(post.dict())
    #----VAMOS TRABAJAR CON LOS UUID MAS NO IDENTITY----
    #---SETEO EL ID---
    post.id=str(uuid())

    #---AGREGAR LA CLASE ENTIDAD POST A LA LISTA---    
    lista.append(post.dict())
    #print(lista)
    return lista[-1]
    #return "Guardado correctamente"


#---API DE CONSULTA ESPECIFICA-----
@app.get('/posts/{post_id}')
def ConsultaEspecifica(post_id:str):
    #---ASUMIENDO QUE RECUPERAMOS LOS REGISTROS DE UN SP----
    for item in lista:
        if item["id"]==post_id:
            return item

    #---codigo 200 (peticion ok)
    #---codigo 400 (bad request)
    #--- codigo 500 (errores de servidor o infraestructura)
    return HTTPException(status_code=400, detail="Registro no encontrado")


#-----API DE ELIMINACION------
@app.delete("/posts/{post_id}")
def eliminar_post(post_id:str):
    for indice, contenido in enumerate(lista):
        if contenido["id"]==post_id:
            lista.pop(indice)
            return {"message":"Post Eliminado Corretamente"}

    return HTTPException(status_code=400, detail="Registro No existente")

#----API DE ACTUALIZACION------
@app.put('/actualizarPost/{post_id}')
def actualizar_post(post_id:str, actualizarPost: Post):
    for indice, contenido in enumerate(lista):
        if contenido["id"]==post_id:
            print(actualizarPost.titulo)
            lista[indice]["titulo"]=actualizarPost.titulo
            lista[indice]["autor"]=actualizarPost.autor
            lista[indice]["contenido"]=actualizarPost.contenido

            return {"message":"Post Actualizado Correctamente"}

    return HTTPException(status_code=404, detail="Registro No existente")
    
           

