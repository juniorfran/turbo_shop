from django.contrib import admin

# Register your models here.

from . models import Product

class ProductAdmin(admin.ModelAdmin):

    fields = ('titulo', 'descripcion', 'precio', 'image')
    list_display = ('__str__', 'slug', 'created_at')


admin.site.register(Product, ProductAdmin)