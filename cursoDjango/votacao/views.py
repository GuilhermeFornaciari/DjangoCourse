from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    perguntas = models.pergunta.objects.all()
    pacote = { 'perguntas' : perguntas}
    return render(request,'index.html',pacote)

def votacao(request,votacao_id):
    return HttpResponse("Oi, eu sou a pagina de votacao")

def resultado(request):
    return HttpResponse("Oi, eu sou o resultado")