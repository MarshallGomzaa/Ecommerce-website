from django.db import models
import datetime



from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField( max_length=100)
    password = models.CharField( max_length=50)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category =  models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products', height_field=None, width_field=None, max_length=None)

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name




class Order(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity =  models.IntegerField(default=1)
    address = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        # safe string representation
        return f"Order #{self.id} - {self.product.name}"