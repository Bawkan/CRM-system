from django.db import models
from potclient.models import PotClientModel
from contracts.models import ContractModel

class ActClientModel(models.Model):
    data_pot_client = models.ForeignKey(PotClientModel, on_delete=models.CASCADE, related_name="actclient")
    data_contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE, related_name="dcontract")

