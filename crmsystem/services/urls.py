from django.urls import path
from .views import (ProductCreate,
                    ProductDelete,
                    ProductDetail,
                    ProductUpdate,
                    ProductsListView,)


app_name = "product"


urlpatterns = [
    path("create/", ProductCreate.as_view(), name="create"),
    path("list/", ProductsListView.as_view(), name="list"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("delete/<int:pk>", ProductDelete.as_view(), name="delete"),
    path("edit/<int:pk>/", ProductUpdate.as_view(), name="edit"),
]