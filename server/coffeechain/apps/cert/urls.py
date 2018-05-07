from rest_framework.routers import SimpleRouter

from coffeechain.apps.cert.api import CertView

router = SimpleRouter()
router.register('cert', CertView)

urlpatterns = []  # manual urls
urlpatterns += router.urls
