from django.contrib import admin

# Register your models here.
from .models import Account, Invoice

admin.site.register(Account)
admin.site.register(Invoice)