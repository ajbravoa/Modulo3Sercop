from  Universidad.Funciones import librerias as l

class clsUsuarios:

    #------PANTALL DE INICIO DE SESION-----
    def IniciarSesion(request):
        return l.render(request,"autenticacion/index.html")


    #----LOGUEAR-------
    def Login(request):
        if request.method=="POST":
            usuario=request.POST["txtUsuario"]
            contrasena=request.POST["txtContrasena"]

            user=l.authenticate(username=usuario, password=contrasena)

            if(user is not None):
                l.login(request,user)
                fname=user.first_name
                lname=user.last_name
                login1=user.username
                correo=user.email
            
                nombre_completo=fname+" "+lname

                #----CREACION DE VARIABLES DE SESION----
                if(nombre_completo=="" or nombre_completo==" "):
                     request.session["FullName"]=login1
                else:
                    request.session["FullName"]=fname+" "+lname

                request.session["usuario"]=login1
                request.session["email"]=correo
                #contexto={"login1":login1}
                #return render(request, "gestionCursos.html",contexto)
                return l.redirect("GestionCursos")

            else:
                l.messages.error(request, "! CREDENCIALES INCORRECTAS")

        return l.render(request,"autenticacion/index.html")

    #---METODO PARA CERRAR SESION----
    def CerrarSesion(request):
        #---DESTRUYO LAS VARIABLES DE SESION
        del request.session["FullName"]
        del request.session["usuario"]

        #----HACIENDO LE LOGOUT SE DESTRUYE TAMBIEN LAS VARIABLES DE SESION------
        l.logout(request)
        l.messages.success(request, "! Has Cerrado la Sesion")

        #----REDIRECCION AL INICIO DE SESION-----
        return l.redirect("IniciarSesion")


    #----METODO SOLO PARA PRESENTAR EL REGISTRAR USUARIO-----
    def PresentarRegistrarUsuario(request):
        #----ESTO REEMPLAZAR POR LA INVOCACION DE UN SP O VISTA-------
        preguntas=l.Pregunta.objects.all()
        contexto={"preguntas":preguntas}
        return l.render(request,"autenticacion/Registrar.html", contexto)


    #--- REGISTRO DE USUARIOS-------
    def RegistroUsuario(request):
        if request.method=="POST":

            username=request.POST["txtUsuario"]
            fname=request.POST["txtNombre"]
            lname=request.POST["txtApellido"]
            email=request.POST["txtEmail"]
            pass1=request.POST["txtPassword"]
            pass2=request.POST["txtPasswordConfirm"]

            #-----CAMPOS COMPLEMENTARIOS PARA LA AUDITORIA (PERSONA)------
            nombreCompleto=fname+" "+lname
            pregunta_secreta=request.POST["ddlPregunta"]
            respuesta=request.POST["txtRespuesta"]

            #-----AQUI VA LA RUTINA DE ENCRIPTACION------
            encriptado=l.pbkdf2_sha256.encrypt(respuesta,rounds=15000, salt_size=32)

            #----SE VALIDA SI EL USUARIO EXISTE-----
            if l.User.objects.filter(username=username):
                l.messages.error(request, "! USUARIO YA EXISTENTE !")
                return l.redirect("IniciarSesion")

            #-----VALIDACIONES PARA REGISTRAR EL USUARIO-----
            if len(username)<5:
                l.messages.error(request, "! USUARIO DEBE SER MAYOR A 5 CARACTERES !")

                #-----PANTALLA QUE MUESTRE EL MENSAJE DE ERROR (PENDIENTE CAMBIAR)----
                return l.redirect('/')
            
            if pass1!=pass2:
                l.messages.error(request, "! CONTRASEÑAS NO SON IGUALES !")
                return l.redirect('/')

            if not username.isalnum():
                l.messages.error(request, "! USUARIO DEBE CONTENER LETRAS Y NUMEROS !")
                return l.redirect('/')


            if l.User.objects.filter(email=email):
                l.messages.error(request, "! USUARIO DEBE CONTENER LETRAS Y NUMEROS !")
                return l.redirect('/')
            
            #-----CREAMOS EL USUARIO MAS AUDITORIA  (PERFIL DEL USUARIO)-----
            miUsuario=l.User.objects.create_user(username, email, pass1)
            miUsuario.first_name=fname
            miUsuario.last_name=lname
            miUsuario.is_active=False
            miUsuario.is_staff=True 
            miUsuario.save()

            persona=l.Persona.objects.create(
                usuarios=username,
                nombre=fname,
                apellido=lname,
                nombreCompleto= (fname + lname),
                Contrasena=pass1,
                PreguntaSecreta=pregunta_secreta,
                Respuesta=encriptado
            )
            #---AQUI REGISTRAMOS LA AUDITORIA-----
            l.messages.success(request, "! USUARIO CREADO CORRECTAMENTE !")
            return l.redirect("IniciarSesion")

        return l.render(request, "autenticacion/Registrar.html")


    #-----CONSULTAS DE USUARIOS POR SP -------------------------
    def ConsultaLogin(request):
        try:
            #----ESTABLEZCO LA CONECTION---
            cursor=l.connection.cursor()

            #---ejectuo la consulta (FUNCION RETURN QUERY)----
            #cursor.execute("select fn_consulta_usuarios(0)")

            #-----INVOCACION DE LA VISTA------
            cursor.execute('select usuarios, nombre, apellido, email from Persona ')

            #-----FUNCION TIPO TABLA----
            #cursor.execute('select fn_cons_usuarios_table(0)')
            
        
            #----OBTENER LOS RESULTADOS
            resultados=cursor.fetchall()

            #---ASI SE OBTIENE LA DATA---
            #"(piedad,Piedad,Armijos,parmijos@gmail.com)"

            result = []

            for row in resultados:
                result.append(list(row))

            context={"resultado":result}
            #print(result)
            return l.render(request, "Usuarios/ConsultaUsuarios.html",context)

        finally:
            cursor.close()









