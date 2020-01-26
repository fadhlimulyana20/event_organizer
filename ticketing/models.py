from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from filemanager.models import Data

# Create your models here.
class Location(models.Model):
    name = models.CharField(default="untitled location", blank=False, null=False, max_length=120)
    street = models.CharField(default="untitled street", blank=False, null=False, max_length=300)
    sub_district = models.CharField(default="untitled sub district", blank=False, null=False, max_length=120)
    city = models.CharField(default="untitled city", blank=False, null=False, max_length=120)
    province_or_state = models.CharField(default="untitled province", blank=False, null=False, max_length=120)
    country = models.CharField(default="untitled country", blank=False, null=False, max_length=120)
    postal_code = models.DecimalField(decimal_places=0, max_digits=5)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(default="untitled event", blank=False, null=False, max_length=120)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now_add=False, auto_now=False)
    topic = models.CharField(default="untitled topic", blank=False, null=False, max_length=120)
    event_type_choice = [
        ('SM', 'Seminar'),
        ('HO', 'Hand On'),
        ('PL', 'Pelatihan'),
        ('WS', 'Workshop'),
        ('SW', 'Seminar dan workshop')
    ]
    event_type = models.CharField(blank=True, choices= event_type_choice, max_length=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(User, through='EventParticipant', related_name='participants')
    price = models.DecimalField(decimal_places=0, max_digits=10, default=0)
    data = models.ManyToManyField(Data, through="DataEvent", related_name="data_event")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ticketing:event_detail_view', kwargs={'id': self.id})

    def get_register_url(self):
        return reverse('ticketing:event_register_view', kwargs={'id': self.id})
    
    @property
    def is_past_due(self):
        return date.today() > self.date

class EventParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    roles = [
        ('1', 'Peserta'),
        ('2', 'Narasumber')
    ]
    role = models.CharField(blank=False, max_length=1, choices=roles, default='1')
    pay_status = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class DataEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)

    def __str__(self):
        return self.data.file.name
