from django.urls import path

from coffeechain.apps.farm.api import views

urlpatterns = [
    path("create/", views.CreateFarmView),
]
