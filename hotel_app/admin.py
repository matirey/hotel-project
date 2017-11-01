from django.contrib import admin

# Register your models here.
from hotel_app.models import *

admin.site.register(User)
admin.site.register(City)
admin.site.register(Estate)
admin.site.register(Booking)