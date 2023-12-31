from netbox.views import generic
from . import filtersets, forms, models, tables
from utilities.views import ViewTab, register_model_view
from dcim.models import Device

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

# Main Storage Bay Views
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