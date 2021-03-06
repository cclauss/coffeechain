"""coffeechain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('codes/', include('coffeechain.apps.code.urls')),
        path('certs/', include('coffeechain.apps.cert.urls')),
        path('farms/', include('coffeechain.apps.farm.urls')),
        path('harvests/', include('coffeechain.apps.harvest.urls')),
        path('shipments/', include('coffeechain.apps.shipment.urls')),
        path('roasts/', include('coffeechain.apps.roast.urls')),
        path('explore/', include('coffeechain.apps.explore.urls')),
    ]))
]
