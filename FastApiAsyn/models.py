from sqlalchemy import Column,Integer, Float, Boolean, String, DateTime, Date
from config import Base

#---ESTABLECIKIENTO LA ENTIDAD
class Articule(Base):
    __tablename__='Articulo'

    id=Column(Integer, primary_key=True, index=True)
    titulo=Column(String)
    descripcion=Column(String)
    