from netbox.filtersets import NetBoxModelFilterSet
from .models import StorageDevice, StorageBay, StorageManufacturer, StorageDeviceType

class StorageDeviceTypeFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageDeviceType
        fields = ('name', 'manufacturer', 'protocol', 'model_number', 'part_number', 'size')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class StorageManufacturerFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = StorageManufacturer
        fields = ('name', 'slug', 'description')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class StorageBayFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageBay
        fields = ('device', 'name', 'form_factor', 'hot_swap_capability', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class StorageDeviceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageDevice
        fields = ('name', 'storage_device_model', 'serial_number', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
