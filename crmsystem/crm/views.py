from django.shortcuts import render,reverse
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


def base_list(request):
    return render(request, 'crm/base.html')


def index_list(request):
    return render(request, "crm/index.html")


class LogoutView(LogoutView):
    next_page = "/"