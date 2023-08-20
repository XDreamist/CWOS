from django.urls import path

from chipworld import views

urlpatterns = [path('', views.homepage, name = "home"),
               path('about', views.aboutpage, name = "about"),
               path('shop', views.shoppage, name = "shop"),
               path('contact', views.contactpage, name = "contact"),
               path('cart', views.cartpage, name = "cart"),
               path('checkout', views.checkoutpage, name = "checkout"),
               path('thankyou', views.thankyoupage, name = "thankyou"),
               # path('addproduct', views.addproductpage, name = "addproduct"),
               ]