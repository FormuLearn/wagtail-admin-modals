---
title: Getting Started
description: Quickstart guide for wagtail-admin-modals
slug: /projects/wagtail-admin-modals/getting-started
sidebar_position: 1
---

# Getting Started with **wagtail-admin-modals**

Just two simple steps to enable modals in your Wagtail project:

1. **Install the package**  
   ```bash
   pip install wagtail-admin-modals
   ```
2. **Enable the app**
   In your project’s `settings/base.py`, add
   ```python
   INSTALLED_APPS = [
        # …
        'wagtail_admin_modals',
    ]
   ```

Your Wagtail admin is now ready to register and render custom modals. For a live demo, follow the instructions [here](index.md). To see more, continue to [Basic Usage](basic_usage.md)