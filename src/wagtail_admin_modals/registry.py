# src/wagtail_admin_modals/registry.py

from wagtail import hooks
from django.urls import path, include
from django.templatetags.static import static
from django.utils.html import format_html

# Internal registry of modal endpoints is managed via hooks,
# so we don't need a separate list here.

# -----------------------------------------------------------------------------
# 1) JS injector
# -----------------------------------------------------------------------------

_js_injected = False

def _inject_modal_js():
    """
    Inject our modal-workflow wrapper script on every admin page.
    Registered dynamically on first modal registration.
    """
    return format_html(
        '<script src="{}"></script>',
        static('wagtail_admin_modals/js/modal-workflow-wrapper.js')
    )

# -----------------------------------------------------------------------------
# 2) Declare our custom URL hook (so get_hooks() always returns at least one fn)
# -----------------------------------------------------------------------------

@hooks.register('register_modal_urls')
def _dummy_modal_urls():
    return []

# -----------------------------------------------------------------------------
# 3) Mount all registered modal URLs under /admin/modals/
#    (Wagtail will call this because it's a built-in hook)
# -----------------------------------------------------------------------------

@hooks.register('register_admin_urls')
def _register_admin_urls():
    all_patterns = []
    for fn in hooks.get_hooks('register_modal_urls'):
        all_patterns += fn()
    if not all_patterns:
        return []
    return [
        # mounts at /admin/modals/<route>/
        path(
            'modals/',
            include((all_patterns, 'wagtail_admin_modals')),
            name='wagtail_admin_modals'
        ),
    ]

# -----------------------------------------------------------------------------
# 4) Public API for registering a modal
# -----------------------------------------------------------------------------

def register_modal(route: str, view_cls, name: str):
    """
    Register a modal endpoint.

    - route: URL fragment under '/admin/modals/', e.g. 'test-modal/'
    - view_cls: a subclass of BaseModalView (or any Django view)
    - name: URL name for reversing, e.g. 'test_modal'
    """
    global _js_injected

    # 1) On first registration, wire up our JS injector
    if not _js_injected:
        hooks.register('insert_global_admin_js')(_inject_modal_js)
        _js_injected = True

    # 2) Register a hook that returns this one modal's URL pattern
    def _modal_urls():
        return [path(route, view_cls.as_view(), name=name)]

    hooks.register('register_modal_urls')(_modal_urls)
