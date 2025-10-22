from django.contrib import admin
from django.urls import include, path


api = [
    path("api/v1/", include("apps.expenses.urls")),
]

urlpatterns = [path("admin/", admin.site.urls), *api]
