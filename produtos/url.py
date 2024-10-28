from django.urls import path
from . import views

urlpatterns = [
    path("", views.produtos, name="produtos"),
    path("card", views.card, name="card")
]
