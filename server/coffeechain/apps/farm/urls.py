from django.urls import path, include

from coffeechain.apps.farm.api import views

urlpatterns = [
    path("create/", views.CreateFarmView.as_view()),
    path("<slug:key>/", include([
        path("add-cert/", views.AddCertView.as_view())
    ]))
]
