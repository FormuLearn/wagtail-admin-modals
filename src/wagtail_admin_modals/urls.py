# src/wagtail_admin_modals/urls.py

from wagtail import hooks
from django.urls import include, path

app_name = 'wagtail_admin_modals'

def modal_urlpatterns(prefix: str = ''):
    """
    Return a single include() that gathers up all 
    `register_modal_urls` hooks under `prefix`.
    """
    # Collect every modal URL (each fn returns a [ path(...) ] list)
    patterns = []
    for fn in hooks.get_hooks('register_modal_urls'):
        patterns += fn()

    # If nobody registered, give back an empty list
    if not patterns:
        return []

    # Wrap them in a Django include
    return [
        path(prefix, include((patterns, app_name))),
    ]
