"""
Define the plugin menu buttons & the plugin navigation bar enteries.
"""

from django.conf import settings
from extras.plugins import PluginMenu, PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_settings = settings.PLUGINS_CONFIG["netbox_physical_storage"]

#
# Define storage device menu buttons
#
storagedevice_buttons = [
    PluginMenuButton(
        link='plugins:netbox_physical_storage:storagedevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    )
]

#
# Define the storage device menu
#
storagedevice_menu = (
    PluginMenuItem(
        link='plugins:netbox_physical_storage:storagedevice_list',
        link_text='Storage Devices',
        buttons=storagedevice_buttons,
    ),
)

#
# Define storage bay menu buttons
#
storagebay_buttons = [
    PluginMenuButton(
        link='plugins:netbox_physical_storage:storagebay_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    )
]

#
# Define the storage bay menu
#
storagebay_menu = (
    PluginMenuItem(
        link='plugins:netbox_physical_storage:storagebay_list',
        link_text='Storage Bays',
        buttons=storagedevice_buttons,
    ),
)

#
# Define storage device type menu buttons
#
storagedevicetype_buttons = [
    PluginMenuButton(
        link='plugins:netbox_physical_storage:storagedevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    )
]

#
# Define storage device manufacturer menu buttons
#
storagedevicemanufacturer_buttons = [
    PluginMenuButton(
        link='plugins:netbox_physical_storage:storagedevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    )
]

#
# Define the storage device type menu
#
storagedevicetype_menu = (
    PluginMenuItem(
        link='plugins:netbox_physical_storage:storagedevice_list',
        link_text='Storage Device Types',
        buttons=storagedevicetype_buttons,
    ),
    PluginMenuItem(
        link='plugins:netbox_physical_storage:storagedevice_list',
        link_text='Manufacturers',
        buttons=storagedevicemanufacturer_buttons,
    )
)

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="Storage",

        groups=(
            ("Storage Devices", storagedevice_menu),
            ("Storage Device Types", storagedevicetype_menu),
            ("Storage Bays", storagebay_menu),
        ),
        icon_class="mdi mdi-harddisk",
    )
else:
    menu_items = menu_buttons