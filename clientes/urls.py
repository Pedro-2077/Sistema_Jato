from django.urls import path
from . import views

urlpatterns = [

    path('', views.clientes, name='clientes'),
    path('atualizar_cliente/', views.att_cliente, name='atualizar_cliente'),
    path('update_carro/<int:id>', views.update_carro, name='update_carro'),
    path('excluir_carro/<int:id>', views.excluir_carro, name='excluir_carro'),
    path('update_cliente/<int:id>', views.update_cliente, name='update_cliente'),

]

#path('', home, name='hm') HOME é uma função que vamos receber nossas requisições

