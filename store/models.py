from django.db import models
from category.models import Category
from django.urls import reverse

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

    def get_url(self):
        # reverse() generates a URL by looking at the name given in urls.py.
        # Here, 'product_detail' is the name of the URL pattern used
        # for displaying a single product's detail page.
        
        # 'args' provides the dynamic parts of the URL.
        # In your urls.py, your product detail URL likely looks like this:
        # path('category/<slug:category_slug>/<slug:product_slug>/', ...)
        #
        # So we need to provide 2 values in order:
        # 1. category_slug  → self.category.slug (slug of the product's category)
        # 2. product_slug   → self.slug (slug of the product itself)
        
        # This returns a complete URL like:
        # /category/electronics/iphone-14-pro/
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

