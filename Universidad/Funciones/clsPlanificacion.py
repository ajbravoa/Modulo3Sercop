from Universidad.Funciones import librerias as l
import json

class clsPlanificacion:
    def GrabarPlanificacion(request):
        if request.method=="POST":
            if request.POST.get("txtPlanificacion") and request.POST.get("txtAnio"):
                #---INSTANCIANDO A LA CLASE -----
                resultado=l.pa_ingreso_planificacion()
                resultado.Nombre=request.POST.get("txtPlanificacion")
                resultado.Usuario=request.session["usuario"]
                resultado.Anio=request.POST.get("txtAnio")

                #try:
                    #------INSERCION DIRECTA A BASE DE DATOS CON STORE PROCEDURES-------
                    #cursor=l.connection.cursor()
                    #print ("call pa_ingreso_planificacion('"+ resultado.Nombre+"','"+resultado.Usuario+"','"+resultado.Anio+"')")
                    
                    #----EJECUTO EL SP-----
                    #cursor.execute("call pa_ingreso_planificacion('"+ resultado.Nombre+"','"+resultado.Usuario+"','"+resultado.Anio+"')")

                    #l.messages.success(request,"¡PLANIFICACION CORRECTAMENTE INGRESADA!")

                    #return l.render(request,"planificacion/planin.html")

                    #-----INSERCION CON REST API -----------
                data=json.dumps(
                    {
                        "id": 0,
                        "nombre": resultado.Nombre ,
                        "usuario": resultado.Usuario,
                        "anio": resultado.Anio
                    }
                )
                print (data)
                data_planificacion=data
                headers={
                        "accept":"application/json"
                    }
                respuesta=l.requests.post("http://localhost:8000/ApiPlanificacion",data=data_planificacion,headers=headers)
                print ("Respuesta: "+respuesta.text)
                print("Codigo Respuesta: "+str(respuesta.status_code))

                l.messages.success(request,"Planificacion grabada correctamente")
                return l.redirect("/ConsultarPlanificacion")

                #except:
                    #l.messages.error(request,"HUBO UN ERROR EN GRABAR LA PLANIFICACION")

                #---CERRAMOS LA CONEXION----
                #finally:
                    #cursor.close()

            #return l.redirect("/ConsultarPlanificacion")
        else:
            #return l.render(request,"planificacion/planin.html")
            return l.redirect("/ConsultarPlanificacion")

    #----CONNSULTA DE PLANFICIACIONES POR API-------
    def ConsultarPlanificacion(request):

        #--- INVOCO A LA URL DEL API (GET)
        respuesta=l.requests.get("http://localhost:8000/ApiPlanificacion")
        json=respuesta.json()
        #print(json)
        contexto={"JsonTables":json}
        return l.render(request, "planificacion/planin.html",contexto)


       

