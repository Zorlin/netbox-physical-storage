from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

storagedevice_buttons = [
    PluginMenuButton(
        link='plugins:netbox_physical_storage:storagedevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN,
    ),
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_physical_storage:storagedevice_list',
        link_text='Storage Devices',
        buttons=storagedevice_buttons,
    ),
)