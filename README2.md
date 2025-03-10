# aa base plugin

[![Badge: Version]][pypi]
[![Badge: License]][license]
[![Badge: Supported Python Versions]][pypi]
[![Badge: Supported Django Versions]][pypi]
![Badge: pre-commit]
[![Badge: pre-commit.ci status]][pre-commit.ci status]
[![Badge: Code Style: black]][black code formatter documentation]
[![Badge: Automated Tests]][automated tests on github]
[![Badge: Code Coverage]][codecov]

AA base plugin Module for [Alliance Auth]

## Features

- feature 1
- feature 2

## Installation

- aa base plugin is a plugin for Alliance Auth. If you don't have Alliance Auth running
  already, please install it first before proceeding. (see the official
  [Alliance Auth installation guide] for details)

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

<!-- Links -->

[alliance auth]: https://gitlab.com/allianceauth/allianceauth "Alliance Auth"
[alliance auth installation guide]: https://allianceauth.readthedocs.io/en/latest/installation/allianceauth.html "Alliance Auth installation guide"
[automated tests on github]: https://github.com/astrum-mechanica/aa-base-plugin/actions/workflows/automated-checks.yml
[badge: automated tests]: https://github.com/astrum-mechanica/aa-base-plugin/actions/workflows/automated-checks.yml/badge.svg "Automated Tests"
[badge: code coverage]: https://codecov.io/gh/astrum-mechanica/aa-base-plugin/branch/master/graph/badge.svg "Code Coverage"
[badge: code style: black]: https://img.shields.io/badge/code%20style-black-000000.svg "Code Style: black"
[badge: license]: https://img.shields.io/github/license/astrum-mechanica/aa-base-plugin "License"
[badge: pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white "pre-commit"
[badge: pre-commit.ci status]: https://results.pre-commit.ci/badge/github/astrum-mechanica/aa-base-plugin/master.svg "pre-commit.ci status"
[badge: supported django versions]: https://img.shields.io/pypi/djversions/aa-base-plugin?label=django "Supported Django Versions"
[badge: supported python versions]: https://img.shields.io/pypi/pyversions/aa-base-plugin "Supported Python Versions"
[badge: version]: https://img.shields.io/pypi/v/aa-base-plugin?label=release "Version"
[black code formatter documentation]: http://black.readthedocs.io/en/latest/
[codecov]: https://codecov.io/gh/astrum-mechanica/aa-base-plugin
[license]: https://github.com/astrum-mechanica/aa-base-plugin/blob/master/LICENSE
[pre-commit.ci status]: https://results.pre-commit.ci/latest/github/astrum-mechanica/aa-base-plugin/master "pre-commit.ci"
[pypi]: https://pypi.org/project/aa-base-plugin/
