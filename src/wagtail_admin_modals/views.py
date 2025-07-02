import abc
from django.views import View
from wagtail.admin.modal_workflow import render_modal_workflow

class BaseModalView(View, metaclass=abc.ABCMeta):
    """
    Abstract base class for Wagtail admin modals.

    Subclasses must define:
      - template_name: path to the template to render in the modal
      - template_vars: dict or callable(request, *args, **kwargs) returning dict
      - json_data: dict or callable(request, *args, **kwargs) returning dict
    """

    # Subclasses should override these attributes:
    template_name = "wagtail_admin_modals/base_modal.html"
    template_vars = {}
    json_data = {}
    css_files = []
    js_files = []

    @abc.abstractmethod
    def get_template_vars(self, request, *args, **kwargs):
        """Return a dict of context variables for rendering."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_json_data(self, request, *args, **kwargs):
        """Return a dict to be returned as json_data for the modal workflow."""
        raise NotImplementedError
    
    def _append_css_files(self, template_vars: dict):
        if not isinstance(self.css_files, list):
            raise ValueError('Classes that extend wagtail_admin_modals.views.BaseModalView css_files attribute must be of type List[str]')
        if not ('css_files' in template_vars):
            template_vars['css_files'] = self.css_files
        elif isinstance(template_vars['css_files'], list):
            template_vars['css_files'] += self.css_files

        return template_vars

    def _append_js_files(self, template_vars: dict):
        if not isinstance(self.js_files, list):
            raise ValueError('Classes that extend wagtail_admin_modals.views.BaseModalView js_files attribute must be of type List[str]')
        if not('js_files' in template_vars):
            template_vars['js_files'] = self.js_files
        elif isinstance(template_vars['js_files'], list):
            template_vars['js_files'] += self.js_files

        return template_vars
    
    def _append_tab_vars(self, tpl_vars):
        """
        No-op in the base class. TabbedModalView will override this.
        """
        tpl_vars.setdefault('tabs', [])
        return tpl_vars

    def get(self, request, *args, **kwargs):
        # Resolve template name
        if self.template_name is None:
            raise ValueError(f"{self.__class__.__name__} must declare a self.template_name variable")
        
        template = self.template_name
        # Resolve context dicts
        tpl_vars = self.get_template_vars(request, *args, **kwargs)
        jdata = self.get_json_data(request, *args, **kwargs)

        # add local frontend files to template vars:
        tpl_vars = self._append_css_files(tpl_vars)
        tpl_vars = self._append_js_files(tpl_vars)
        tpl_vars = self._append_tab_vars(tpl_vars)

        return render_modal_workflow(
            request,
            template,
            None,
            template_vars=tpl_vars,
            json_data=jdata,
        )


from django.template.loader import render_to_string

class TabbedModalView(BaseModalView):
    """
    Subclasses should set:
      - tabs: a list of dicts with keys:
          * key:   unique string, used in IDs
          * title: displayed in the tab nav
          * template: path to a small template for that pane
          * context: (optional) extra vars for that pane
    """
    tabs = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # append the tab-switching script
        # ensure our tabs CSS and JS are injected
        self.css_files = getattr(self, 'css_files', []) + [
            'wagtail_admin_modals/css/modal-tabs.css',
        ]
        self.js_files = getattr(self, 'js_files', []) + [
            'wagtail_admin_modals/js/modal-tabs.js',
        ]

    def _append_tab_vars(self, tpl_vars):
        """
        Render each tab’s template into HTML, then store a list of
        {'key','title','html'} in tpl_vars['tabs'].
        """
        rendered = []
        for tab in self.tabs:
            pane_context = {**tpl_vars, **tab.get('context', {})}
            html = render_to_string(tab['template'], pane_context)

            rendered.append({
                'key':   tab['key'],
                'title': tab['title'],
                'html':  html,
            })

        tpl_vars['tabs'] = rendered
        return tpl_vars
