from django.urls import path, include

from coffeechain.apps.farm.api import views
from coffeechain.common.rest_api.views import block_data_view
from coffeechain.proto.coffee_pb2 import Farm

urlpatterns = [
    path("create/", views.CreateFarmView.as_view()),
    path("<slug:key>/", include([
        path("", views.FarmGetView.as_view()),
        path("add-cert/", views.AddCertView.as_view()),
        path("block-data/", block_data_view(Farm)),
    ]))
]
