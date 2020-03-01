from django.urls import include, path
from .views import dash_admin_view, user_admin_view
app_name = 'appmanager'

urlpatterns = [
    path('', dash_admin_view, name='dash_admin_view'),
    path('user/', user_admin_view, name='user_admin_view')
]