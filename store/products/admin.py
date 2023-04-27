from django.contrib import admin

from products.models import ProductCategory, Product, Basket


#admin.site.register(Product)
#admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','quantity', 'price',)
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category', )
    ordering = ('name', )



class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity','creative_timestamp')
    extra = 0
    readonly_fields = ('creative_timestamp', )