# NetBox Physical Storage Plugin

A [Netbox](https://github.com/netbox-community/netbox) plugin for physical storage management.

CURRENTLY DOES NOT DO ANYTHING USEFUL. HERE BE DRAGONS, BE WARNED.

## Features

This plugin plans to provide the following features:

- Allows you to add Storage Devices

## Future features

These are things I've been thinking about, but haven't implemented.

- Storage devices
    - Size of device
- Extends Component Assignment to allow you to select a Storage Interface
- Allows you to add Storage Interfaces to Device Types and Devices
- SAS cabling/topology (potentially with visualisation as a stretch goal?)
- Performance classes of drives (enterprise, WORM, SMR etc)
- DWPD?

## Credits

Based on the NetBox plugin tutorial by [jeremystretch](https://github.com/jeremystretch):

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

Portions taken from [Ryan Merolle](https://github.com/ryanmerolle/netbox-acls)

## Contributing

This project is currently maintained by [Benjamin Arntzen](https://github.com/zorlin)

See the [CONTRIBUTING](CONTRIBUTING.md) for more information.

## Compatibility

Each Plugin version listed below has been tested with its corresponding NetBox version.

| NetBox version | Plugin version |
|:--------------:|:--------------:|
|      3.6       |     0.0.1      |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

You can install with pip:

```bash
pip install netbox-physical-storage
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
netbox-physical-storage
```

## Configuration

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    "netbox_physical-storage"
]

PLUGINS_CONFIG = {
    "netbox_physical-storage": {
        "top_level_menu": True # If set to True the plugin will add a top level menu item for the plugin. If set to False the plugin will add a menu item under the Plugins menu item.  Default is set to True.
    },
}
```

## Screenshots

None yet.
