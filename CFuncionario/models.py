from django.db import models
from django.forms import EmailField

# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=50,  primary_key=True)
    Email = models.CharField(max_length=60)
    Contraseña = models.CharField(max_length=15)

