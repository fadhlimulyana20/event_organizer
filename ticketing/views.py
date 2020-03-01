from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date

from .models import Event, EventParticipant, EventPayment, PricePlan
from payment.models import Invoice
from .form import UpdateTranferReceipt

from django.views.generic import View
# from .utils import render_to_pdf
# from django.template.loader import get_template
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

import barcode
from barcode.writer import ImageWriter
from barcode import generate 
import os.path

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
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

@login_required
def my_event_view(request, *args, **kwargs):
    event_participant = EventParticipant.objects.filter(user=request.user)

    # for i in event_participant:
    #     if i.invoice:
    #         if i.invoice.is_invoice_due and i.invoice.pay_status == False:
    #             i.delete()

    context = {
        'event_participant' : event_participant
    }

    return render(request, 'my_event_view.html', context)

@login_required
def event_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    event_participant = EventParticipant.objects.filter(user=request.user, event=obj)

    profession_code = request.user.profile.get_profession_code()
    print('code : ', profession_code)
    
    price = PricePlan.objects.get(event_price_plan = obj, role= profession_code)
    event_lecture = EventParticipant.objects.filter(event=obj, role='2')

    # if event_participant.count() > 0 :
    #     if event_participant[0].invoice:
    #         if event_participant[0].invoice.is_invoice_due and event_participant[0].invoice.pay_status == False:
    #             event_participant[0].delete()
    #             return HttpResponseRedirect(reverse('ticketing:my_event_view'))

    context = {
        'object' : obj,
        'event_participant' : event_participant,
        'event_lecture' : event_lecture,
        'price' : price
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
        if event_participant.count() > 0:
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


@login_required
def event_register_view(request, id):
    event = Event.objects.get(id=id) 
    created = EventParticipant.objects.filter(user=request.user, event=event).exists()
    event_participant = EventParticipant.objects.filter(user=request.user, event=event)
    invoice = Invoice.objects.filter(eventparticipant = event_participant.first())

    if invoice.exists and created:
        if invoice.first().is_invoice_due:
            event_participant.first().delete()
            create = EventParticipant.objects.create(user=request.user, event=event)

            # create barcode
            barcode_type = barcode.get_barcode_class('code128')
            barcode_file = barcode_type("%s_%s" %(event.event_type, create.id), writer=ImageWriter())

            save_path = 'static/barcode/'
            file_path = 'barcode/'
            file_name = "barcode_%s_%s" %(event.event_type, create.id)
            # fullname = barcode_file.save(os.path.join(save_path, file_name))

            
            f = open(os.path.join(save_path, file_name)+'.png', 'wb')
            barcode_file.write(f) # Pillow (ImageWriter) produces RAW format here

            create.barcode = os.path.join(file_path, file_name+".png")
            create.save()

        elif not invoice.first().is_invoice_due:
            return HttpResponseRedirect(reverse('ticketing:event_detail_view', kwargs={'id': id}))
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
        # fullname = barcode_file.save(os.path.join(save_path, file_name))

        f = open(os.path.join(save_path, file_name)+'.png', 'wb')
        barcode_file.write(f) # Pillow (ImageWriter) produces RAW format here
           
        # name = generate('code128', '5901234123457', output='barcode_svg')
        # name
        create.barcode = os.path.join(file_path, file_name+".png")
        create.save()
    
    return HttpResponseRedirect(reverse('ticketing:event_detail_view', kwargs={'id': id}))

def event_registered_view(request, *args, **kwargs):
    return render(request, 'event_registered_view.html')

@login_required
def payment_detail_view(request, id):
    # create_payment = Invoice.objects.create()
    event = Event.objects.get(id=id)
    all_fields = event._meta.get_fields()
    print(all_fields)
    participant = EventParticipant.objects.get(user=request.user, event=event)
    print(participant)

    profession_code = request.user.profile.get_profession_code()
    print('code : ', profession_code)
    
    price = PricePlan.objects.get(event_price_plan = event , role= profession_code)
    get_price = price.price

    if participant.invoice:
        return HttpResponseRedirect(participant.get_payment_method_url())
    else:
        create_payment = Invoice.objects.create(price = get_price)
        participant.invoice = create_payment
        participant.save()

    return HttpResponseRedirect(participant.get_payment_method_url())
