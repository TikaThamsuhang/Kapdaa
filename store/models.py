from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # if category is deleted, then all products of that category will be deleted
    # This means that Category is the parent of Product since ForeignKey is used.

    created_date = models.DateTimeField(auto_now_add=True) # auto_now_add=True means it will add the current time when the object is created
    modified_date = models.DateTimeField(auto_now=True) # auto_now=True means it will update the current time when the object is modified

    def __str__(self):
        return self.product_name

