from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('product/<int:pk>/', product, name='product'),
    path('category/<int:category_id>/', category, name='category'),

]
