from django.urls import path

from chipworld import views

urlpatterns = [path('', views.homepage, name = "home"),
               path('products', views.shoppage, name = "shop"),
               path('contact', views.contactpage, name = "contact"),
               path('products/<int:product_id>/', views.product_detail, name = 'product_detail')
               ]