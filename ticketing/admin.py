from django.contrib import admin

# Register your models here.
from .models import Event, Location, EventParticipant, DataEvent

class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'role', 'pay_status')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'event_type', 'date', 'time')

class DataEventAdmin(admin.ModelAdmin):
    list_display = ('id','event', 'data')

admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(EventParticipant, EventParticipantAdmin)
admin.site.register(DataEvent, DataEventAdmin)