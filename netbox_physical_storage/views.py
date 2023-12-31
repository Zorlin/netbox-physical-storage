from netbox.views import generic
from . import filtersets, forms, models, tables

class StorageDeviceView(generic.ObjectView):
    queryset = models.StorageDevice.objects.all()
    
class StorageDeviceListView(generic.ObjectListView):
    queryset = models.StorageDevice.objects.all()
    table = tables.StorageDeviceTable

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