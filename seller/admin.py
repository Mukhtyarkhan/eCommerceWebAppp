from django.contrib import admin
from .models import Store,Products

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'seller', 'is_approved', 'created_at', 'description']
    list_filter = ['is_approved', 'created_at']
    actions = ['approve_store', 'deny_store']

    def approve_store(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "store have been approved.")
    
    def deny_store(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, "store have been denied.")
    
    approve_store.short_description = "Approve store"
    deny_store.short_description = "Deny store"

admin.site.register(Store, StoreAdmin)
admin.site.register(Products)
 
 
# class ManageProduct(admin.ModelAdmin):
#     list_display = ['product_name', 'product_price', 'product_desc', 'product_image']
#     search_fields = ['product_name', 'product_desc']
#     actions = ["delete_selected", "update_product"]
    
     

# admin.site.register(Products, ManageProduct)
         