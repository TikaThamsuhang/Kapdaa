from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Store page view: Displays products (all or filtered by category)
def store(request, category_slug=None):
    catergories = None
    products = None

    # If category slug is passed → filter products by category
    if category_slug is not None:
        # Get the category using the slug (404 if not found)
        catergories = get_object_or_404(Category, slug=category_slug)

        # Get only available products from this category
        # is_available=True filters out products that are not available
        # here 'category' is the foreign key in Product model
        products = Product.objects.filter(category=catergories, is_available=True)

    else:
        # If no slug → show all available products
        products = Product.objects.filter(is_available=True)

    # Count number of products (common for both cases)
    products_count = products.count()

    # Data to send to the template
    context = {
        'products': products,
        'product_count': products_count,
    }

    # Render and return the store page
    return render(request, "store/store.html", context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) # category__slug means we are filtering by category slug from Product model
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    
    return render(request, "store/product_detail.html", context)