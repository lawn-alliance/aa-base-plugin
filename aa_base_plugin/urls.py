"""Routes."""

# Django
from django.urls import path

from . import views

app_name = "aa_base_plugin"

urlpatterns = [
    path("", views.index, name="index"),
]
