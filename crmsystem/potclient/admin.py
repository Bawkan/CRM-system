from django.contrib import admin
from .models import PotClientModel


@admin.register(PotClientModel)
class CompanyAdmin(admin.ModelAdmin):
    list_display = "last_name", "first_name", "phone", "email", "adv_company"
