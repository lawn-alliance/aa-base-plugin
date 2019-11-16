# Setup development environment for AA on Windows

This documents describes how to setup a development environment for Alliance Auth (AA) on Windows.

There are many different ways how to setup a development environment on Windows, mostly depending on your preferred choice of IDE. This guide will describe a setup on Windows with WSL / Ubuntu and Visual Studio Code (VSC) as editor / IDE.

The basic outline is:

- Windows 10 with WSL Ubuntu
- VSC on Windows with [WSL extension](https://code.visualstudio.com/docs/remote/wsl)
- ngrok on Windows
- AA is installed from official doc on WSL
- all code on WSL

## WSL

Install WSL with Ubuntu on Windows 10 from your Microsoft store

## VSC

Install VSC from the [official website](https://code.visualstudio.com/). 

In VSC install the following extensions:

- [Remote WSL](https://code.visualstudio.com/docs/remote/wsl)
- Python

Once you fully setup you can start VSC from the root of your AA instance folder (e.g. `~/dev/aa-dev`) with this command from WSL:

```bash
code .
```

Note that you can also start a Windows explorer directly from your current WSL folder in order to copy files between WSL and Windows:

```bash
explorer.exe .
```

## ngrok

You need to install and run [ngrok](https://ngrok.com/) to enable authentication of your AA instance with EVE SSO. Since ngrok will give you a new URL after every reboot you will need to update your EVE SSO app and the AA settings accordingly after every reboot.

## AA

### Folder structure

Basic folder structure on WSL (e.g. in `~/dev/aa-dev`) for an AA instance:

```text
aa-dev
+-- venv
+-- myauth
+-- myapp
+-- ...
```

Details on folders:

- `venv`: holds the virtual environment for this instance and is shared with all apps
- `myauth`: your AA project folder, e.g. holding settings and log files
- `myapp`: the AA plugin app you are developing. It has its own git and can be installed into this AA instance with `pip install -e myapp` plus you need to add the app in INSTALLED_APPS in the `local.py` settings under `myauth/settings` like any AA app.

You can add and develop multiple apps to this AA instance as needed.

You can also add additional AA instances on your WSL if needed. (e.g. one as you main development instance, and one for testing out apps from others). We would recommend to rebuild a new instance from scratch and not copying an existing folder structure, because some paths are absolute (e.g. in venv).

### Installation

You can follow the [official documentation](https://allianceauth.readthedocs.io/en/latest/installation/) for installing AA into your aa-dev folder.

However note these differences:

- Different folder placement for virtual environment, since we need one venv for each AA instance
- WSL does not have a startup capability (systemd) and can not run supervisor, so you need to start redis and mysql manually after each reboot:
    ```bash
    # start redis
    redis-server

    # start mysql
    service mysql start
    ```
- We would advise against installing AA as root. Instead install as your main user and use sudo where needed (e.g. for installing services).
