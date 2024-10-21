from django.shortcuts import render, redirect
from seller.models import Products
from auth_app.models import Profile
from .models import Cart, Order, OrderItem #Address
from django.contrib import messages
from django.conf import settings
import stripe   # type: ignore






def cart(request):
    items=Cart.objects.filter(buyer=request.user)
    total=sum(item.get_total() for item in items)
    data={'items':items,
          'total': total}
    return render(request, 'cart.html', data)


def add_to_cart(request, id):
    if request.user.is_authenticated:
        try:
            product = Products.objects.get(id=id)
            
            profile = Profile.objects.get(user=request.user)
            
            if profile.is_buyer:
                if product.stock == 0:  
                    messages.error(request, 'Sorry, this product is out of stock!')
                    return redirect('home')
                
                cart, created = Cart.objects.get_or_create(
                    buyer=request.user,
                    product=product,
                )
                
                if not created:
                    cart.quantity += 1
                    cart.save()
                
                messages.success(request, 'Product added to cart!')
                return redirect('cart')
            else:
                messages.error(request, 'Only buyers can add products to the cart.')
                return redirect('home')
                
        except:
            pass 
            
    messages.warning(request, 'Please login to add items to cart.')
    return redirect('login')


def edit_cart(request, id):
    item = Cart.objects.get(id=id)
    action= request.POST.get('action')
    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease':
        if item.quantity >1:
            item.quantity -= 1
        else:
            item.delete()
            return redirect('cart')
    item.save()
    return redirect('cart')



def remove_from_cart(request, id):
    item = Cart.objects.get(buyer=request.user, id=id)
    item.delete()
    return redirect('cart')


def new_order(user, total, charge):
    return Order.objects.create(
        buyer=user,
        total_amount=total,
        payment_id=charge,
        status='completed'
        
        )


def checkout(request):
    items = Cart.objects.filter(buyer=request.user)
    total = sum(item.get_total() for item in items)
    
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=int(total * 100),
            currency="usd",
            source='tok_visa'
        )

        if charge.status == 'succeeded':
            order=new_order(request.user, total, charge)

            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price
                )


                def update_stock(item):
                    return Products.objects.filter(id=item.product.id).update(
                         stock=item.product.stock - item.quantity,
                         sales_count=item.product.sales_count + item.quantity
                    )
                    
                    
                update_stock(item)       
                      
            items.delete()

            messages.success(request, "Order completed successfully!")
            return redirect('order_history')

    data = {
        'items': items,
        'total': total
    }
    return render(request, 'checkout.html', data)


def order_history(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at').prefetch_related('orderitem_set__product')
    for order in orders:
        for item in order.orderitem_set.all():
            item.total = item.price * item.quantity

    return render(request, 'history.html', {'orders': orders})


