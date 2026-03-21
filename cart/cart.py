from home.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        # Get image URL safely
        image_url = getattr(product.image, 'url', '')

        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'image': image_url,
                'quantity': quantity,
            }
        else:
            self.cart[product_id]['quantity'] += quantity

        self.session.modified = True

    def update_quantity(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            if self.cart[product_id]['quantity'] <= 0:
                del self.cart[product_id]
            self.session.modified = True
    
    def total(self):
        product_ids = self.cart.keys()
        quantities = self.cart
        products = Product.objects.filter(id__in=product_ids)

        total = 0

        for product in products:
            quantity = self.cart[str(product.id)]["quantity"]
            total += product.price * quantity

        return total


    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_items = []

        for product in products:
            session_item = self.cart.get(str(product.id), {})
            price = float(session_item.get('price', product.price))
            quantity = session_item.get('quantity', 1)
            cart_items.append({
                'id': product.id,
                'name': session_item.get('name', product.name),
                'price': price,
                'quantity': quantity,
                'image': session_item.get('image', ''),
                'total': price * quantity,
                'product_obj': product,
            })
        return cart_items

    def __len__(self):
        # total quantity of all items
        return sum(item.get('quantity', 0) for item in self.cart.values())