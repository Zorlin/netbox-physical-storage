import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StorageDevice

class StorageDeviceTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    storage_device_type = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = StorageDevice
        fields = ('pk', 'id', 'name', 'storage_device_type', 'serial_number', 'mount_point', 'comments')
        default_columns = ('name', 'storage_device_type')
