from .models import StorageDevice, StorageDeviceTypeChoices, StorageBay
from utilities.forms.fields import CommentField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from dcim.models import Device

class StorageBayFilterForm(NetBoxModelFilterSetForm):
    model = StorageBay

    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='Device'
    )

    form_factor = forms.MultipleChoiceField(
        choices=StorageDeviceTypeChoices,
        required=False
    )

class StorageBayForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = StorageBay
        fields = ('device', 'name', 'form_factor', 'hot_swap_capability', 'comments')

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
