from fastapi import FastAPI
import models
from routes import router
from config import engine


#----ESTABLEZCO LA CONEXION-----
models.Base.metadata.create_all(bind=engine)

#---INSTANCIO AL FAST API
app=FastAPI()

#---EMULO EL PATH DE URL DE DJANGO..
app.include_router(router, prefix="/articulo", tags=["articulo"])


