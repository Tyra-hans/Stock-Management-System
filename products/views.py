from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Product


def products(request):
    products = Product.objects.all()
    
    return render(request, 'products.html',{"products": products})