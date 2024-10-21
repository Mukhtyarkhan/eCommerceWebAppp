# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('store-request/', views.create_store_request, name='store_request'),
    path('profile/', views.seller_profile, name='seller_profile'),
    path('manage_store/', views.manage_store, name='manage_store'),
    path('add_new_product/', views.add_new_product, name="add_new_product"),
    path("update_product/<int:id>/", views.update_product, name="update_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
    path('update_stock/<int:id>/', views.update_stock, name='update_stock'),
]