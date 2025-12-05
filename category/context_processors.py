from .models import Category

def menu_links(request):
    categories = Category.objects.all() # this will return all categories to all templates
    return dict(links=categories) # dict is used to return a dictionary