# Example plugin app for Alliance Auth

This is an example plugin app for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) (AA) that can be used as starting point to develop custom plugins.

![License](https://img.shields.io/badge/license-MIT-green) ![python](https://img.shields.io/badge/python-3.5-informational) ![django](https://img.shields.io/badge/django-2.2-informational)

## What it can do

- The plugin can be installed, upgraded and removed into an existing AA installation using PyInstaller.

- The app can be accessed through a menu item in the sidebar.

- It has one view that shows a table with dummy data retrieved from an API.

## How to install it

To test install this example plugin into your AA dev project run this command within your virtual Python environment of AA:

```bash
pip install git+https://gitlab.com/ErikKalkoken/allianceauth-example-plugin
```

## How to use it

To use this example as basis for your own development, fork this repo and clone it into on your dev machine.

### Folder structure

For this app to work within the Django project the package folder (e.g. "example") needs to be in the same folder as your `manage.py` file.

This should look something like this:

```plain
myauth/
|- example/
|- myauth/
|- log
|- __init__.py
|- manage.py
|- supervisor.conf
```

Note that your PyInstaller files, license and readme need to be in the same folder, so this can look a bit messy. However, with well configured  `.gitignore` and `MANIFESTR.in` this works fine. The ones provided in the repo only needs to be adjusted to your new app name and the name of your auth project.

### Renaming the app

> **Important** <br>Before installing this app into your dev AA you should rename it to something suitable for your development project. Otherwise you risk not being able to install additional apps that might also be called example.

Here is an overview of the places that you need to edit to adopt the name.

Location | Description
-- | --
/example/ | folder name
/example/templates/example/ | folder name
/example/__init__.py | app name
/example/apps.py | app name
/example/auth_hooks.py | menu hook config incl. icon and label of your app's menu item appearing in the sidebar
/example/urls.py | app name
/example/views.py | permission name and template path
/example/templates/example/base.html | Title of your app to be shown in all views and as title in the browser tab
/example/templates/example/index.html | template path
/.gitignore | path of files to include / exclude for git
/MANIFEST.IN | path of files to include / exclude for PyInstaller
/setup.py | package name

> **Note** <br>You can also do a full text search for the keyword "example" in the source files to find most of them.

### Installing into your dev AA

Once you have cloned or copied all files into place and finished renaming the app you are ready to install it to your dev AA instance.

First add your app to the Django project by adding a string with the name of your app to INSTALLED_APPS in `settings/local.py`.

Then run a check to see if everything is setup correctly.

```bash
python manage.py check
```

In case they are errors make sure to fix them before proceeding.

Next perform migrations to add your model to the database:

```bash
python manage.py migrate
```

Finally restart your AA server and that's it.

> **Final note** <br>If you made a new app for AA please consider sharing it with the rest of the community. For any questions on how to share your app please contact the AA devs on their Discord. You find the current community creations [here](https://gitlab.com/allianceauth/community-creations).
