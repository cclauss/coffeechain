from django.urls import path

from coffeechain.apps.harvest.api import views

urlpatterns = [
    path("create/", views.CreateHarvestView.as_view())
]
