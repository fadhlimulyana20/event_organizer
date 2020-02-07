from django.shortcuts import render
from .models import Invoice
from django.contrib.auth.decorators import login_required
from .form import UpdateTranferReceipt

# Create your views here.
@login_required
def invoice_list_view(request):
    invoice_list = Invoice.objects.filter(eventparticipant__user = request.user)
    context = {
        'invoice_list' : invoice_list
    }

    return render(request, 'invoice_list_view.html', context)

def invoice_detail_view(request, id):
    invoice = Invoice.objects.filter(eventparticipant__user = request.user, number = id)
    if request.method == 'POST':
        form = UpdateTranferReceipt(request.POST, request.FILES, instance=invoice[0])
        if form.is_valid:
            update = form.save(commit = False)
            update.save()
    else:
        form = UpdateTranferReceipt(instance=invoice[0])
    context = {
        'form' : form,
        'invoice' : invoice
    }

    return render(request, 'invoice_detail_view.html', context)