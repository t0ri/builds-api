from rest_framework import routers
from .api import LotViewset

router = routers.DefaultRouter()
router.register('api/lots', LotViewset, 'lots')

urlpatterns = router.urls
