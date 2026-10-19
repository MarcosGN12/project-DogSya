from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def cart_detail(request):
    return render(request, 'products/cart.html')

def add_to_cart(request, product_id):
    # Cart logic will be implemented in the next phase
    return redirect('products:cart')