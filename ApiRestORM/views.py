import collections
from http.client import HTTPResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from .models import Planificacion
from .serializers import PlanificacionSerialize
import json
from .Utilitarios import Utilitarios as u

#----LIBRERIA PARA STORE PROCEDURES----
from django.db import connection

@csrf_exempt
def PlanificacionApi(request, id=0):
    Id=None
    NombrePlanificacion=None
    Usuario=None
    Anio=None
    FechaRegistro=None

    cursor=connection.cursor()
    if request.method=='GET':
        cursor.execute('select id,nombre,usuario,anio, fecharegistro from fn_cons_planificacion(0) where id>0')
        #---RECUPERO LOS REGISTROS---
        resultados=cursor.fetchall()

        #--DECLARAMOS LA LISTA
        result=[]

        #----PRIMERA FORMA------
        #for row in resultados:
        #    items=(row[0], row[1],row[2],row[3])
        #    result.append(items)

        #------SEGUNDA FORMA--------
        for row in resultados:
            coleccion=collections.OrderedDict()
            coleccion["id"]=row[0]
            coleccion["nombre"]=row[1]
            coleccion["usuario"]=row[2]
            coleccion["anio"]=row[3]
            coleccion["fecharegistro"]=str(row[4])

            result.append(coleccion)

        #print(result)
        jsonConsulta=json.dumps(result)
        serializer = PlanificacionSerialize(result, many=True)
        #print("========DESPUES===========")
        #print(jsonConsulta)
        return JsonResponse(serializer.data, safe=False)

    #----- INSERTAR O ACTUALIZAR ------
    elif request.method=='POST':
        #----VALIDO EL FORMATO DEL JSON ENVIADO---
        planificacion_data=JSONParser().parse(request)
        
        planificacion_serializer=PlanificacionSerialize(data=planificacion_data)

        if planificacion_serializer.is_valid():
            jsonResultados=json.dumps(planificacion_data)
            dict_json=json.loads(jsonResultados)
            Id=dict_json["id"]
            NombrePlanificacion=dict_json["nombre"]
            Usuario=dict_json["usuario"]
            Anio=dict_json["anio"]

            #print(Id)
            #print(NombrePlanificacion)
            #print(Usuario)
            #print(Anio)
            print("call pa_ing_act_planin('"+str(Id)+"','"+NombrePlanificacion+"','"+Usuario+"','"+str(Anio)+"')")
            cursor.execute("call pa_ing_act_planin('"+str(Id)+"','"+NombrePlanificacion+"','"+Usuario+"','"+str(Anio)+"')")

            return JsonResponse(u.Mensajes.CreacionOK(),safe=False)

    return JsonResponse("Codigo Error: 400 - Error en la peticion", safe=False)








       

















