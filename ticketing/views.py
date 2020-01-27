from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Event, EventParticipant
# Create your views here.

def event_list_view(request, *args, **kwargs):
    queryset = Event.objects.all()
    context = {
        'object_list' : queryset
    }

    return render(request, 'event_list_view.html', context)

def event_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    event_participant = EventParticipant.objects.filter(user=request.user, event=obj, pay_status = True)
    context = {
        'object' : obj,
        'event_participant' : event_participant
    }

    return render(request, 'event_detail_view.html', context)

def event_register_view(request, id):
    event = Event.objects.get(id=id) 
    created = EventParticipant.objects.filter(user=request.user, event=event).exists()

    if created:
        return HttpResponseRedirect(reverse('ticketing:event_registered_view'))
    else:
        create = EventParticipant.objects.create(user=request.user, event=event)
    
    return HttpResponse("Pendaftaran Sukses")

def event_registered_view(request, *args, **kwargs):
    return render(request, 'event_registered_view.html')