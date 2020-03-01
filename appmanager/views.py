from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dash_admin_view(request):
    return HttpResponse('good')
