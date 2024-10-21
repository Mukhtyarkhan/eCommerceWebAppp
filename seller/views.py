from django.shortcuts import render, redirect
from .models import Store,Products
from .forms import StoreRequestForm,ProductsForm
from django.contrib.auth.decorators import login_required 

def auth(view_function):
    def login_re(request, *args, **kwargs):
        if request.user.is_authenticated==False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return login_re




@login_required
def create_store_request(request):
    if request.method == 'POST':
        form = StoreRequestForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.seller = request.user
            store.save()
            return redirect('seller_profile')  
    else:
        form = StoreRequestForm()

    return render(request, 'create_store_request.html', {'form': form})





@login_required
def seller_profile(request):
    store = Store.objects.get(seller=request.user)
    products = Products.objects.filter(store=store)
    
    # Calculate basic analytics
    total_products = products.count()
    total_stock = sum(product.stock for product in products)
    print(total_stock)
    low_stock_products = products.filter(stock__lte=5)
    out_of_stock = products.filter(stock=0)
    top_selling = products.order_by('-sales_count')[:5]
    
    data = {
        'store': store,
        'total_products': total_products,
        "total_stock": total_stock,
        'low_stock_products': low_stock_products,
        'out_of_stock': out_of_stock,
        'top_selling': top_selling,
    }
    return render(request, 'seller_profile.html', data)






@login_required
def manage_store(request):

    store = Store.objects.get(seller=request.user)
    products = Products.objects.filter(store=store)
    data = {
        "store": store,
        'products': products
        }
    return render(request, 'manage_store.html', data)
    
        


@login_required
def add_new_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = Store.objects.get(seller=request.user)
            product.save()
            return redirect('manage_store')
    else:
        form = ProductsForm()
    return render(request, 'add_new_product.html', {'form': form})




@login_required
def update_product(request, id):
    product=Products.objects.get(id=id)
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_store')
    else:
        form = ProductsForm(instance=product)
    return render(request, 'update_product.html', {'form': form,"product":product})


@login_required
def update_stock(request, id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        new_stock =int( request.POST.get('stock'))
        if new_stock >= 0:
            product.stock = new_stock
            product.save()
        return redirect('manage_store')
    return render(request, 'update_stock.html', {'product': product})   




@login_required
def delete_product(request,id):
    product=Products.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('manage_store')
        
    return render(request,'update_product.html',{'product':product})
    
    

