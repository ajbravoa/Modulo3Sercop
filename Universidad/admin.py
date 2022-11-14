from django.contrib import admin
from .models import Curso, Persona, Pregunta, Post, Comentario

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filed=("Titulo","Slug", "Contenido")

    #------PALABRA RESERVADA PARA EL SLUG------
    prepopulated_fields={'Slug': ('Titulo',)}




admin.site.register(Curso)
admin.site.register(Persona)
admin.site.register(Pregunta)
admin.site.register(Post,PostAdmin)
admin.site.register(Comentario)




