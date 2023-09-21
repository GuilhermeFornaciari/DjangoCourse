from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    perguntas = models.pergunta.objects.all()
    pacote = { 'perguntas' : perguntas}
    return render(request,'index.html',pacote)

def votacao(request,pergunta_id):
    pergunta = get_object_or_404(models.pergunta,pk=pergunta_id)    
    pacote = { 'pergunta' : pergunta }
    return render(request,'votacao.html', pacote)

def resultado(request,pergunta_id):
    return HttpResponse("Oi, eu sou o resultado")