from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='product_photos/')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProductCharacteristic(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_type} - {self.name}"

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/')
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name