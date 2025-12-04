from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} # automatically creates slug
    list_display = ('category_name', 'slug', 'cat_image') # displays in admin panel

admin.site.register(Category, CategoryAdmin)

