from django.contrib import admin
from .models import Product, Image, Parameter

class ImageInline(admin.TabularInline):
    model = Image

class ParameterInline(admin.TabularInline):
    model = Parameter

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ParameterInline]
    list_display = ('name', 'base_price', 'sort_order')
    search_fields = ('name', 'description')

# Можно также зарегистрировать Image и Parameter, если нужно
admin.site.register(Image)
admin.site.register(Parameter)
