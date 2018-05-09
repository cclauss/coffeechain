from django.urls import path, include

from coffeechain.apps.harvest.api import views

urlpatterns = [
    path("create/", views.HarvestCreateView.as_view()),
    path("<slug:key>/", include([
        path("", views.HarvestGetView.as_view()),
        path("add-shipment/", views.HarvestAddShipmentView.as_view()),
        path("add-farm/", views.HarvestAddFarmView.as_view())
    ]))
]
