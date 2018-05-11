from django.urls import include, path

from coffeechain.apps.roast.api import views
from coffeechain.common.rest_api.views import block_data_view
from coffeechain.proto.coffee_pb2 import Roast

urlpatterns = [
    path("create/", views.RoastCreateView.as_view()),
    path("<slug:key>/", include([
        path("", views.RoastGetView.as_view()),
        path("add-harvest/", views.RoastAddHarvestView.as_view()),
        path("block-data/", block_data_view(Roast))
    ]))
]
