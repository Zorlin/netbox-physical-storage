from netbox.filtersets import NetBoxModelFilterSet
from .models import StorageDevice

class StorageDeviceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageDevice
        fields = ('name', 'storage_device_type', 'serial_number', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
