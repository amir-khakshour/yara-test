from rest_framework import routers
from misc_api.views import PurchaseItemsAPIViewSet

router = routers.DefaultRouter()
router.register('misc_api', PurchaseItemsAPIViewSet, base_name="misc-api")


urlpatterns = router.urls
