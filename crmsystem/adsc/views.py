from django.shortcuts import reverse, render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import AdvertCompany


class AdvertListView(ListView):
    model = AdvertCompany
    context_object_name = "ads"


def static(request):
    return render(request, "adsc/ads-statistic.html")


class AdvertDetailView(DetailView):
    model = AdvertCompany


class AdvertUpdateView(UpdateView):
    model = AdvertCompany
    fields = "name", "service_advert", "promotion_channel", "budget"

    def get_success_url(self):
        return reverse("ads:list")


class AdvertCreateView(CreateView):
    template_name = "adsc/advertcompany_create_form.html"
    model = AdvertCompany
    fields = "name", "service_advert", "promotion_channel", "budget"

    def get_success_url(self):
        return reverse("ads:list")


class AdvertDeleteView(DeleteView):
    model = AdvertCompany

    def get_success_url(self):
        return reverse("ads:list")
