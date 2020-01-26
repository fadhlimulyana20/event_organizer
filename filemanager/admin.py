from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('id' ,'file', 'date_created')
admin.site.register(Data, DataAdmin)
