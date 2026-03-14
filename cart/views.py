from django.shortcuts import render, get_object_or_404, redirect
from home.models import Category, Product
from .cart import Cart
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def cart_detail(request):
    categories = Category.objects.all()
    cart = Cart(request)
    cart_products = cart.get_products()
    totals = cart.total()
    return render(request, 'cart_detail.html', {
        'categories': categories,
        'cart_products': cart_products,
        'totals': totals,
    })

def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        return JsonResponse({'quantity': len(cart)})
def delete_cart(request): 
    return redirect(request,'cart_detail')
@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        product_id = int(request.POST.get('product_id'))
        cart = Cart(request)

        current_quantity = cart.cart.get(str(product_id), {}).get('quantity', 1)
        if action == 'increase':
            cart.update_quantity(product_id, current_quantity + 1)
        elif action == 'decrease':
            cart.update_quantity(product_id, current_quantity - 1)

    return redirect('cart_detail')