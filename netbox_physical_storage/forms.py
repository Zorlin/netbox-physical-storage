from .models import StorageDevice, StorageDeviceTypeChoices
from utilities.forms.fields import CommentField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

class StorageDeviceFilterForm(NetBoxModelFilterSetForm):
    model = StorageDevice

    # TODO We're using Django's ModelMultipleChoiceField class for this field instead of NetBox's DynamicModelChoiceField because the latter requires a functional REST API endpoint for the model. Once we implement a REST API in step nine, you're free to revisit this form and change access_list to a DynamicModelChoiceField.
    storage_device = forms.ModelMultipleChoiceField(
        queryset=StorageDevice.objects.all(),
        required=False
    )

    storage_device_type = forms.MultipleChoiceField(
        choices=StorageDeviceTypeChoices,
        required=False
    )

class StorageDeviceForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = StorageDevice
        fields = ('name', 'storage_device_type', 'serial_number', 'comments')
