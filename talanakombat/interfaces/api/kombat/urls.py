from django.urls import path
from talanakombat.interfaces.api.kombat import views

app_name = "kombat_api"


urlpatterns = [
    path(
        "api/v1/kombat/",
        views.Kombat.as_view(),
        name="kombat",
    ),
]
