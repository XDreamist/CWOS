from django.contrib import admin
from .models import ProductType, Company, Product, Printer, Computer, Cctv

admin.site.register(ProductType)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Printer)
admin.site.register(Computer)
admin.site.register(Cctv)