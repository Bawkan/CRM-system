from django.urls import path
from .views import (PotClientListView,
                    PotClientCreateView,
                    PotClientDetailView,
                    PotClientUpdateView,
                    PotClientDeleteView)


app_name = "potc"


urlpatterns = [
    path("list/", PotClientListView.as_view(), name="list"),
    path("create/", PotClientCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", PotClientDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", PotClientUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", PotClientDeleteView.as_view(), name="delete")

]
