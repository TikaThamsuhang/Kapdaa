from django.urls import path
from . import views # import views from current directory

urlpatterns = [
    path("", views.store, name="store"),
    # this slug is for category
    path("<slug:category_slug>/", views.store, name="products_by_category"),
    path("<slug:category_slug>/<slug:product_slug>/", views.product_detail, name="product_detail"),
] 
