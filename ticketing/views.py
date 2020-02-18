from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date

from .models import Event, EventParticipant, EventPayment
from payment.models import Invoice
from .form import UpdateTranferReceipt

from django.views.generic import View
from .utils import render_to_pdf
# from django.template.loader import get_template
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

import barcode
from barcode.writer import ImageWriter
from barcode import generate 
import os.path

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
    event_lecture = EventParticipant.objects.filter(event=obj, role='2')
    context = {
        'object' : obj,
        'event_participant' : event_participant,
        'event_lecture' : event_lecture
    }

    return render(request, 'event_detail_view.html', context)

class GeneratePDF(View):
    def get(self, request, id):
        obj = get_object_or_404(Event, id=id)
        event_participant = EventParticipant.objects.filter(user=request.user, event=obj)
        event_name = obj.event_type.replace(" ", "_")
        # template = get_template('ticket.html')
        context = {
            'object' : obj,
            'event_participant' : event_participant
        }

        # html = template.render(context)
        html = render_to_string("ticket.html", context)
        # pdf = render_to_pdf("ticket.html", context)
        if event_participant[0].invoice :
            if event_participant[0].invoice.pay_status :
                filename = "Ticket_%s_%s.pdf" %(event_name, request.user.username)
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                font_config = FontConfiguration()
                html_response = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(font_config=font_config, presentational_hints=True)
                response = HttpResponse(html_response, content_type='application/pdf')
                response['Content-Disposition'] = content
                return response
        return HttpResponseRedirect(reverse('ticketing:event_detail_view', kwargs={'id': id}))



def event_register_view(request, id):
    event = Event.objects.get(id=id) 
    created = EventParticipant.objects.filter(user=request.user, event=event).exists()  

    if created:
        return HttpResponseRedirect(reverse('ticketing:event_registered_view'))
    else:
        # create_payment = EventPayment.objects.create()
        create = EventParticipant.objects.create(user=request.user, event=event)

        # create barcode
        barcode_type = barcode.get_barcode_class('code128')
        barcode_file = barcode_type("%s_%s" %(event.event_type, create.id), writer=ImageWriter())
        # barcode_file = barcode_type("a_2", writer=ImageWriter())
        save_path = 'static/barcode/'
        file_path = 'barcode/'
        file_name = "barcode_%s_%s" %(event.event_type, create.id)
        fullname = barcode_file.save(os.path.join(save_path, file_name))

        # f = open('/my/new/file', 'wb')
        # ean.write(f) # Pillow (ImageWriter) produces RAW format here
           
        # name = generate('code128', '5901234123457', output='barcode_svg')
        # name
        create.barcode = os.path.join(file_path, file_name+".png")
        create.save()
    
    return HttpResponseRedirect(reverse('ticketing:event_registered_view'))

def event_registered_view(request, *args, **kwargs):
    return render(request, 'event_registered_view.html')

def payment_detail_view(request, id):
    # create_payment = Invoice.objects.create()
    event = Event.objects.get(id=id)
    all_fields = event._meta.get_fields()
    print(all_fields)
    participant = EventParticipant.objects.get(user=request.user, event=event)
    print(participant)
    if participant.invoice:
        return HttpResponseRedirect(participant.get_payment_method_url())
    else:
        create_payment = Invoice.objects.create()
        participant.invoice = create_payment
        participant.save()

    return HttpResponseRedirect(participant.get_payment_method_url())
