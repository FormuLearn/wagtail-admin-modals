from wagtail.models import Page
from wagtail.admin.panels import HelpPanel
from wagtail_admin_modals.panels import ButtonPanel


class HomePage(Page):

    content_panels = Page.content_panels + [
        ButtonPanel(url_name="test_modal", label="Open Test Modal"),
    ]
    
