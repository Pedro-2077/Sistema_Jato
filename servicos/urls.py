from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('novo_servicos/', views.novo_servicos, name='servicos'),
    path('listar_servicos/', views.listar_servicos, name='lista'),

]
