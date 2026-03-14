from django.urls import path
from .views import *
urlpatterns = [
    path("", cart_detail, name="cart_detail"),
    path("add/", add_cart, name="add_cart"),
    path("delete/", delete_cart, name="delete_cart"),
    path("update/", update_cart, name="update_cart"),
]
