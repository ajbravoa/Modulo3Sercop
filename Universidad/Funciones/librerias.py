from re import S
from django.shortcuts import render, redirect
from Universidad.models import Curso, Persona, Pregunta,Post,Comentario

#----STORE PROCEDURES-----
from Universidad.models import pa_ingreso_planificacion

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages
#----INCLUIR MAS LIBRERIAS ------

from django.contrib.auth.models import UserManager, User
from django.core.paginator import Paginator
from django.http import Http404

#---INCORPORO LA LIBRERIA PASSLIB (ENCRIPTACION) ------
from passlib.hash import pbkdf2_sha256

#----LIBRERIA PARA STORE PROCEDURES----
from django.db import connection

import requests
