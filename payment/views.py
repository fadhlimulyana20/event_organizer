from django.shortcuts import render
from .models import Invoice, Account
from ticketing.models import PricePlan
from django.contrib.auth.decorators import login_required
from .form import UpdateTranferReceipt
from django.views.generic import RedirectView
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
@login_required
def invoice_list_view(request):
    invoice_list = Invoice.objects.filter(eventparticipant__user = request.user)
    context = {
        'invoice_list' : invoice_list
    }

    return render(request, 'invoice_list_view.html', context)

def invoice_payment_method(request, id):
    invoice = Invoice.objects.get(number=id)
    payment_method = Account.objects.filter(role = '1')
    context = {
        'payment_method' : payment_method,
        'invoice' :invoice
    }
    return render(request, 'payment_method.html', context)

class PaymentMethodRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        number = self.kwargs.get('id')
        num = self.kwargs.get('num')
        print(number)
        invoice = Invoice.objects.get(number=number)
        payment_method = Account.objects.get(id=num)
        print(payment_method)
        invoice.account = payment_method
        invoice.save()
        return invoice.get_payment_method_url()


def invoice_detail_view(request, id):
    invoice = Invoice.objects.filter(eventparticipant__user = request.user, number = id)
    event = invoice[0].eventparticipant.event

    if invoice[0].account != None:
        if not invoice[0].is_invoice_due():
            if request.method == 'POST':
                form = UpdateTranferReceipt(request.POST, request.FILES, instance=invoice[0])
                if form.is_valid:
                    update = form.save(commit = False)
                    update.save()
            else:
                form = UpdateTranferReceipt(instance=invoice[0])
            context = {
                'form' : form,
                'invoice' : invoice,
            }

            return render(request, 'invoice_detail_view.html', context)
        else :
            raise Http404("Invoice not Found")
    else:
        return HttpResponseRedirect(invoice[0].eventparticipant.get_payment_method_url())
