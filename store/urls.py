from django.urls import path
from . import views # import views from current directory

urlpatterns = [
    path("", views.store, name="store"),
    # this slug is for category
    path("<slug:category_slug>/", views.store, name="products_by_category"),
] 
