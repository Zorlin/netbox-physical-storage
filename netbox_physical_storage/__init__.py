from extras.plugins import PluginConfig

class NetBoxPhysicalStorageConfig(PluginConfig):
    name = 'netbox_physical_storage'
    verbose_name = ' NetBox Physical Storage'
    description = 'Manage physical storage interfaces and devices in NetBox.'
    version = '0.0.1'
    base_url = 'physical-storage'

config = NetBoxPhysicalStorageConfig