from django.urls import path
#from .import views
from Universidad.Funciones import clsPlanificacion, clsUsuarios, clsAcademico, clsBlog

urlpatterns = [
    #path('GestionCursos',views.Inicio, name="GestionCursos"),
    path('GestionCursos',clsAcademico.clsAcademico.Inicio, name="GestionCursos"),

    #path('registrarCurso', views.registrarCurso, name="registrarCurso"),
    path('registrarCurso', clsAcademico.clsAcademico.registrarCurso, name="registrarCurso"),


    #path('edicionCurso/<codigo>', views.edicionCurso, name="edicionCurso"),
    path('edicionCurso/<codigo>', clsAcademico.clsAcademico.edicionCurso, name="edicionCurso"),


    #path('editarCurso', views.editarCurso, name="editarCurso"),
    path('editarCurso', clsAcademico.clsAcademico.editarCurso, name="editarCurso"),


    #path('eliminarCurso/<codigo>', views.eliminarCurso, name="eliminarCurso"),
    path('eliminarCurso/<codigo>', clsAcademico.clsAcademico.eliminarCurso, name="eliminarCurso"),

    #----PANTALLA DE INICIAR SESION-----
    #path('', views.IniciarSesion, name="IniciarSesion"),
    path('', clsUsuarios.clsUsuarios.IniciarSesion, name="IniciarSesion"),
    
    #---LOGIN DE AUTENTTICACION
    #path('Login', views.Login, name="Login"),
    path('Login', clsUsuarios.clsUsuarios.Login, name="Login"),

    #----CERRAR SESION----
    #path('CerrarSesion', views.CerrarSesion, name="CerrarSesion"),
    path('CerrarSesion', clsUsuarios.clsUsuarios.CerrarSesion, name="CerrarSesion"),

    #------PRESENTAR PANTALLA REGISTRAR USUARIO------
    #path('PresentarRegistrarUsuario', views.PresentarRegistrarUsuario, name="PresentarRegistrarUsuario"),
    path('PresentarRegistrarUsuario', clsUsuarios.clsUsuarios.PresentarRegistrarUsuario, name="PresentarRegistrarUsuario"),
    
    
    #path('RegistroUsuario', views.RegistroUsuario, name="RegistroUsuario"),
    path('RegistroUsuario', clsUsuarios.clsUsuarios.RegistroUsuario, name="RegistroUsuario"),


    path('BlogAcademico', clsBlog.clsBlog.PresentarBlog, name="BlogAcademico"),

    #-----PARA VER EL DETALLE DEL POST------
    path('post_detalle/<int:post_id>', clsBlog.clsBlog.post_detail, name="post_detalle"),

    #----GRABAR COMENTARIO----
     path('grabar_comentario', clsBlog.clsBlog.grabarComentarios, name="grabar_comentario"),


     #-----STORE PROCEDURES
    path('ConsultaLogin', clsUsuarios.clsUsuarios.ConsultaLogin, name="ConsultaLogin"),

    path('GrabarPlanificacion', clsPlanificacion.clsPlanificacion.GrabarPlanificacion, name="GrabarPlanificacion"),

    #--- FUNCION QUE INVOCA A API ----------
    path('ConsultarPlanificacion', clsPlanificacion.clsPlanificacion.ConsultarPlanificacion, name="ConsultarPlanificacion"),


]