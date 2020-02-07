from django.urls import path
from .views import invoice_list_view, invoice_detail_view

app_name = 'payment'
urlpatterns = [
    path('invoice/', invoice_list_view, name='invoice_list_view'),
    path('invoice/detail=<int:id>', invoice_detail_view, name='invoice_detail_view')
]