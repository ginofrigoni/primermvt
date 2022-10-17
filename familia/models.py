from django.db import models
#from django.utils import timezone

# Create your models here.
class Integrante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(default = None)
    alta = models.DateField(default = None)