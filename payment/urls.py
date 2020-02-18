from django.urls import path
from .views import invoice_list_view, invoice_detail_view, invoice_payment_method, PaymentMethodRedirect

app_name = 'payment'
urlpatterns = [
    path('invoice/', invoice_list_view, name='invoice_list_view'),
    path('invoice/detail=<int:id>', invoice_detail_view, name='invoice_detail_view'),
    path('method/for=<int:id>', invoice_payment_method, name='invoice_payment_method_view'),
    path('method/for=<int:id>/select=<int:num>/', PaymentMethodRedirect.as_view(), name='invoice_payment_method_redirect')
]