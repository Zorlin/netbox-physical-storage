from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import StorageDeviceSerializer, StorageBaySerializer

class StorageDeviceViewSet(NetBoxModelViewSet):
    queryset = models.StorageDevice.objects.prefetch_related('tags')
    serializer_class = StorageDeviceSerializer

class StorageBayViewSet(NetBoxModelViewSet):
    queryset = models.StorageBay.objects.prefetch_related('tags')
    serializer_class = StorageBaySerializer
