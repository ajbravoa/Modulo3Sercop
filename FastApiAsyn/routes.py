from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
#----IMPORTO LA CADENA DE CONEXION --
from config import SessionLocal
from sqlalchemy.orm import Session

#----IMPORTO LOS SCHEMAS------
from schemas import ArticuleSchema, Request, Response, RequestArticule

#----IMPORTO LA LOGICA DEL NEGOCIO -----
import crud

#----instancio las rutas----
router=APIRouter()

#---CONTROLAMOS LA CONEXION------
def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()


#--------DEFINIR LAS APIS (ASINCRONAS)---------
#------CREATE-----------
@router.post("/crear")
async def crear_articulo_servicio(request:RequestArticule, db:Session=Depends(get_db)):
    crud.crear_articulo(db, art=request.parameter)
    return Response(status="OK", code="200", message="Creado exitosamente").dict(exclude_none=True)

#-----CONSULTA GENERAL---------
@router.get("/")
async def consulta_articulos(skip:int=0, limit: int=100, db:Session=Depends(get_db)):
    _articulo=crud.consulta_general_articulo(db,skip,limit)
    return Response(status="OK", code="200", message="Consulta General Exitosa",result=_articulo)


 #-----CONSULTA ESPECIFICA---------
@router.get("/{id}")
async def consulta_especifica_articulos_id(id: int, db:Session=Depends(get_db)):
    _articulo=crud.consulta_especifica_articulo_id(db,id)
    return Response(code="200", status="OK", message="Consulta Especifica Exitosa",result=_articulo).dict(exclude_none=True)
   
#------ACTUALIZAR-------
#---patch: es la definicion de update, un update lo puedes hacer por patch, put, post
#---patch: es actualizacion directa
#---put: primero elimino y luego inserto
#---post: mediante una condicion yo elijo si es insert o es update
@router.patch("/actualizar")
async def actualizar_articulo(request: RequestArticule, db:Session=Depends(get_db)):
    articulo=crud.actualizar_articulo(db,id_articulo=request.parameter.id, 
    titulo_articulo=request.parameter.titulo, descripcion_articulo=request.parameter.descripcion)

    return Response(status="OK", code="200", message="Actualizado exitosamente")


#-----ELIMINAR-------
@router.delete("/eliminar")
async def consulta_especifica_articulos_id(request: RequestArticule, db:Session=Depends(get_db)):
    crud.eliminar_articulo(db,articulo_id=request.parameter.id)
    return Response(code="200", status="OK", message="Eliminacion Exitosa").dict(exclude_none=True)




