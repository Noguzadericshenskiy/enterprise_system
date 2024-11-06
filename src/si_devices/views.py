from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from si_devices.forms import CreateVersionForm, DeviceCreateForm
from si_devices.models import Version, Device


class VersionCreateView(generic.CreateView):
    form_class = CreateVersionForm
    model = Version
    context_object_name = "version"
    template_name = "si_devices/version_create.html"

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("si_devices:version_success", kwargs={"pk": obj.id})


class SuccessVersionView(generic.DetailView):
    model = Version
    template_name = "si_devices/version_success.html"


class VersionEditView(generic.UpdateView):
    model = Version
    form_class = CreateVersionForm
    template_name = ""
    context_object_name = "versions"


class VersionListView(generic.ListView):
    model = Version
    context_object_name = "device_versions"
    template_name = ""

    def get_queryset(self):
        context = Version.objects.all()
        return context


class DeviceListView(generic.ListView):
    model = Device
    context_object_name = "context"
    template_name = "si_devices/devices.html"

    def get_queryset(self):
        context = {
            "title": "Список изделий",
            "devices": Device.objects.order_by("name")
        }
        return context


class DeviceDetailView(generic.DetailView):
    model = Device
    context_object_name = "device"
    template_name = ""
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["pk"] = self.kwargs["pk"]
    #     return context

    def get_queryset(self):
        return Device.objects.get(self.kwargs["pk"])


class DeviceCreateView(generic.CreateView):
    model = Device
    template_name = "si_devices/create_device.html"
    context_object_name = "device"
    form_class = DeviceCreateForm

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("si_devices:device_list")


class DeviceUpdateView(generic.UpdateView):
    ...








