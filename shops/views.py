from django.shortcuts import render

def cart_view(request):
    return render(request, 'shop/cart.html')

def category_view(request):
    return render(request, 'shop/category.html')

def checkout_view(request):
    return render(request, 'shop/checkout.html')

def product_view(request):
    return render(request, 'shop/product-detail.html')

def wishlist_view(request):
    return render(request, 'shop/wishlist.html')