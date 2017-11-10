from django.shortcuts import render
from hotel_app.models import City, Estate, Booking
from hotel_app.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.html import escape
import datetime

# Create your views here.
def index(request):
    if request.method == 'GET':
        cities = City.objects.all()
        if 'filter' in request.GET:
            FilteredEstates = Estate.objects.all().filter(city = request.GET['idCity'], maxPax = request.GET['maxPax'])
            context = {
                'estates': FilteredEstates,
                'cities': cities
            }
            return render(request, 'estate/index.html', context)
        else:
            estates = Estate.objects.all()

            context = {
                'estates' : estates ,
                'cities' : cities
            }
            return render(request, 'estate/index.html', context)

def hosts(request):
    hosts = User.objects.all()
    context = {
        'hosts': hosts
    }
    return render(request, 'host/index.html', context)

def index_reserve(request, id_estate):
    estate = Estate.objects.get(id = id_estate)
    form = ResidentForm(initial={'name': 'Federico', 'surname': 'Palomero', 'email':'aldosivi@yahoo.com'})
    now = datetime.datetime.now
    context = {
        'e': estate,
        'form' : form,
        'now':now
    }
    return render(request, 'reserve/index.html', context)

#def make_reserve(request, id_estate):
    #try:
    #    estate = Estate.objects.get(id=id_estate)
    #    Booking booking = new Booking(datetime.datetime.now(), estate.price, #total_price, resident)
    #except(e):
    #print(e)