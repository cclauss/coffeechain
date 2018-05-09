from django.urls import path, include

from coffeechain.apps.shipment.api import views

urlpatterns = [
    path("create/", views.ShipmentCreateView.as_view()),
    path("<slug:key>/", include([
        path("", views.ShipmentGetView.as_view())
    ]))
]
