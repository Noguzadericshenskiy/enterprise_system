from django.contrib import admin

from si_devices.models import Device, Version


admin.site.register(Device)
admin.site.register(Version)
