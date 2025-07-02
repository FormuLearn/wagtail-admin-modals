# src/wagtail_admin_modals/panels.py

from wagtail.admin.panels import Panel

class ButtonPanel(Panel):
    """
    A simple button that launches a wagtail-admin-modals modal.
    """
    def __init__(self, *, url_name: str, label: str, **kwargs):
        # url_name: e.g. "test_modal"
        # label: the button text
        # kwargs: any of Panel's own args (heading, classname, help_text, attrs)
        super().__init__(**kwargs)
        self.url_name = url_name
        self.label = label

    def clone_kwargs(self):
        """
        Ensure Wagtail’s Panel.clone() carries url_name+label forward.
        """
        kw = super().clone_kwargs()
        kw.update({
            'url_name': self.url_name,
            'label': self.label,
        })
        return kw

    class BoundPanel(Panel.BoundPanel):
        template_name = "wagtail_admin_modals/panels/button_panel.html"

        def __init__(self, panel, instance, request, form, prefix, *args, **kwargs):
            # Must match Wagtail 7’s signature:
            # BoundPanel(panel, instance, request, form, prefix)
            super().__init__(panel, instance, request, form, prefix, *args, **kwargs)
            self.url_name = panel.url_name
            self.label = panel.label
            self.full_url_name = f"wagtail_admin_modals:{self.url_name}"

        def get_context_data(self, parent_context):
            """
            Add our two variables into the template context.
            """
            context = super().get_context_data(parent_context)
            context.update({
                'url_name': self.url_name,
                'label': self.label,
                'full_url_name': self.full_url_name,
            })
            return context
