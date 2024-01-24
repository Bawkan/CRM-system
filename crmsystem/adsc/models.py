from django.db import models
from services.models import ServicesModel

class AdvertCompany(models.Model):
    name = models.CharField(max_length=200, verbose_name="название компании")
    service_advert = models.ForeignKey(ServicesModel,
                                          on_delete=models.CASCADE,
                                          related_name="product")
    promotion_channel = models.CharField(max_length=500, verbose_name="канал продвижения")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="бюджет на рекламу")

    def __str__(self):
        return f"{self.name}"

