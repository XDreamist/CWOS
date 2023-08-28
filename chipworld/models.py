from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    image1 = models.ImageField(upload_to='product_images/', blank=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True)
    image4 = models.ImageField(upload_to='product_images/', blank=True)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    specification = models.TextField(max_length=500)
    new_arrival = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name

class Slides(models.Model):
    heading = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slide_images/', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)