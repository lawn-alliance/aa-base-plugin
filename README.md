# Example plugin app for Alliance Auth

This is an example plugin app for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) (AA) that can be used as starting point to develop custom plugins.

![License](https://img.shields.io/badge/license-MIT-green) ![python](https://img.shields.io/badge/python-3.5-informational) ![django](https://img.shields.io/badge/django-2.2-informational)

## Features

- The plugin can be installed, upgraded and removed into an existing AA installation using PyInstaller.

- It shows a browsable table with the all the countries of the world and can be accessed through its own menu item on the sidebar.

## Installation

To install this plugin into your AA project run this command within your virtual Python environment of AA:

```bash
pip install git+https://gitlab.com/ErikKalkoken/allianceauth-example-plugin
```

## Development

To use this example as basis for your own development, fork it and clone it to your dev machine. Then you need to install it into your dev AA installation. For that the top folder "example" needs to be in the same folder as your `manage.py` script.
