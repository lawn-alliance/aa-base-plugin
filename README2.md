# App Name

App info

## Features

- feature 1
- feature 2

## Installing

app name is a plugin for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth). If you don't have Alliance Auth running already, please install it first before proceeding. (see the official [AA installation guide](https://allianceauth.readthedocs.io/en/latest/installation/auth/allianceauth/) for details)

```bash
pip install app-name
```

Configure your Auth settings (`local.py`) as follows:

- Add `'app-name'` to `INSTALLED_APPS`
- Add the following lines to your settings file:

```python
something
```

Run migrations & copy static files

```bash
python manage.py migrate
python manage.py collectstatic
```

Restart your supervisor services for Auth

## Settings

Here is a list of available settings for this app. They can be configured by adding them to your Auth settings file (`local.py`).

Note that all settings are optional and the app will use the documented default settings if they are not used.

| Name      | Description                | Default   |
| --------- | -------------------------- | --------- |
| `Setting` | Description of the setting | `default` |

## Permissions

Here are all relevant permissions:

| Codename                        | Description                                             |
| ------------------------------- | ------------------------------------------------------- |
| `general - Can access this app` | Basic permission required by anyone to access this app. |

## Management commands

The following management commands are available:

- **command**: command description
