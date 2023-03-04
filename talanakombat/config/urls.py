"""talanakombat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="TALANA KOMBAT",
        default_version="v1",
        description="API TALANA KOMBAT",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="karina.vargasgonzalez@gmail.com"),
        license=openapi.License(name="Software"),
    ),
    public=True,
    permission_classes=[],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Interface API
    path("", include("talanakombat.interfaces.api.urls")),
    # Documentation
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
