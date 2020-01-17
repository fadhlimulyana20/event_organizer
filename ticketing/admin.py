from django.contrib import admin

# Register your models here.
from .models import Event, Localtion
admin.site.register(Event)
admin.site.register(Localtion)