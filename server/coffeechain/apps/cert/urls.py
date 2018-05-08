from django.urls import path

from coffeechain.apps.cert.api import views

urlpatterns = [
    path("create/", views.CreateCertSerializer),
    path("<slug:key>/", views.GetCertView)
]
