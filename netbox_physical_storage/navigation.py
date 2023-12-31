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
# Define the top-level menu
#
menu_buttons = (
    PluginMenuItem(
        link='plugins:netbox_physical_storage:storagedevice_list',
        link_text='Storage Devices',
        buttons=storagedevice_buttons,
    ),
)

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="Physical Storage",
        groups=(("Storage Devices", menu_buttons),),
        icon_class="mdi mdi-harddisk",
    )
else:
    menu_items = menu_buttons