from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Seller who owns the store
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_approved = models.BooleanField(null=True, default=None)  # Approval status by admin
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    



class Products(models.Model):
    product_name = models.CharField(max_length=500)
    product_desc = models.TextField()
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/',null=True,blank=True,default=None)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    stock = models.IntegerField(default=0)
    sales_count = models.IntegerField(default=0)  
    
    
    
    



