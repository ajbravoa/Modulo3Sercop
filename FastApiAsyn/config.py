from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#---DEFINO LA CADENA DE CONEXION---
DATABASE_URL='postgresql://postgres:password@localhost:5432/academico'

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()