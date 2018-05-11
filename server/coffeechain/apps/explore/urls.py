from django.urls import path

from coffeechain.apps.explore.api import views

urlpatterns = [
    path("state/<slug:addr>/", views.AddressView.as_view()),
    path("state/<slug:addr>/<slug:as_type>/", views.AddressView.as_view())
]
