from django.shortcuts import render, redirect

from chipworld.forms import addproductForm


# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def shoppage(request):
    return render(request, 'shop.html')

def contactpage(request):
    return render(request, 'contact.html')

def cartpage(request):
    return render(request, 'cart.html')

def checkoutpage(request):
    return render(request, 'checkout.html')

def thankyoupage(request):
    return render(request, 'thankyou.html')

def addproductpage(request):
    if request.method == 'POST':
        form = addproductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addproductForm()

    return render(request, 'addproduct.html', {'addform': form})