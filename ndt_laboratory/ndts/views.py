from django.views import generic as views
from ndt_laboratory.ndts.models import Ndt


class NdtsListView(views.ListView):
    template_name = 'ndts_list.html'
    model = Ndt


class NdtDetailsView(views.DetailView):
    template_name = 'ndt_details.html'
    model = Ndt


class CreateBlogView(views.CreateView):
    template_name = 'ndt_create.html'
    model = Ndt
    fields = ('type', 'name', 'standard', 'description', 'image')