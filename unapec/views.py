from django.shortcuts import render
import requests
import json
from .models import Financiamiento_estudiantil
# Create your views here.

def home(request):
    
    return render(request, 'unapec/home.html')

def send(request):
    
    headers = {'Content-Type' : 'application/json'}
    
    financiamiento = list(Financiamiento_estudiantil.objects.all().values("nombre","apellido","email","telefono","monto","producto"))
    
    requests.post('http://localhost:3000/credito-estudiantil', data=json.dumps(financiamiento), headers=headers)
    
    return render(request, 'unapec/home.html')