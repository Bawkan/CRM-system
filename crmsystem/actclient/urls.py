from django.urls import path
from .views import (ActiveListView,
                    ActiveDetailView,
                    ActiveCreateView,
                    ActiveDeleteView,
                    ActiveUpdateView,)


app_name = "act"


urlpatterns = [
    path("list/", ActiveListView.as_view(), name="list"),
    path("detail/<int:pk>/", ActiveDetailView.as_view(), name="detail"),
    path("create/", ActiveCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", ActiveDeleteView.as_view(), name="delete"),
    path("update/<int:pk>", ActiveUpdateView.as_view(), name="update")
]
