from django.shortcuts import render
from hotel_app.models import *

# Create your views here.
def index(request):
    estates = Estate.objects.all()
    contexto = { 'estates' : estates }
    return render(request, 'estate/index.html', contexto)