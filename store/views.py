from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.views import _cart_id
from store.models import Product
from hateykhori.models import Category
from cart.models import Cart, CartItem

# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
        
    else:
    
        products = Product.objects.all().filter(
            is_available=True).order_by('-created_date')
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product=single_product).exists()
        # return HttpResponse(in_cart)
        # exit()
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    
    return render(request, 'product_detail.html', context)