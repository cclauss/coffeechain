from django.urls import path
from .api import views

urlpatterns = [
    path("mint/", views.MintCodes.as_view(), name="mint-codes"),
    path("get/<slug:message>/", views.GetCode.as_view(), name="get-code")
]
