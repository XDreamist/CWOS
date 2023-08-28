from django.shortcuts import render, redirect, get_object_or_404

from chipworld.models import Product, ProductType, Computer, Cctv, Printer

# Create your views here.

def homepage(request):
    products = Product.objects.all()
    product_type = ProductType.objects.all()
    new_prod = Product.objects.filter(new_arrival = True)

    return render(request, 'index.html', {'products': products, 'product_type': product_type, 'new_prod': new_prod})

def shoppage(request):
    products = Product.objects.all()
    product_type = ProductType.objects.all()
    return render(request, 'categories.html', {'products': products, 'product_type': product_type})

def contactpage(request):
    product_type = ProductType.objects.all()
    return render(request, 'contact.html', {'product_type': product_type})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_type = ProductType.objects.all()

    return render(request, 'shop-single.html', {'product': product, 'product_type': product_type})