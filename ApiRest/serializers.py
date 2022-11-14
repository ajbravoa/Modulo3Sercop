from pyexpat import model
from rest_framework import serializers
from .models import Planificacion

class PlanificacionSerialize(serializers.ModelSerializer):
    class Meta:
        model=Planificacion
        fields=['id','nombre','usuario','anio','fecharegistro']



