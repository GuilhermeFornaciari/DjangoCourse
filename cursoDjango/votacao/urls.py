from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:pergunta_id>',views.votacao,name='votacao'),
    path('<int:pergunta_id>/votar',views.resultado, name='votar'),
    path('<int:pergunta_id>/resultado',views.resultado, name='resultado')

]
