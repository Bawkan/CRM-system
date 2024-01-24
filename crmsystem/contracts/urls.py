from django.urls import path
from .views import (ContractView,
                    ContractDetailView,
                    ContrarctCreatView,
                    ContractDeleteView,
                    ContractUpdateView,)

app_name = "contract"


urlpatterns = [
    path("list/", ContractView.as_view(), name="list"),
    path("detail/<int:pk>/", ContractDetailView.as_view(), name="detail"),
    path("create/", ContrarctCreatView.as_view(), name="create"),
    path("deelete/<int:pk>/", ContractDeleteView.as_view(), name="delete"),
    path("edit/<int:pk>/", ContractUpdateView.as_view(), name="edit")
]
