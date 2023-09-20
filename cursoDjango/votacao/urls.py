from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:votacao_id>',views.votacao,name='votacao'),
    path('<int:votacao_id>/votar',views.resultado, name='votar'),
    path('<int:votacao_id>/resultado',views.resultado, name='resultado')

]
