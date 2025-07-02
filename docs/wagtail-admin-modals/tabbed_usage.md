---
title: Tabbed Usage
description: Create a multi-pane modal with TabbedModalView
slug: /projects/wagtail-admin-modals/tabbed-usage
sidebar_position: 3
---

# Tabbed Modal Usage

Follow these steps to register a tabbed modal and launch it from your page edit interface.

---

## 1. Define your `TabbedModalView`

```python
# myapp/views.py
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
```

## 2. Register the Modal

```python
# myapp/wagtail_hooks.py
from wagtail_admin_modals.registry import register_modal
from .views import MyTabbedModal

register_modal(
    route='my-tabs/',       # mounts at /admin/modals/my-tabs/
    view_cls=MyTabbedModal,
    name='my_tabs'          # reverse as wagtail_admin_modals:my_tabs
)
```

## 3. Add launch buttons to your page model

```python
# myapp/models.py
from wagtail.models import Page
from wagtail_admin_modals.panels import ButtonPanel

class HomePage(Page):
    content_panels = Page.content_panels + [
        #...
        ButtonPanel(url_name='my_tabs',    label='Open Tabs Modal'),
    ]
```

> "`url_name` must match the name used in `register_modal`."

## 4. Create each tab’s template
> In `home/templates/home/modals/info_tab.html`

```html
{# Info tab pane #}
<div class="info-tab">
  <p>{{ text }}</p>
</div>
```

> In `home/templates/home/modals/info_tab.html`

```html
{# Settings tab pane #}
<div class="settings-tab">
  <p>Settings content goes here.</p>
</div>
```

That’s all, your tabbed modal is ready! You will see it in the admin interface for whatever model you added the ButtonPanel to.