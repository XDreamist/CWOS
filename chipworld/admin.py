from django.contrib import admin
from .models import ProductType, Company, ProductCharacteristic, Product

admin.site.register(ProductType)
admin.site.register(Company)
admin.site.register(ProductCharacteristic)
admin.site.register(Product)