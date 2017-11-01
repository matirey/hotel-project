from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, null = False, blank = False)

    def __str__(self):
        return self.name;

class User(models.Model):
    name = models.CharField(max_length=50, null = False, blank = False)
    lastName = models.CharField(max_length = 50, null = False, blank = False)
    email = models.EmailField(max_length = 50, null = False, blank = False)
    userName = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name + ' ' + self.lastName + ' (' + self.userName + ')';

class Estate(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    confort= models.TextField(null=True, blank=True)
    services = models.TextField(null=True, blank=True)
    maxPax = models.IntegerField(null=False, blank=False, default=1)
    dateFrom = models.DateTimeField(null=False, blank=False)
    dateTo = models.DateTimeField(null=False, blank=False)
    price = models.FloatField(null=False, blank=True, default=0)
    image = models.CharField(max_length=512, null=True, blank=True)
    city = models.ForeignKey(City, null=False, blank=False)
    host = models.OneToOneField(User, null=False, blank=False)

class Booking(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    estate = models.ForeignKey(Estate, null=False, blank=False)
    resident = models.OneToOneField(User, null=False, blank=False, related_name='fk_resident')