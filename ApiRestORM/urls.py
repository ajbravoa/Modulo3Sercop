from django.urls import path
from ApiRestORM import views


urlpatterns = [
    path('ApiPlanificacion', views.PlanificacionApi, name="ApiPlanificacion"),
    path('ApiPlanificacion/<int:id>', views.PlanificacionApi, name="ApiPlanificacion"),

]