from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import HelpPanel
from django.utils.safestring import mark_safe


class HomePage(Page):

    content_panels = Page.content_panels + [
        HelpPanel(template="panels/test_modal.html", heading="Test Modal"),
    ]
    
