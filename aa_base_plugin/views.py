"""Views."""

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required
@permission_required("aa_base_plugin.basic_access")
def index(request):
    """Render index view."""
    context = {"text": "Hello, World!"}
    return render(request, "aa_base_plugin/index.html", context)
