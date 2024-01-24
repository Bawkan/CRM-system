from django.urls import path
from .views import (AdvertListView,
                    AdvertDetailView,
                    AdvertUpdateView,
                    AdvertCreateView,
                    AdvertDeleteView,
                    static,)

app_name="ads"


urlpatterns = [
    path("static/", static, name="static"),
    path("list/", AdvertListView.as_view(), name="list"),
    path("create/", AdvertCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", AdvertDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", AdvertDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", AdvertUpdateView.as_view(), name="edit"),

]
