from rest_framework import permissions, viewsets

from misc_api.models import UserPurchaseHistory
from misc_api.utils import JokingThrottling
from misc_api.serializers import UserPurchaseHistorySerializer


class PurchaseItemsAPIViewSet(viewsets.ModelViewSet):
    """
    Misc API view Set
    """
    throttle_classes = (JokingThrottling,)  # Custom Throttling Class
    queryset = UserPurchaseHistory.objects.all()
    serializer_class = UserPurchaseHistorySerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )
