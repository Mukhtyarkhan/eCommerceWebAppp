from django import forms
from .models import Store,Products

class StoreRequestForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description']
        
        



class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_desc', 'product_price', 'product_image']

