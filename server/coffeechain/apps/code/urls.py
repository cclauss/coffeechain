from django.urls import path, include

from coffeechain.common.rest_api.views import block_data_view
from coffeechain.proto.coffee_pb2 import Code
from .api import views

urlpatterns = [
    path("mint/", views.MintCodes.as_view(), name="mint-codes"),
    path("activate/", views.ActivateCodesView.as_view(), name="activate-codes"),
    path("<slug:key>/", include([
        path("", views.GetCode.as_view(), name="get-code"),
        path("block-data/", block_data_view(Code)),
    ]))
]
