from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import StorageDeviceSerializer

class StorageDeviceViewSet(NetBoxModelViewSet):
    queryset = models.StorageDevice.objects.prefetch_related('tags')
    serializer_class = StorageDeviceSerializer
