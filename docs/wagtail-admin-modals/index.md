---
title: wagtail-admin-modals
description: A tiny library for adding rich, workflow-style modals to the Wagtail admin.
slug: /projects/wagtail-admin-modals/
---

# Welcome to **wagtail-admin-modals**

**wagtail-admin-modals** lets you declare custom modals in your Wagtail admin with:

- A tiny registry hook: `register_modal(route, ViewClass, name)`  
- A simple **BaseModalView** (single-pane) and **TabbedModalView** (multi-pane)  
- Automatic injection of our JS/CSS wrappers  
- A minimal example site so you can see it in action  

> **Tip:** Clone this repo and run the included `example_site` to see everything live.  
> 
> ```bash
> git clone https://github.com/FormuLearn/wagtail-admin-modals.git
> cd wagtail-admin-modals/example_site
> pip install -r requirements.txt
> python manage.py runserver
> ```
> You can then navigate to: http://127.0.0.1:8000/admin/ in your browser and login with 
>
>
> **Username:** modals-example
>
> **Password:** modals-example
>
>
> Then navigate to edit the home page and see buttons for first an ordinary, and then a tabbed modal. 

---

>## More coming soon...
> This is a very early version of the library, and is just an early prototype. The library will be more extensively developed in the coming weeks and months. Pull requests and suggestions are of course welcome at this library's [GitHub Page](https://github.com/FormuLearn/wagtail-admin-modals)
