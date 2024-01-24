from django.db import models


class ServicesModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="название")
    description = models.TextField(max_length=1500, verbose_name="описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return f"{self.name}"