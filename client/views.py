from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .models import Client

def clients(request):
    clients = Client.objects.all()

    return render(request, 'clients.html',{"clients": clients})


