from django.urls import path
from .api import views

urlpatterns = [
    path("mint/", views.MintCodes.as_view(), name="mint-codes"),
    path("activate/", views.ActivateCodesView.as_view(), name="activate-codes"),
    path("<slug:message>/", views.GetCode.as_view(), name="get-code")
]
