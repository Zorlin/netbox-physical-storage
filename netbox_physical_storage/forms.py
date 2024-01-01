from utilities.forms.fields import CommentField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from dcim.models import Device
from .models import StorageDevice, StorageBay, StorageManufacturer, StorageDeviceType

class StorageDeviceTypeFilterForm(NetBoxModelFilterSetForm):
    model = StorageDeviceType

    name = forms.CharField(
        required=False
    )

class StorageDeviceTypeForm(NetBoxModelForm):
    comments = CommentField()

    SIZE_UNITS = (
        ('GB', 'GB'),
        ('TB', 'TB'),
        ('PB', 'PB'),
    )
    size_unit = forms.ChoiceField(choices=SIZE_UNITS, required=True, label="Size unit")

    class Meta:
        model = StorageDeviceType
        fields = ('name', 'manufacturer', 'protocol', 'form_factor', 'model_number', 'size', 'size_unit', 'part_number', 'comments')

class StorageManufacturerFilterForm(NetBoxModelFilterSetForm):
    model = StorageManufacturer

    name = forms.CharField(
        required=False
    )

class StorageManufacturerForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = StorageManufacturer
        fields = ('name', 'slug', 'description', 'comments')

class StorageBayFilterForm(NetBoxModelFilterSetForm):
    model = StorageBay

    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='Device'
    )

    form_factor = forms.MultipleChoiceField(
        choices=StorageBay.form_factor_choices,
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

class StorageDeviceForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = StorageDevice
        fields = ('name', 'storage_device_model', 'storage_bay', 'serial_number', 'comments')
