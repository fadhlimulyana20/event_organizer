from django.urls import path
from .views import home_view, signup_view, signin_view, user_logout, edit_user_view, edit_password_view, edit_profile_view, profile_view

app_name = 'registration'
urlpatterns = [
    path('', home_view, name='home'),
    path('sign_up/', signup_view, name='sign_up'),
    path('sign_in/', signin_view, name='sign_in'),
    path('logout/', user_logout, name='user_logout'),
    path('edit/', edit_user_view, name='edit_user'),
    path('change_password/', edit_password_view, name='edit_password'),
    path('edit_profile/', edit_profile_view, name='edit_profile'),
    path('profile/', profile_view, name='profile'),
]