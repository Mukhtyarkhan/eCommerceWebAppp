from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('edit_cart/<int:id>', views.edit_cart, name='edit_cart'),
    path('remove_from_cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    # path('payment_success/', views.payment_success, name='payment_success'),
    path('order_history/', views.order_history, name='order_history'),
    
]