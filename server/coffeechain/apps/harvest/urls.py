from django.urls import path, include

from coffeechain.apps.harvest.api import views
from coffeechain.common.rest_api.views import block_data_view
from coffeechain.proto.coffee_pb2 import Harvest

urlpatterns = [
    path("create/", views.HarvestCreateView.as_view()),
    path("<slug:key>/", include([
        path("", views.HarvestGetView.as_view()),
        path("add-shipment/", views.HarvestAddShipmentView.as_view()),
        path("add-farm/", views.HarvestAddFarmView.as_view()),
        path("block-data/", block_data_view(Harvest)),
    ]))
]
