from aa_base_plugin import __version__
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExampleConfig(AppConfig):
    name = "aa_base_plugin"
    label = "aa_base_plugin"
    verbose_name = f"AA Base Plugin v{__version__}"
