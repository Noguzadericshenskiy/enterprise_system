from contextlib import redirect_stderr
from pickletools import read_long1

from  django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django_htmx.http import HttpResponseClientRedirect

from si_devices.forms import CreateVersionForm, DeviceCreateForm, DeviceEditForm
from si_devices.models import Version, Device

from loguru import logger


class VersionCreateView(generic.CreateView):
    form_class = CreateVersionForm
    model = Version
    context_object_name = "version"
    template_name = "si_devices/version_create.html"

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("version-success", kwargs={"pk": obj.id})


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
    context_object_name = "device_info"
    template_name = "si_devices/device_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["device"] = Device.objects.get(pk=self.kwargs["pk"])
        context["title"] = "Информация о изделии:"

        return context

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     logger.info(f"{request.META['HTTP_REFERER']}")
    #     if request.htmx:
    #         logger.info("htmx")
    #         return HttpResponse()
    #     else:
    #         logger.info(f"req  {self.request}")
    #         return self.render_to_response(context)


class DeviceCreateView(generic.CreateView):
    model = Device
    template_name = "si_devices/create_device.html"
    context_object_name = "device"
    form_class = DeviceCreateForm

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("si_devices:device-list")


def device_update(request, pk):
    from django.http import QueryDict

    device = Device.objects.get(id=pk)
    logger.info("start update")

    if request.method == "PUT":
        logger.info("start put")
        # qd = QueryDict(request.body)
        # form = DeviceEditForm(instance=device, data=qd)
        form = DeviceEditForm(instance=device)
        logger.info(f"form: {form}")
        if form.is_valid():
            device = form.save()
            logger.info("start render")
            return render(request, "si_devices/device_detail.html", {"device": device})

    form = DeviceEditForm(instance=device)
    context = {
        "form": form,
        "device": device,
        "title": "Обновление"
    }
    return render(request, "si_devices/device_form.html", context)


# def update_view(request, *args, **kwargs):
#     print(kwargs)
#     if request.htmx:
#         logger.info(f"target {request.htmx.target}")
#         print(f"{request.htmx.trigger}")
#
#         if request.method == "POST":
#             ...
#         else:
#             ...
#     else:
#         print(request.content_params())
#         return render(request, "si_devices/device_detail.html", 1)



# class DeviceUpdateView(generic.UpdateView):
#     model = Device
#     form_class = DeviceEditForm
#     # template_name = "si_devices/device_form.html"
#     context_object_name = "device_form"
#
#     def get_context_data(self, **kwargs):
#         context = {"device": Device.objects.get(pk=self.kwargs["pk"])}
#         context["title"] = "Информация о изделии:"
#         return context
#
#     def put(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         return reverse("si_devices:device-update", context)

    # def put(self, *args, **kwargs):




    # def form_valid(self, form):
    #     if self.request.htmx:
    #         logger.info("htmx")
    #     else:
    #         logger.info(f"req  {self.request}")
    #     return reverse("si_devices:device_detail", kwargs={"pk": 1})


    # def dispatch(self, request, *args, **kwargs):
    # template_name_suffix = "si_devices/device_edit"

    # success_url = "si_devices:device_detail"

    # def put(self, *args, **kwargs):
    #     if self.request.htmx:
    #         obj = self.get_object(self.request)
    #         print("htmx", obj.id)
    #         return render(self.request, "si_devices/device_detail.html")
    #     else:
    #         print("not htmx")
    #     return ...

    #     req = self.request.content_params
    #
    #     print(req)
    #     return reverse("si_devices:device_detail", kwargs={"pk":3})

    # def get_success_url(self):
    #     obj = self.object
    #     print(obj)
    #     return reverse("si_devices:device_detail", kwargs={"pk": obj.id})

    # def form_valid(self, form):
    #     print("valid")
    #     return form
    # # def put(self, *args, **kwargs):
    # #     pass
    # def form_invalid(self, form):
    #     print("invalid", not form.errors.items())
    #     return form


# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
