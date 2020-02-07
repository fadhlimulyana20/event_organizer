from django.db import models
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default='Unnamed Account')
    provider = models.CharField(max_length=100, blank=False, null=False, default='Unnamed Provider')
    number = models.CharField(default='0', max_length=50, blank=False, null=False)
    logo = models.ImageField(upload_to='images/payment/account/', null=True, blank=True)
    role_choice = [
        ('1', 'Company'),
        ('2', 'User'),
    ]
    role = models.CharField(blank=True, choices= role_choice, max_length=1)

class Invoice(models.Model):
    number = models.AutoField(primary_key=True)
    release_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now()+timedelta(days=2))
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    pay_status = models.BooleanField(blank=False, null=False, default=False)
    image_receipt = models.ImageField(upload_to='images/transfer_receipt/', blank=True, null=True)

    def is_invoice_due(self):
        return timezone.now() >= self.due_date
    
    def get_payment_url(self):
        return reverse('payment:invoice_detail_view', kwargs={'id': self.number})


class Place(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default='Unnamed Account')
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
