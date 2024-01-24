from django.db import models
from adsc.models import AdvertCompany

class PotClientModel(models.Model):
    last_name = models.CharField(max_length=150, verbose_name="ф.и.о.")
    first_name = models.CharField(max_length=150, verbose_name="ф.и.о.")
    phone = models.IntegerField(null=True, blank=True, verbose_name='номер телефона')
    email = models.EmailField(blank=True, null=True, verbose_name='имейл')
    adv_company = models.ForeignKey(AdvertCompany, on_delete=models.CASCADE, related_name="company")

    def __str__(self):
        return f"{self.last_name}"

