from django.db import models
from seller.models import Products
from django.contrib.auth.models import User

class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_total(self):
        return self.product.product_price * self.quantity


    
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Products, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)