from django.urls import path, include

from coffeechain.apps.harvest.api import views

urlpatterns = [
    path("create/", views.CreateHarvestView.as_view()),
    path("<slug:key>/", include([
        path("", views.GetHarvestView.as_view()),
        path("add-shipment/", views.AddShipmentView.as_view()),
        path("add-farm/", views.AddFarmView.as_view())
    ]))
]
