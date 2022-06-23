import email
from time import monotonic
from django.db import models

# Create your models here.
class Financiamiento_estudiantil(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=25, null=True)
    apellido = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=20, null=True, unique=True)
    telefono = models.CharField(max_length=11, null=True, unique=True)
    monto = models.IntegerField()
    producto = models.CharField(max_length=50, null=True)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
    