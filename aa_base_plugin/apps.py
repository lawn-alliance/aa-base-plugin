from django.apps import AppConfig


class ExampleConfig(AppConfig):
    name = "aa_base_plugin"
    label = "aa_base_plugin"
    verbose_name = f"AA Base Plugin v{__version__}"
