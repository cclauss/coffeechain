from django.urls import include, path

from coffeechain.apps.roast.api import views

urlpatterns = [
    path("create/", views.RoastCreateView.as_view()),
    path("<slug:key>/", include([
        path("", views.RoastGetView.as_view()),
        path("add-harvest/", views.RoastAddHarvestView.as_view()),
        path("block-data/", views.BlockChainDataView.as_view())
    ]))
]
