from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages

def home(request):
    products=Product.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',{"products":products,"categories": categories})

def product(request,pk):
    product=Product.objects.get(id=pk)
    categories = Category.objects.all()
    return render(request,'product.html',{"product": product,
        "categories": categories})

def category(request, category_id):
    try:
        selected_category = Category.objects.get(id=category_id)
        products_in_category = Product.objects.filter(category=selected_category)
        categories = Category.objects.all()  # for navbar
        return render(request, 'category.html', {
            'products': products_in_category,
            'category': selected_category,
            'categories': categories
        })
    except Category.DoesNotExist:
        messages.success(request, "That category doesn't exist!")
        return redirect('home')
def about(request):
    categories = Category.objects.all()
    return render(request, 'about.html',{'categories':categories})