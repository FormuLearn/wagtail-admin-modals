# example_site/home/views.py

from wagtail_admin_modals.views import BaseModalView

class TestModalView(BaseModalView):
    
    def get_template_vars(self, request, *args, **kwargs):
        return {
            "header": "👋 Welcome to Your Modal",
            "content": "<p>This is a test powered by wagtail_admin_modals.</p>",
        }

    def get_json_data(self, request, *args, **kwargs):
        # no dynamic JSON injection needed for this demo
        return {}
