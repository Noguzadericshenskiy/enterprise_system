from audioop import reverse
from fileinput import filename
from lib2to3.fixes.fix_input import context

from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from si_devices.forms import CreateVersionForm, DeviceCreateForm, DeviceEditForm
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
    template_name = "si_devices/versions.html"


    def get_queryset(self):
        context = {}
        context["title"] = "Версии"
        context["versions"] = Version.objects.all()
        return context

    # def get_context_data(self, **kwargs):
    #     con = {}
    #     con["title"] = "Версии"



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
    template_name = "si_devices/device_detail.html"
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["description"] = Device.objects.get(pk=self.kwargs["pk"])
        context["title"] = "Информация о изделии:"
        return context


class DeviceCreateView(generic.CreateView):
    model = Device
    template_name = "si_devices/create_device.html"
    context_object_name = "device"
    form_class = DeviceCreateForm

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("si_devices:device_list")


class DeviceUpdateView(generic.UpdateView):
    # def dispatch(self, request, *args, **kwargs):
    model = Device
    form_class = DeviceEditForm
    template_name = "si_devices/device_edit.html"
    context_object_name = "device"

    def get_success_url(self):
        obj = self.object.id
        print(obj)
        return reverse("si_devices:device_detail", kwargs={"pk": obj})




# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
