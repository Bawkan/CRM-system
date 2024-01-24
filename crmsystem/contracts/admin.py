from django.contrib import admin
from .models import ContractModel


@admin.register((ContractModel))
class ContractAdmin(admin.ModelAdmin):
    list_display = "name", "service", "file", "start_date", "end_date", "price"
