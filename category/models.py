from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) #blank=True means it is optional

    # Meta class is used to provide additional information about the model
    class Meta:
        # To change the name of the model in the admin panel
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.category_name