from django.shortcuts import render, redirect

from chipworld.models import Product, ProductType


# from chipworld.forms import addproductForm


# Create your views here.

def homepage(request):
    products = Product.objects.all()
    product_type = ProductType.objects.all()
    return render(request, 'index.html', {'products': products, 'product_type': product_type})

def aboutpage(request):
    return render(request, 'about.html')

def shoppage(request):
    products = Product.objects.all()
    product_type = ProductType.objects.all()
    return render(request, 'categories.html', {'products': products, 'product_type': product_type})

def contactpage(request):
    return render(request, 'contact.html')

def cartpage(request):
    return render(request, 'cart.html')

def checkoutpage(request):
    return render(request, 'checkout.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})