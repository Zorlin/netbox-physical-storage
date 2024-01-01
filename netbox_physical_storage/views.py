from netbox.views import generic
from . import filtersets, forms, models, tables
from utilities.views import ViewTab, register_model_view
from dcim.models import Device

# Storage Device Type views
class StorageDeviceTypeView(generic.ObjectView):
    queryset = models.StorageDeviceType.objects.all()
    table = tables.StorageDeviceTypeTable

class StorageDeviceTypeEditView(generic.ObjectEditView):
    queryset = models.StorageDeviceType.objects.all()
    form = forms.StorageDeviceTypeForm

class StorageDeviceTypeDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageDeviceType.objects.all()

class StorageDeviceTypeListView(generic.ObjectListView):
    queryset = models.StorageDeviceType.objects.all()
    table = tables.StorageDeviceTypeTable
    filterset = filtersets.StorageDeviceTypeFilterSet
    filterset_form = forms.StorageDeviceTypeFilterForm

# Storage Manufacturer views
class StorageManufacturerView(generic.ObjectView):
    queryset = models.StorageManufacturer.objects.all()
    table = tables.StorageManufacturerTable

class StorageManufacturerEditView(generic.ObjectEditView):
    queryset = models.StorageManufacturer.objects.all()
    form = forms.StorageManufacturerForm

class StorageManufacturerDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageManufacturer.objects.all()

class StorageManufacturerListView(generic.ObjectListView):
    queryset = models.StorageManufacturer.objects.all()
    table = tables.StorageManufacturerTable
    filterset = filtersets.StorageManufacturerFilterSet
    filterset_form = forms.StorageManufacturerFilterForm

# Storage Bay views
class StorageBayView(generic.ObjectView):
    queryset = models.StorageBay.objects.all()
    table = tables.StorageBayTable

class StorageBayEditView(generic.ObjectEditView):
    queryset = models.StorageBay.objects.all()
    form = forms.StorageBayForm

class StorageBayDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageBay.objects.all()

class StorageBayListView(generic.ObjectListView):
    queryset = models.StorageBay.objects.all()
    table = tables.StorageBayTable
    filterset = filtersets.StorageBayFilterSet
    filterset_form = forms.StorageBayFilterForm

# Display tabs in Devices for Storage Bays
@register_model_view(Device, name='Storage Bays')
class StorageBaysTabView(generic.ObjectView):
    queryset = Device.objects.all()

    tab = ViewTab(
        label='Storage Bays',
        hide_if_empty=False,
    )
    template_name = "netbox_physical_storage/storagebays_tab.html"

class StorageDeviceView(generic.ObjectView):
    queryset = models.StorageDevice.objects.all()

class StorageDeviceEditView(generic.ObjectEditView):
    queryset = models.StorageDevice.objects.all()
    form = forms.StorageDeviceForm

class StorageDeviceDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageDevice.objects.all()

class StorageDeviceListView(generic.ObjectListView):
    queryset = models.StorageDevice.objects.all()
    table = tables.StorageDeviceTable
    filterset = filtersets.StorageDeviceFilterSet
    filterset_form = forms.StorageDeviceFilterForm