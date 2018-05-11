from django.urls import path, include

from coffeechain.apps.shipment.api import views
from coffeechain.common.rest_api.views import block_data_view
from coffeechain.proto.coffee_pb2 import Shipment

urlpatterns = [
    path("create/", views.ShipmentCreateView.as_view()),
    path("<slug:key>/", include([
        path("", views.ShipmentGetView.as_view()),
        path("block-data/", block_data_view(Shipment)),
    ]))
]
