import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StorageDevice, StorageBay

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
    storage_device_type = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = StorageDevice
        fields = ('pk', 'id', 'name', 'storage_device_type', 'serial_number', 'comments')
        default_columns = ('name', 'storage_device_type', 'serial_number')
