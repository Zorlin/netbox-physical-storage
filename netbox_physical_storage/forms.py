from netbox.forms import NetBoxModelForm
from .models import StorageDevice
from utilities.forms.fields import CommentField

class StorageDeviceForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = StorageDevice
        fields = ('name', 'storage_device_type', 'serial_number', 'mount_point', 'comments')