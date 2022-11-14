from  Universidad.Funciones import librerias as l


class clsBlog:

    #------PRESENTACION DE BLOGS-----
    def PresentarBlog(request):
        post=l.Post.objects.all()
        context={'post':post}
        return l.render(request,"Blog/blog.html",context)

    #-------VISUALIZACION DE LOS COMNENTARIOS-----
    def post_detail(request, post_id):
        
        #----RECUPERO EL TITULO PRINCIPAL (BLOG)-----
        post=l.Post.objects.get(Id=post_id)

        #----VOY A MOSTAR LOS COMENTARIOS ACTIVOS---
        comentarios=post.comentarios.filter(Estado=True)

        #----GRABO EN UNA VARIABLE SESION---
        request.session["PostID"]=post_id
        context={"comentarios":comentarios}
        return l.render(request, "Blog/post_detail.html",context)

    #-----GRABAR COMENTARIOS-----
    def grabarComentarios(request):
        Nombres=request.session["FullName"]
        email= request.session["email"]
        usuario=request.session["usuario"]
        comentarios=request.POST["txtComentario"]

        resultado=l.Comentario.objects.create(
            post_id=request.session["PostID"],
            Nombre=Nombres,
            Email=email,
            UsuarioCreacion=usuario,
            Contenido=comentarios,
            Estado=True
        )

        return l.redirect("post_detalle/"+str(request.session["PostID"]))


        



        

     
        





