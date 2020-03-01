from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from payment.models import Invoice
from ticketing.models import EventParticipant
from django.core.paginator import Paginator


# Create your views here.
def superuser_check(user):
    return user.is_superuser

@user_passes_test(superuser_check)
def dash_admin_view(request):
    user = User.objects.all()
    invoice = Invoice.objects.filter(pay_status=True)
    invoice_debt = Invoice.objects.filter(pay_status=False)

    get_income = 0
    for instance in invoice:
        get_income += instance.price

    context = {
        'user' : user,
        'invoice' : invoice,
        'invoice_debt' : invoice_debt,
        'get_income' : get_income
    }
    return render(request, 'manager_home.html', context)

@user_passes_test(superuser_check)
def user_admin_view(request):
    user = User.objects.all()
    paginator = Paginator(user, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj
    }

    return render(request, 'user_management.html', context)

@user_passes_test(superuser_check)
def ep_admin_view(request):
    event_participant = EventParticipant.objects.all()
    paginator = Paginator(event_participant, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj
    }

    return render(request, 'ep_management.html', context)