from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from seller.models import Products,Store





def home(request):
    # stores=Store.objects.all()
    products=Products.objects.all()
    
    data={'products': products}
    return render(request, 'index.html', data)