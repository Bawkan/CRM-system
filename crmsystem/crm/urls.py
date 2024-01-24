from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import base_list, index_list

app_name = "crm"


urlpatterns = [
    path("login/",
         LoginView.as_view(template_name="crm/login.html"),
         name="login"),
    path('', base_list, name='base'),
    path("index/", index_list, name="index"),
    path("logout/", LogoutView.as_view(), name="logout")
]
