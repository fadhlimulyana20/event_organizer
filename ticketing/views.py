from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date

from .models import Event, EventParticipant, EventPayment
from .form import UpdateTranferReceipt
# Create your views here.

def event_list_view(request, *args, **kwargs):
    seminar_list = Event.objects.filter(due_registration__gt=date.today()).filter(event_type="SM")
    pelatihan_list = Event.objects.filter(due_registration__gt=date.today()).filter(event_type="PL")
    workshop_list = Event.objects.filter(due_registration__gt=date.today()).filter(event_type="WS")
    seminar_workshop_list = Event.objects.filter(due_registration__gt=date.today()).filter(event_type="SW")
    context = {
        'seminar_list' : seminar_list,
        'pelatihan_list' : pelatihan_list,
        'workshop_list' : workshop_list,
        'seminar_workshop_list' : seminar_workshop_list,
    }

    return render(request, 'event_list_view.html', context)

def my_event_view(request, *args, **kwargs):
    event_participant = EventParticipant.objects.filter(user=request.user)
    context = {
        'event_participant' : event_participant
    }

    return render(request, 'my_event_view.html', context)


def event_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    event_participant = EventParticipant.objects.filter(user=request.user, event=obj)
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
        create_payment = EventPayment.objects.create()
        create = EventParticipant.objects.create(user=request.user, event=event, payment=create_payment)
    
    return HttpResponse("Pendaftaran Sukses")

def event_registered_view(request, *args, **kwargs):
    return render(request, 'event_registered_view.html')

def payment_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    event_participant = EventParticipant.objects.filter(user=request.user, event=obj)
    if request.method == 'POST':
        form = UpdateTranferReceipt(request.POST, request.FILES, instance=event_participant[0].payment)
        if form.is_valid:
            update = form.save(commit = False)
            update.save()
    else:
        form = UpdateTranferReceipt(instance=event_participant[0].payment)
    context = {
        'object' : obj,
        'event_participant' : event_participant,
        'form' : form
    }

    return render(request, 'payment_detail_view.html', context)