from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from si_devices.forms import CreateVersionForm
from si_devices.models import Version, Device


class CreateVersionView(generic.CreateView):
    form_class = CreateVersionForm
    model = Version
    context_object_name = "version"
    template_name = "si_devices/version_create.html"

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("si_devices:success", kwargs={"pk": obj.id})


class SuccessVersionView(generic.DetailView):
    model = Version
    template_name = "si_devices/version_success.html"
