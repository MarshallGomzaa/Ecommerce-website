from .cart import Cart

#creating context processors so that our cart work on all pages
def cart_quantity(request):
    cart = Cart(request)
    return {'cart_quantity': len(cart)}