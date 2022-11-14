from  Universidad.Funciones import librerias as l
class clsAcademico:

    #-----PANTALLA DE BIENVENIDA AL ACADEMICO-----
    def Inicio(request):
        #-----OBTENEMOS TODA LA CONSULTA DE CURSOS-----
        cursosListados=l.Curso.objects.all().order_by()


        #----OBTENEMOS EL NUMERO DE PAGINA (PAGINACION)------
        page=request.GET.get('page',1)

        try:
            paginator=l.Paginator(cursosListados,3)
            cursosListados=paginator.page(page)

        except:
            raise l.Http404


        l.messages.success(request, '==CURSOS LISTADOS==')
        contexto={
            'entity':cursosListados,
            'paginator':paginator
        }
        return l.render(request,"gestionCursos.html",contexto)


    #----REGISTRO DEL CURSO------
    def registrarCurso(request):
        #---OBTENEMOS LOS DATOS DEL POST----
        codigo=request.POST["txtCodigo"]
        nombre=request.POST["txtNombre"]
        creditos=request.POST["txtNumCreditos"] 

        #print("Codigo: "+codigo)
        #print("Nombre: "+nombre)
        #print("Creditos: "+creditos)

        #----CREAR EL OBJETO MAS REGISTRO-----
        curso=l.Curso.objects.create(
            codigo=codigo,
            nombre=nombre,
            creditos=creditos
        )
        l.messages.success(request, "! CURSO REGISTRADO CORRECTAMENTE !")
        return l.redirect("GestionCursos")


    #------EDICION DE CURSO (BUSQUEDA)---------
    def edicionCurso(request,codigo):
        try:
            curso=l.Curso.objects.get(codigo=codigo)
            context={"curso":curso}

        except Exception:
            curso="No Existente"
            context={"curso":curso}
        
        return l.render(request, "edicionCurso.html", context)

    
    #---EDICION DE CURSO (CUANDO SE REALIZA EL POST)------
    def editarCurso(request):
        codigo=request.POST["txtCodigo"]
        nombre=request.POST["txtNombre"]
        creditos=request.POST["txtNumCreditos"] 

        curso=l.Curso.objects.get(codigo=codigo)
        curso.nombre=nombre
        curso.creditos=creditos
        #----actualizo----
        curso.save()
        l.messages.success(request, '! CURSO ACTUALIZADO !')
        return l.redirect("GestionCursos")



    #-----ELIMINACION DE CURSO-----
    def eliminarCurso(request, codigo):
        curso=l.Curso.objects.get(codigo=codigo)
        curso.delete()
        l.messages.success(request, '! CURSO ELIMINADO OK !')
        return l.redirect("GestionCursos")

