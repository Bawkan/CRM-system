from django.contrib import admin
from .models import ServicesModel


@admin.register(ServicesModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = "name", "description", "price"





