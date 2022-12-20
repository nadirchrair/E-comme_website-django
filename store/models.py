from email.policy import default
from django.db import models
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=120)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    desc = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="product")
    image1 = models.FileField(upload_to="product", blank=True, null=True)
    image2 = models.FileField(upload_to="product", blank=True, null=True)
    type = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_detial", kwargs={"slug": self.slug})
    
class Order (models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)


    


    def __str__(self):
        return f"{self.product.name}({self.quantity})"


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    order= models.ManyToManyField(Order)
    
    
    def __str__(self):
        return self.user.username