from django.db import models

# Create your models here.

class Planificacion(models.Model):
    Id=models.IntegerField()
    nombre=models.CharField(max_length=200)
    usuario=models.CharField(max_length=30)
    anio=models.IntegerField()
    fecharegistro=models.DateField(auto_now_add=True)
   
