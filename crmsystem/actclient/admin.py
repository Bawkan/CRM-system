from django.contrib import admin
from .models import ActClientModel


@admin.register(ActClientModel)
class ActClientAdmin(admin.ModelAdmin):
    list_display = "data_pot_client", "data_contract"