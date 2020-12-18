import os
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from ndt_laboratory.ndts.forms import NdtCreateForm
from ndt_laboratory.ndts.models import Ndt


def clean_up_files(path):
    os.remove(path)


class NdtsListView(views.ListView):
    template_name = 'ndts_list.html'
    model = Ndt


class NdtDetailsView(views.DetailView):
    template_name = 'ndt_details.html'
    model = Ndt


class CreateNdtView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'ndt_create.html'
    form_class = NdtCreateForm
    model = Ndt

    def get_success_url(self):
        return reverse_lazy('ndt details', kwargs={'pk': self.object.id, 'slug': self.object.slug})

    def form_valid(self, form):
        ndt = form.save(commit=False)
        ndt.user = self.request.user
        ndt.save()
        return super().form_valid(form)


class UpdateNdtView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'ndt_edit.html'
    model = Ndt
    form_class = NdtCreateForm

    def get_success_url(self):
        return reverse_lazy('ndt details', kwargs={'pk': self.object.id, 'slug': self.object.slug})

    def form_valid(self, form):
        old_image = self.get_object().image
        if old_image:
            clean_up_files(old_image.path)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        ndt = self.get_object()
        if ndt.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class DeleteNdtView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'ndt_delete.html'
    model = Ndt
    success_url = reverse_lazy('ndts list')

    def dispatch(self, request, *args, **kwargs):
        ndt = self.get_object()
        if ndt.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
