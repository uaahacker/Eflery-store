from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category_c(models.Model):
    cate = models.CharField(max_length=100, null=True)
    
    
    def __str__(self) -> str:
        return self.cate



class Products(models.Model):
    Category = (
    ('Fashion', 'Fashion'),
    ('Electronics' , 'Electronics'),
    ('Food','Food'),
    ('Cosmatics','Cosmatics'),
)
    
    product_name = models.CharField(max_length=100, null=True)
    product_description = models.TextField(max_length=600, null=True)
    product_price = models.FloatField(max_length=30, null=True)
    cats = models.ManyToManyField(Category_c)
    category = models.CharField(max_length=200, null=True, choices=Category)
    product_images = models.ImageField(upload_to='dbfl',null=True)  
    
    def __str__(self) -> str:
        return self.product_name
    

    
#   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
# profile_image = models.ImageField(upload_to='profile')


    
class order(models.Model):
    stat = (
    ('Pending', 'Pending'),
    ('Out for delivery' , 'Out for delivery'),
    ('Delivered','Delivered'),
)
    usr_cos = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    prod = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, choices=stat, default='pending')
    
    def __str__(self) -> str:
        return self.status
    
class carte(models.Model):
    usr_cos = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,related_name='carts')
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL ,related_name='carts')
    time_created = models.DateTimeField(auto_now_add=True, null=True)