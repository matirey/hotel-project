from django.shortcuts import render
from hotel_app.models import City, Estate, Booking, Resident
from hotel_app.forms import ResidentForm
from django.contrib.auth.models import User
from django.contrib import messages
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
    messages = None
    if request.method == 'GET':
        estate = Estate.objects.get(id = id_estate)
        form = ResidentForm(initial={'name': 'Federico', 'surname': 'Palomero', 'email':'aldosivi@yahoo.com'})
        now = datetime.datetime.now
        context = {
            'e': estate,
            'form' : form,
            'now':now
        }
        return render(request, 'reserve/index.html', context)


    if request.method == 'POST': #Cuando se envía la info para la reserva
        try:
            estate = Estate.objects.get(id = id_estate)
            resident = Resident(name = request.POST['name'], surname = request.POST['surname'], email = request.POST['email'])
            resident.save()
            booking = Booking(date = datetime.datetime.now(), total_price =  estate.price, resident = resident)
            context = {
                'booking':booking,
                'e' : estate
            }
            booking.save()
            messages.success(request, "Reserva concretada con éxito")
            return render(request, 'reserve/index.html', context)
        except Exception as e:
            print(e)


