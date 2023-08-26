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
    prod_details = None

    if product.type == "Computer":
        prod_details = Computer.objects.filter(name=product.name).first()
        print("Computer details:", prod_details)
    elif product.type == "Cctv":  prod_details = Cctv.objects.filter(name=product.name).first()
    elif product.type == "Printer":  prod_details = Printer.objects.filter(name=product.name).first()

    return render(request, 'shop-single.html', {'product': product, 'product_type': product_type, 'details': prod_details})