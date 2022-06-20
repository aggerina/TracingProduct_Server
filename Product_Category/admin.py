from django.contrib import admin
from .models import  Products_category

class productCateury(admin.ModelAdmin):
    list_display = ['__str__', 'name']
    class Meta:
        model = Products_category
admin.site.register(Products_category, productCateury)
# Register your models here.
