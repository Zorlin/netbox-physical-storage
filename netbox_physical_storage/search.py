from netbox.search import SearchIndex, register_search
from .models import StorageDevice

@register_search

class StorageDeviceIndex(SearchIndex):
    model = StorageDevice
    fields = (
        ('name', 100),
        ('storage_device_type', 50),
        ('serial_number', 50),
        ('comments', 50),
    )
