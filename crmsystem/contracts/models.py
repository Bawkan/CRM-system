from django.db import models


class ContractModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    service = models.TextField(max_length=2500, verbose_name="предоставление услуги")
    file = models.FileField(upload_to="file", verbose_name="файл с документом")
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата:")
    start_date = models.DateTimeField(verbose_name="с:")
    end_date = models.DateTimeField(verbose_name="до:")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма")

    def __str__(self):
        return f"{self.name}"