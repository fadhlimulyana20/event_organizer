from django.contrib import admin

# Register your models here.
from .models import Event, Location, Event_participant

class Event_participantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'role')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_type', 'date', 'time')

admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(Event_participant, Event_participantAdmin)