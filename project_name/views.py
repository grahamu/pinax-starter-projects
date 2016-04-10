from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .compat import LoginRequiredMixin
from .models import CloudSpotting


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("cloudspotting_list"))
    return render(request, "homepage.html")


class CloudSpottingCreateView(LoginRequiredMixin, CreateView):
    model = CloudSpotting
    fields = ["cloud_type"]
    template_name = "cloudspotting_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CloudSpottingCreateView, self).form_valid(form)


class CloudSpottingDetailView(DetailView):
    model = CloudSpotting
    template_name = "cloudspotting_detail.html"


class CloudSpottingListView(ListView):
    model = CloudSpotting
    template_name = "cloudspotting_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CloudSpottingUpdateView(UpdateView):
    model = CloudSpotting
    fields = ["cloud_type"]
    template_name = "cloudspotting_form.html"


class CloudSpottingDeleteView(DeleteView):
    model = CloudSpotting
    success_url = reverse_lazy("cloudspotting_list")
    template_name = "cloudspotting_confirm_delete.html"
