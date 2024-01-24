from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import ServicesModel


class ProductCreate(CreateView):
    model = ServicesModel
    fields = "name", "description", "price"

    def get_success_url(self):
        return reverse("product:list")


class ProductDetail(DetailView):
    model = ServicesModel


class ProductUpdate(UpdateView):
    model = ServicesModel
    fields = "name", "description", "price"
    template_name_suffix = "_update_form"

    def get_success_url(self, **kwargs):
        return reverse("product:list")


class ProductDelete(DeleteView):
    model = ServicesModel
    def get_success_url(self):
        return reverse("product:list")


class ProductsListView(ListView):
    model = ServicesModel
    context_object_name = "products"
