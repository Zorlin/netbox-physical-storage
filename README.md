# NetBox Physical Storage Plugin

A [Netbox](https://github.com/netbox-community/netbox) plugin for physical storage management.

## Features

This plugin plans to provide the following features:

- Extends Component Assignment to allow you to select a Storage Interface
- Allows you to add Storage Interfaces to Device Types and Devices

## Future features

These are things I've been thinking about, but haven't implemented.

- SAS cabling/topology (potentially with visualisation as a stretch goal?)

## Credits

Based on the NetBox plugin tutorial by [jeremystretch](https://github.com/jeremystretch):

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

README and devcontainers/development setup created by [Ryan Merolle](https://github.com/ryanmerolle/netbox-acls)

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

## Developing

### VSCode + Docker + Dev Containers

To develop this plugin further one can use the included .devcontainer configuration. This configuration creates a docker container which includes a fully working netbox installation. Currently it should work when using WSL 2. For this to work make sure you have Docker Desktop installed and the WSL 2 integrations activated.

1. In the WSL terminal, enter `code` to run Visual studio code.
2. Install the devcontainer extension "ms-vscode-remote.remote-containers"
3. Press Ctrl+Shift+P and use the "Dev Container: Clone Repository in Container Volume" function to clone this repository. This will take a while depending on your computer
4. If you'd like the netbox instance to be prepopulated with example data from [netbox-initializers](https://github.com/tobiasge/netbox-initializers) run `make  initializers`
5. Start the netbox instance using `make all`

Your netbox instance will be served under 0.0.0.0:8000, so it should now be available under localhost:8000.

## Screenshots

None yet.
