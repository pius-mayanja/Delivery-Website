from django.shortcuts import render, get_object_or_404
from .models import Product

def items(request):
    product = Product.objects.all()
    return render(request, 'product/home.html', {'products': product,})


def details(request, pk):
    product = get_object_or_404(Product, id=pk)
    related_items = Product.objects.filter(category=product.category).exclude(pk=pk)
    return render(request, 'product/details.html', {'product':product,
                                                    'related':related_items} )
