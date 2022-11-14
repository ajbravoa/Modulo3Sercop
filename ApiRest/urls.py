from django.urls import path
from django.contrib import admin
from .import views
from rest_framework.routers import DefaultRouter

router_post=DefaultRouter()

router_post.register(prefix="ApiRest", basename="ApiRest", viewset=views.ApiPlanificacion)

