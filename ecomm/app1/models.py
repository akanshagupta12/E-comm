from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    shortdescription = models.TextField()
    brand = models.CharField(max_length=50)
    description = models.TextField()
    mrp = models.IntegerField()
    csp = models.IntegerField(default=0.00)
    image = models.URLField(null=True , blank=True)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True)
    in_cart = models.BooleanField(default=False)
    in_warranty = models.IntegerField(default=0)
    @property
    def discount(self):
        return round(((self.mrp-self.csp)/(self.mrp))*100 , 2)

class Cart(models.Model):
    name = models.CharField(max_length=50)
    mrp = models.IntegerField(default=0.00)
    csp = models.IntegerField(default=0.00)
    quantity = models.IntegerField(default=1)
    image = models.URLField(null=True , blank=True)
    @property
    def subtotal(self):
        return self.csp*self.quantity

class Razorpay(models.Model):
    razorpay_order_id = models.CharField(max_length=30)
    razorpay_merchant_key =  models.CharField(max_length=50)
    razorpay_amount= models.IntegerField(default=0)
    currency =  models.CharField(max_length=50)
    callback_url = models.CharField(max_length=50)
