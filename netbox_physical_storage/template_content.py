# template_content.py
from extras.plugins import PluginTemplateExtension

from .models import StorageDevice

class StorageDeviceCount(PluginTemplateExtension):
    """Template extension to display drive count on the right side of the page."""

    model = 'dcim.site'

    def right_page(self):
        # Query the StorageDevice model to get the current count of storage devices
        storage_device_count = StorageDevice.objects.count()

        return self.render('netbox_physical_storage/storagedevice_count.html', extra_context={
            'storage_device_count': storage_device_count
        })

class StorageBayTab(PluginTemplateExtension):
    """Template extension to add a Storage Bays tab to Devices."""

    # TODO: In future we may make it possible to decide if you want a tab or a section
    # If you select tab, this will show up in Devices as a tab, otherwise it shows up as a fullpage section
    # in the same.

    model = 'dcim.devices'
    
    def tabs(self):
        # This method is used to add a new tab.
        # 'storage-bays' is the identifier for the tab, and the URL parameter that will activate it.
        # 'Storage Bays' is the display name of the tab.
        # The template 'my_plugin/storage_bays_tab.html' is where you define the HTML content of the tab.
        return {
            'storage-bays': (
                'Storage Bays',  # Display name
                self.render('netbox_physical_storage/storagebays_tab.html')  # Path to your template
            )
        }

class StorageBaySection(PluginTemplateExtension):
    """Template extension to add a Storage Bays section to Devices."""
    
    model = 'dcim.device'

    def full_width_page(self):
        device = self.context["object"]

        return self.render('netbox_physical_storage/storagebays_section.html', extra_context={ 'device': device })

template_extensions = [StorageDeviceCount, StorageBayTab, StorageBaySection]
