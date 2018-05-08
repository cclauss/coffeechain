from django.urls import path

from coffeechain.apps.cert.api import views

urlpatterns = [
    path("create/", views.CreateCertView.as_view()),
    path("<slug:key>/", views.GetCertView.as_view())
]
