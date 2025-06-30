# example_site/home/wagtail_hooks.py

from wagtail_admin_modals.registry import register_modal
from .views import TestModalView

# Mounts at /admin/modals/test-modal/
register_modal('test-modal/', TestModalView, name='test_modal')
