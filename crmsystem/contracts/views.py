from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import ContractModel


class ContractView(ListView):
    model = ContractModel
    context_object_name = "contracts"


class ContractDetailView(DetailView):
    model = ContractModel


class ContrarctCreatView(CreateView):
    model = ContractModel
    fields = "name", "service", "file", "start_date", "end_date", "price"

    def get_success_url(self):
        return reverse("contract:list")


class ContractDeleteView(DeleteView):
    model = ContractModel

    def get_success_url(self):
        return reverse("contract:list")


class ContractUpdateView(UpdateView):
    model = ContractModel
    fields = "name", "service", "file", "start_date", "end_date", "price"

    def get_success_url(self):
        return reverse("contract:list")