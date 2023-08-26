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
    new_arrival = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name

class Printer(Product):
    print_type = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    connectivity = models.CharField(max_length=50)
    paper_handling = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = "Printer"
        super(Printer, self).save(*args, **kwargs)

class Computer(Product):
    processor = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = "Computer"
        super(Computer, self).save(*args, **kwargs)

class Cctv(Product):
    resolution = models.CharField(max_length=50)
    nightvision = models.CharField(max_length=50)
    fov = models.CharField(max_length=50)
    connectivity = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = "Cctv"
        super(Cctv, self).save(*args, **kwargs)