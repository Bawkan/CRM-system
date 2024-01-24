from services.models import ServicesModel
from adsc.models import AdvertCompany
from potclient.models import PotClientModel
from actclient.models import ActClientModel

def contents(request):
    context = {
        "products_count": ServicesModel.objects.count(),
        "advertisements_count": AdvertCompany.objects.count(),
        "leads_count": PotClientModel.objects.count(),
        "customers_count": ActClientModel.objects.count()
    }
    return context