from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    path("api/suggestions/", views.suggestions, name="suggestions"),
    path("api/connections/", views.api_connections, name="api_connections"),
]