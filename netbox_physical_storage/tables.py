import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StorageDevice, StorageBay, StorageManufacturer, StorageDeviceType

class StorageManufacturerTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = StorageManufacturer
        fields = ('pk', 'id', 'name', 'slug', 'description')
        default_columns = ('name', 'slug', 'description')

class StorageDeviceTypeTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    manufacturer = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = StorageDeviceType
        fields = ('pk', 'id', 'name', 'manufacturer', 'protocol', 'form_factor', 'model_number', 'part_number', 'size', 'comments')
        default_columns = ('name', 'manufacturer', 'protocol', 'form_factor', 'model_number', 'size')

class StorageBayTable(NetBoxTable):
# Contains device, name, form_factor, hot_swap_capability, and any comments
    name = tables.Column(
        linkify=True
    )

    device = tables.Column(
        linkify=True
    )

    form_factor = ChoiceFieldColumn()

    hot_swap_capability = tables.BooleanColumn()

    class Meta(NetBoxTable.Meta):
        model = StorageBay
        fields = ('pk', 'id', 'device', 'name', 'form_factor', 'hot_swap_capability', 'comments')
        default_columns = ('device', 'name', 'form_factor', 'hot_swap_capability')

class StorageDeviceTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    # Fetch device name from the associated Device model
    device = tables.Column(
        accessor='device'
    )

    # Fetch protocol and form factor from the associated DeviceType model
    protocol = tables.Column(
        accessor='protocol'
    )

    class Meta(NetBoxTable.Meta):
        model = StorageDevice
        fields = ('pk', 'id', 'name', 'protocol', 'storage_device_model', 'serial_number', 'comments')
        default_columns = ('name', 'protocol', 'device', 'storage_device_model', 'serial_number')
