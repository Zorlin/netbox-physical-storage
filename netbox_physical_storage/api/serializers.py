from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import StorageDevice, StorageBay

class StorageBaySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_physical_storage-api:storagebay-detail'
    )
    class Meta:
        model = StorageBay
        fields = [
            'id', 'url', 'name', 'device', 'form_factor', 'hot_swap_capability', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        ]

class StorageDeviceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_physical_storage-api:storagedevice-detail'
    )
    class Meta:
        model = StorageDevice
        fields = [
            'id', 'url', 'name', 'storage_device_type', 'serial_number', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        ]

# TODO: This entire class may be unnecessary, as I don't know that we need nested serializers for this plugin.
# 2023-12-31: Bye 2023! See you in a year...
class NestedStorageDeviceSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_physical_storage-api:storagedevice-detail'
    )

    class Meta:
        model = StorageDevice
        fields = ('id', 'url', 'display', 'name')
