---
title: Basic Usage
description: Minimal example of registering and launching a modal (including ButtonPanel)
slug: /projects/wagtail-admin-modals/basic-usage
sidebar_position: 2
---

# Basic Usage

Follow these steps to register a modal and launch it with a `ButtonPanel`.

---

## 1. Define your modal view

```python
# myapp/views.py
from wagtail_admin_modals.views import BaseModalView

class TestModal(BaseModalView):
    def get_template_vars(self, request, *args, **kwargs):
        return {
            'header': 'Test Modal',
            'content': '<p>This is a test modal.</p>',
        }

    def get_json_data(self, request, *args, **kwargs):
        return {}
```

## 2. Register the modal
```python
# myapp/wagtail_hooks.py
from wagtail_admin_modals.registry import register_modal
from .views import TestModal

register_modal(
    route='test-modal/',    # mounts at /admin/modals/test-modal/
    view_cls=TestModal,
    name='test_modal'       # used for reversing as wagtail_admin_modals:test_modal
)
```

## 3. Launch it with a ButtonPanel
```python
# myapp/models.py
from wagtail.models import Page
from wagtail_admin_modals.panels import ButtonPanel

class HomePage(Page):
    content_panels = Page.content_panels + [
        ButtonPanel(
            url_name='test_modal',      # must match the 'name' it is registered with in your hooks
            label='Open Test Modal'
        ),
    ]

```
