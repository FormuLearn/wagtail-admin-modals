# src/wagtail_admin_modals/registry.py

from wagtail import hooks
from django.urls import path
from django.templatetags.static import static
from django.utils.html import format_html

_js_injected = False
_css_injected = False

def _inject_modal_js():
    return format_html(
        '<script src="{}"></script>',
        static('wagtail_admin_modals/js/modal-workflow-wrapper.js')
    )

def _inject_modal_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('wagtail_admin_modals/css/modal-defaults.css')
    )

@hooks.register('register_modal_urls')
def _dummy_modal_urls():
    return []

@hooks.register('register_admin_urls')
def _register_admin_urls():
    """
    (Optional—only if you still want the hook-based /admin/modals/ mount.)
    """
    patterns = get_modal_urlpatterns()
    if not patterns:
        return []
    from django.urls import include, path
    return [
        path(
            'modals/',
            include((patterns, 'wagtail_admin_modals')),
        ),
    ]

def register_modal(route: str, view_cls, name: str):
    global _js_injected, _css_injected

    if not _js_injected:
        hooks.register('insert_global_admin_js')(_inject_modal_js)
        _js_injected = True
    
    if not _css_injected:
        hooks.register('insert_global_admin_css')(_inject_modal_css)
        _css_injected = True

    def _modal_urls():
        return [path(route, view_cls.as_view(), name=name)]

    hooks.register('register_modal_urls')(_modal_urls)

def get_modal_urlpatterns():
    """
    Collect and flatten all patterns returned by functions
    registered under 'register_modal_urls'.
    """
    patterns = []
    for fn in hooks.get_hooks('register_modal_urls'):
        patterns += fn()
    return patterns
