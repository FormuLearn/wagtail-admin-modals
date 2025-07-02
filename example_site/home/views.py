# example_site/home/views.py

from wagtail_admin_modals.views import BaseModalView

class TestModalView(BaseModalView):

    js_files = [
        'js/test_file.js',
    ]

    css_files = [
        'css/test_file.css',
    ]
    
    def get_template_vars(self, request, *args, **kwargs):
        return {
            "header": "👋 Welcome to Your Modal",
            "content": "<p>This is a test powered by wagtail_admin_modals.</p>",
        }

    def get_json_data(self, request, *args, **kwargs):
        # no dynamic JSON injection needed for this demo
        return {}

# example_site/home/views.py

from wagtail_admin_modals.views import TabbedModalView

class MyTabbedModal(TabbedModalView):
    template_name = "wagtail_admin_modals/base_modal_tabbed.html"

    def get_template_vars(self, request, *args, **kwargs):
        return {
            'header': "My Tabbed Modal",
        }

    def get_json_data(self, request, *args, **kwargs):
        return {}

    tabs = [
      {
        'key': 'info',
        'title': 'Info',
        'template': 'home/modals/info_tab.html',
        'context': {'text': "This is the info pane"},
      },
      {
        'key': 'settings',
        'title': 'Settings',
        'template': 'home/modals/settings_tab.html',
      },
    ]
