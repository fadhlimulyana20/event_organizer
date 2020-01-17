from django.db import models

# Create your models here.
class Localtion(models.Model):
    name = models.CharField(default="untitled location", blank=False, null=False, max_length=120)
    street = models.CharField(default="untitled street", blank=False, null=False, max_length=300)
    sub_district = models.CharField(default="untitled sub district", blank=False, null=False, max_length=120)
    city = models.CharField(default="untitled city", blank=False, null=False, max_length=120)
    province_or_state = models.CharField(default="untitled province", blank=False, null=False, max_length=120)
    country = models.CharField(default="untitled country", blank=False, null=False, max_length=120)
    postal_code = models.DecimalField(decimal_places=0, max_digits=5)

class Event(models.Model):
    name = models.CharField(default="untitled event", blank=False, null=False, max_length=120)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now_add=False, auto_now=False)
    topic = models.CharField(default="untitled topic", blank=False, null=False, max_length=120)
    location = models.ForeignKey(Localtion, on_delete=models.CASCADE)

