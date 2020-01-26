from django.urls import path
from .views import event_list_view, event_detail_view, event_registered_view, event_register_view

app_name = 'ticketing'

urlpatterns = [
    path('daftar_event/', event_list_view, name='event_list_view'),
    path('daftar_event/<int:id>/', event_detail_view, name='event_detail_view'),
    path('registered/', event_registered_view, name='event_registered_view'),
    path('register/<int:id>/', event_register_view, name='event_register_view')
]