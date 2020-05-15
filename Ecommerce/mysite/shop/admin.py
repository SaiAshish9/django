from django.contrib import admin

from .models import Product,Order

# Register your models here.

admin.site.site_header="E-commerce"
admin.site.site_title="Amazon"
admin.site.index_title="Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):

   def change_category_to_default(self, request,queryset):
       queryset.update(categories="default")

   change_category_to_default.short_description ='Default'

   list_display =('title','price','discount_price','categories','image','description')  
   search_fields=['title','categories']
   actions= ['change_category_to_default']
   fields=['title','price']
   list_editable=['price','categories']

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)