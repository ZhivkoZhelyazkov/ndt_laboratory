from ndt_laboratory.common import form_mixins
from django import forms
from ndt_laboratory.ndts.models import Ndt


class NdtCreateForm(form_mixins.BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    class Meta:
        model = Ndt
        exclude = ('user',)
