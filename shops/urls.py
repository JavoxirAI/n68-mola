from django.urls import path

from shops.views import cart_view, category_view, checkout_view, product_view, wishlist_view

app_name = "shops"

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('category/', category_view, name='category'),
    path('checkout/', checkout_view, name='checkout'),
    path('product/', product_view, name='product'),
    path('wishlist/', wishlist_view, name='wishlist'),
]