from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

#---DEFINO EL T (METODO GENERICO)---
T=TypeVar('T')

#---DEFINO LA CLASE LA CUAL RECIBIRA LOS PARAMETROS DE ENTRADA----
class ArticuleSchema(BaseModel):
    id: Optional[int] =None
    titulo: Optional[str] =None
    descripcion: Optional[str]=None
    
    class Config:
        orm_mode=True  #---CONFIGURO LA CONEXION---


#-----ESTABLEZCO EL REQUEST GENERICO (PARA ENVIO DE PARAMETROS)--------
class Request(GenericModel, Generic[T]):
    parameter: Optional[T] =Field(...)

#----DEFINO EL PETICION (REQUEST NORMAL)
class RequestArticule(BaseModel):
    parameter: ArticuleSchema = Field (...)

#----DEFINIRIAN EL RESTO DE CLASES
#......
#......

#----DEFINO LA CLASE QUE ME ENVIARA LA RESPUESTA (COD, STATUS, MESSAG, RESULT)
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


