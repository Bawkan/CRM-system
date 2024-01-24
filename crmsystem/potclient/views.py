from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import PotClientModel


class PotClientListView(ListView):
    model = PotClientModel
    context_object_name = "leads"


class PotClientDetailView(DetailView):
    model = PotClientModel


class PotClientCreateView(CreateView):
    model = PotClientModel
    fields = "last_name", "first_name", "phone", "email", "adv_company"

    def get_success_url(self):
        return reverse("potc:list")


class PotClientUpdateView(UpdateView):
    model = PotClientModel
    fields = "last_name", "first_name", "phone", "email", "adv_company"
    template_name = "potclient/leads-edit.html"

    def get_success_url(self):
        return reverse("potc:list")


class PotClientDeleteView(DeleteView):
    model = PotClientModel

    def get_success_url(self):
        return reverse("potc:list")
