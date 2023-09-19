from django.db import models

# Create your models here.
class pergunta(models.Model):
    texto = models.CharField(max_length=200)
    
class alternativa(models.Model):
    idPergunta = models.ForeignKey(pergunta,on_delete=models.CASCADE)
    texto = models.CharField(max_length=70)
    votos = models.IntegerField(default=0)