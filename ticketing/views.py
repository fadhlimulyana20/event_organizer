from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Event, Event_participant
# Create your views here.

def event_list_view(request, *args, **kwargs):
    queryset = Event.objects.all()
    context = {
        'object_list' : queryset
    }

    return render(request, 'event_list_view.html', context)

def event_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    context = {
        'object' : obj
    }

    return render(request, 'event_detail_view.html', context)

def event_register_view(request, id):
    event = Event.objects.get(id=id) 
    created = Event_participant.objects.filter(user=request.user, event=event).exists()

    if created:
        return HttpResponseRedirect(reverse('ticketing:event_registered_view'))
    else:
        create = Event_participant.objects.create(user=request.user, event=event)
    
    return HttpResponse("Pendaftaran Sukses")

def event_registered_view(request, *args, **kwargs):
    return render(request, 'event_registered_view.html')