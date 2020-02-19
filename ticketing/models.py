from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime, timedelta
from filemanager.models import Data
from django.utils import timezone
from payment.models import Invoice
from .utils import path_and_rename
import os

# Create your models here.
class Location(models.Model):
    name = models.CharField(default="untitled location", blank=False, null=False, max_length=120)
    street = models.CharField(default="untitled street", blank=False, null=False, max_length=300)
    sub_district = models.CharField(default="untitled sub district", blank=False, null=False, max_length=120)
    city = models.CharField(default="untitled city", blank=False, null=False, max_length=120)
    province_or_state = models.CharField(default="untitled province", blank=False, null=False, max_length=120)
    country = models.CharField(default="untitled country", blank=False, null=False, max_length=120)
    postal_code = models.DecimalField(decimal_places=0, max_digits=5)
    google_maps = models.URLField(blank=True, null=True)

    def __str__(self):
        return '%s, %s' %(self.city, self.province_or_state)

class Event(models.Model):
    name = models.CharField(default="untitled event", blank=False, null=False, max_length=120)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now_add=False, auto_now=False)
    due_registration = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now()-timedelta(days=3))
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
    document = models.ManyToManyField('Document', related_name='event_document')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ticketing:event_detail_view', kwargs={'id': self.id})

    def get_register_url(self):
        return reverse('ticketing:event_register_view', kwargs={'id': self.id})
    
    def get_payment_url(self):
        return reverse('ticketing:payment_detail_view', kwargs={'id': self.id})
    
    def get_ticket_url(self):
        return reverse('ticketing:generate_pdf', kwargs={'id': self.id})

    
    @property
    def is_past_due(self):
        return date.today() >= self.date

    def is_registration_due(self):
        return date.today() >= self.due_registration

class EventParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    roles = [
        ('1', 'Peserta'),
        ('2', 'Narasumber')
    ]
    role = models.CharField(blank=False, max_length=1, choices=roles, default='1')
    # payment = models.OneToOneField('EventPayment', on_delete=models.CASCADE, null=True)
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    barcode = models.URLField(blank=True, null=True, editable=False)
    # barcode_image = models.ImageField(upload_to='media/barcode')

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    
    def get_payment_method_url(self):
        if self.invoice:
            return reverse('payment:invoice_payment_method_view', kwargs={'id': self.invoice.number})
        return 

class DataEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)

    def __str__(self):
        return self.data.file.name

class EventPayment(models.Model):
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now()+timedelta(days=2))
    pay_status = models.BooleanField(blank=False, null=False, default=False)
    image_receipt = models.ImageField(upload_to='images/transfer_receipt/', blank=True, null=True)

class Document(models.Model):
    name = models.CharField(default="untitled document", blank=False, null=False, max_length=150)
    date_of_release = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='media/document/pdf/', blank=True, null=True)

    def filename(self):
        return os.path.basename(self.file.name)
