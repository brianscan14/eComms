from django.shortcuts import render
from products.models import Product


# filter is a built in function, gets whatever q is returned from form, form name will be q
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
