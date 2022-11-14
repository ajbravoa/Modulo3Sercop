#-----------------SEPARACION DE FUNCIONES EN CLASES CORRESPONDIENTES------------------------------

#from re import S
#from django.shortcuts import render, redirect
#from .models import Curso, Persona, Pregunta
#from django.contrib.auth import login, logout, authenticate

#from django.contrib import messages
#----INCLUIR MAS LIBRERIAS ------

#from django.contrib.auth.models import UserManager, User
#from django.core.paginator import Paginator
#from django.http import Http404

#---INCORPORO LA LIBRERIA PASSLIB (ENCRIPTACION) ------
#from passlib.hash import pbkdf2_sha256


#------PANTALL DE INICIO DE SESION-----
#def IniciarSesion(request):
#   return render(request,"autenticacion/index.html")

#----LOGUEAR-------
#def Login(request):
#   if request.method=="POST":
#       usuario=request.POST["txtUsuario"]
#       contrasena=request.POST["txtContrasena"]

#       user=authenticate(username=usuario, password=contrasena)

#        if(user is not None):
#            login(request,user)
#            fname=user.first_name
#            lname=user.last_name
#            login1=user.username

            #----CREACION DE VARIABLES DE SESION----
#            request.session["FullName"]=fname+" "+lname
#            request.session["usuario"]=login1
            #contexto={"login1":login1}
            #return render(request, "gestionCursos.html",contexto)
#            return redirect("GestionCursos")

#        else:
#            messages.error(request, "! CREDENCIALES INCORRECTAS")

#    return render(request,"autenticacion/index.html")


#def CerrarSesion(request):
     #---DESTRUYO LAS VARIABLES DE SESION
#    del request.session["FullName"]
#    del request.session["usuario"]

    #----HACIENDO LE LOGOUT SE DESTRUYE TAMBIEN LAS VARIABLES DE SESION------
#    logout(request)
#    messages.success(request, "! Has Cerrado la Sesion")

    #----REDIRECCION AL INICIO DE SESION-----
#    return redirect("IniciarSesion")


#----METODO SOLO PARA PRESENTAR EL REGISTRAR USUARIO-----
#def PresentarRegistrarUsuario(request):

    #----ESTO REEMPLAZAR POR LA INVOCACION DE UN SP O VISTA-------
#    preguntas=Pregunta.objects.all()
#    contexto={"preguntas":preguntas}
#    return render(request,"autenticacion/Registrar.html", contexto)


#def RegistroUsuario(request):
#    if request.method=="POST":

#        username=request.POST["txtUsuario"]
#        fname=request.POST["txtNombre"]
#        lname=request.POST["txtApellido"]
#        email=request.POST["txtEmail"]
#        pass1=request.POST["txtPassword"]
#        pass2=request.POST["txtPasswordConfirm"]

        #-----CAMPOS COMPLEMENTARIOS PARA LA AUDITORIA (PERSONA)------
#        nombreCompleto=fname+" "+lname
#        pregunta_secreta=request.POST["ddlPregunta"]
#        respuesta=request.POST["txtRespuesta"]

        #-----AQUI VA LA RUTINA DE ENCRIPTACION------
#        encriptado=pbkdf2_sha256.encrypt(respuesta,rounds=15000, salt_size=32)

        #----SE VALIDA SI EL USUARIO EXISTE-----
#        if User.objects.filter(username=username):
#             messages.error(request, "! USUARIO YA EXISTENTE !")
#             return redirect("IniciarSesion")

        #-----VALIDACIONES PARA REGISTRAR EL USUARIO-----
#        if len(username)<5:
#            messages.error(request, "! USUARIO DEBE SER MAYOR A 5 CARACTERES !")

            #-----PANTALLA QUE MUESTRE EL MENSAJE DE ERROR (PENDIENTE CAMBIAR)----
#            return redirect('/')
        
#        if pass1!=pass2:
#            messages.error(request, "! CONTRASEÑAS NO SON IGUALES !")
#            return redirect('/')

#        if not username.isalnum():
#            messages.error(request, "! USUARIO DEBE CONTENER LETRAS Y NUMEROS !")
#            return redirect('/')


#        if User.objects.filter(email=email):
#            messages.error(request, "! USUARIO DEBE CONTENER LETRAS Y NUMEROS !")
#            return redirect('/')
        
        #-----CREAMOS EL USUARIO MAS AUDITORIA  (PERFIL DEL USUARIO)-----
#        miUsuario=User.objects.create_user(username, email, pass1)
#        miUsuario.first_name=fname
#        miUsuario.last_name=lname
#        miUsuario.is_active=False
#        miUsuario.is_staff=True 
#        miUsuario.save()

#        persona=Persona.objects.create(
#            usuarios=username,
#            nombre=fname,
#           apellido=lname,
#            nombreCompleto= (fname + lname),
#            Contrasena=pass1,
#            PreguntaSecreta=pregunta_secreta,
#            Respuesta=encriptado
#        )
        #---AQUI REGISTRAMOS LA AUDITORIA-----
#        messages.success(request, "! USUARIO CREADO CORRECTAMENTE !")
#        return redirect("IniciarSesion")

#    return render(request, "autenticacion/Registrar.html")


        




#-----PANTALLA DE BIENVENIDA AL ACADEMICO-----
#def Inicio(request):
    #-----OBTENEMOS TODA LA CONSULTA DE CURSOS-----
#    cursosListados=Curso.objects.all()

    #----OBTENEMOS EL NUMERO DE PAGINA (PAGINACION)------
#    page=request.GET.get('page',1)

#    try:
#        paginator=Paginator(cursosListados,3)
#        cursosListados=paginator.page(page)

#    except:
#        raise Http404




#    messages.success(request, '==CURSOS LISTADOS==')
#    contexto={
#        'entity':cursosListados,
#        'paginator':paginator
#    }
#    return render(request,"gestionCursos.html",contexto)


#----REGISTRO DEL CURSO------
#def registrarCurso(request):
    #---OBTENEMOS LOS DATOS DEL POST----
#    codigo=request.POST["txtCodigo"]
#    nombre=request.POST["txtNombre"]
#    creditos=request.POST["txtNumCreditos"] 

    #print("Codigo: "+codigo)
    #print("Nombre: "+nombre)
    #print("Creditos: "+creditos)

     #----CREAR EL OBJETO MAS REGISTRO-----
#    curso=Curso.objects.create(
#        codigo=codigo,
#        nombre=nombre,
#        creditos=creditos
#    )
#    messages.success(request, "! CURSO REGISTRADO CORRECTAMENTE !")
#    return redirect("GestionCursos")


#------CONSULTA DE CURSOS----------
#-----ESTA CONSULTA LA REALIZAMOS DIRECTAMENTE EN EL FRONT END (GESTIONCURSOS)----
   
#----EDICION DE CURSO (BUSQUEDA)-------
#def edicionCurso(request,codigo):
#    try:
#        curso=Curso.objects.get(codigo=codigo)
#        context={"curso":curso}

#    except Exception:
#        curso="No Existente"
#        context={"curso":curso}
    
#    return render(request, "edicionCurso.html", context)


#---EDICION DE CURSO (CUANDO SE REALIZA EL POST)------
#def editarCurso(request):
#    codigo=request.POST["txtCodigo"]
#    nombre=request.POST["txtNombre"]
#    creditos=request.POST["txtNumCreditos"] 

#    curso=Curso.objects.get(codigo=codigo)
#    curso.nombre=nombre
#    curso.creditos=creditos
    #----actualizo----
#    curso.save()

#    messages.success(request, '! CURSO ACTUALIZADO !')
#    return redirect("GestionCursos")


#-----ELIMINACION DE CURSO-----
#def eliminarCurso(request, codigo):
#    curso=Curso.objects.get(codigo=codigo)
#    curso.delete()
#    messages.success(request, '! CURSO ELIMINADO OK !')
#    return redirect("GestionCursos")
    











    
