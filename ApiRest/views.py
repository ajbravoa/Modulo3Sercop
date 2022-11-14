from django.shortcuts import render
from .models import Planificacion
from .serializers import PlanificacionSerialize
from rest_framework import viewsets


# Create your views here.
class ApiPlanificacion(viewsets.ModelViewSet):
    queryset=Planificacion.objects.raw("select *from fn_cons_planificacion(0)")
    #print(queryset)
    serializer_class=PlanificacionSerialize