from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=100)
    creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        texto="{0}({1})"
        return texto.format(self.nombre,self.creditos)
    

class Persona(models.Model):
    usuarios=models.CharField(max_length=20)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    nombreCompleto=models.CharField(max_length=200)
    Contrasena=models.CharField(max_length=200)
    PreguntaSecreta=models.IntegerField()
    Respuesta=models.TextField()
    FechaRegistro=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombreCompleto
    

class Pregunta(models.Model):
    Pregunta=models.CharField(max_length=150)
    FechaRegistro=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Pregunta


#----ENTIDADES PARA EL POST ACADEMICO-----
class Post(models.Model):
    Id=models.AutoField(primary_key=True)   
    Titulo=models.TextField(max_length=100)
    Slug=models.SlugField()
    FechaCreacion=models.DateTimeField(auto_now_add=True)
    UsuarioCreacion=models.TextField()  #--- se lo recupera de la variable de sesion
    Contenido=models.TextField()

    def __str__(self):
        return self.Titulo

class Comentario(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comentarios")
    Nombre=models.CharField(max_length=100)
    Email=models.EmailField()
    FechaCreacion=models.DateTimeField(auto_now_add=True)
    UsuarioCreacion=models.CharField(max_length=30)  #--- se lo recupera de la variable de sesion
    Contenido=models.TextField()
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return  f"Comentario de {self.Nombre} {self.Contenido}"

#---------STORE PROCEDURES (QUE NO RETORNAN VALORES)----------
class pa_ingreso_planificacion(models.Model):
    Nombre=models.CharField(max_length=100)
    Usuario=models.CharField(max_length=20)
    Anio=models.IntegerField()







