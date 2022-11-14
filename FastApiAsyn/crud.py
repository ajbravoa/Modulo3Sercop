from sqlalchemy.orm import Session
from models import Articule
from schemas import ArticuleSchema

#-----METOD DE CONSULTA GENERAL-------
def consulta_general_articulo(db:Session,skip: int=0, limit: int =100):
    return db.query(Articule).offset(skip).limit(limit).all()


#---METODO DE CONSULTA ESPECIFICA-----
def consulta_especifica_articulo_id(db:Session,articulo_id:int):
    return db.query(Articule).filter(Articule.id==articulo_id).first()


#----INSERCION O CREACION-------
def crear_articulo(db:Session, art:ArticuleSchema):
    _articulo=Articule(
        id=art.id,
        titulo=art.titulo,
        descripcion=art.descripcion
    )
    db.add(_articulo)
    db.commit()
    db.refresh(_articulo)
    return _articulo
    
#----ACTUALIZAR ARTICULO-----
def actualizar_articulo(db:Session, id_articulo: int, titulo_articulo: str, descripcion_articulo:str):
    #----REALIZAR LA BUSQUEDA------
    _articulo=consulta_especifica_articulo_id(db=db, articulo_id=id_articulo )

    _articulo.title=titulo_articulo
    _articulo.descripcion=descripcion_articulo

    db.commit()
    db.refresh(_articulo)
    return _articulo


#----ELIMINAR ARTICULO------
def eliminar_articulo(db:Session, articulo_id: int):
    _articulo=consulta_especifica_articulo_id(db=db, articulo_id=articulo_id)
    db.delete(_articulo)
    db.commit()