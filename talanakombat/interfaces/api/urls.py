from django.urls import include, path

urlpatterns = [
    path("", include("talanakombat.interfaces.api.kombat.urls")),
]
