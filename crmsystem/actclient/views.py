from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ActClientModel


class ActiveListView(ListView):
    model = ActClientModel
    context_object_name = "customers"


class ActiveDetailView(DetailView):
    model = ActClientModel


class ActiveCreateView(CreateView):
    model = ActClientModel
    fields = "data_pot_client", "data_contract"

    def get_success_url(self):
        return reverse("act:list")


class ActiveDeleteView(DeleteView):
    model = ActClientModel

    def get_success_url(self):
        return reverse("act:list")


class ActiveUpdateView(UpdateView):
    model = ActClientModel
    fields = "data_pot_client", "data_contract"
    template_name = "actclient/customers-edit.html"

    def get_success_url(self):
        return reverse("act:list")
