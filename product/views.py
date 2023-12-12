from django.shortcuts import redirect, render, HttpResponse
from .models import Product

# Create your views here.

def show_products_details(request):
    all_products = Product.objects.all()
    return render(request, "showProducts.html", {'all_products': all_products})
