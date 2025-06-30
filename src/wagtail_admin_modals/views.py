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
    template_name = None
    template_vars = {}
    json_data = {}

    @abc.abstractmethod
    def get_template_name(self):
        """Return the template name for the modal."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_template_vars(self, request, *args, **kwargs):
        """Return a dict of context variables for rendering."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_json_data(self, request, *args, **kwargs):
        """Return a dict to be returned as json_data for the modal workflow."""
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        # Resolve template name
        template = self.get_template_name() or self.template_name
        # Resolve context dicts
        tpl_vars = self.get_template_vars(request, *args, **kwargs)
        jdata = self.get_json_data(request, *args, **kwargs)

        return render_modal_workflow(
            request,
            template,
            None,
            template_vars=tpl_vars,
            json_data=jdata,
        )
