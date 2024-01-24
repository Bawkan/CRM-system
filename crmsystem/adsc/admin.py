from django.contrib import admin
from .models import AdvertCompany


@admin.register(AdvertCompany)
class AdvertCompanyAdmin(admin.ModelAdmin):
    list_display = "name", "service_advert", "promotion_channel", "budget"
