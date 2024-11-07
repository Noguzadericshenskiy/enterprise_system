import logging
from django import forms
from django.core.exceptions import ValidationError

from si_devices.models import Device, Version


class CreateVersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "col-lg-1"}),
            "description": forms.TextInput(attrs={"class": "col-lg-4"})
        }

    def clean(self):
        data = self.cleaned_data
        name = self.cleaned_data["name"]

        if Version.objects.filter(name=name):
            raise ValidationError("Такая версия уже есть")
        return data


class DeviceCreateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            "name",
            "version",
            "bord",
            "firmware",
            "decimal_num",
            "constructor",
            "type_release",
            "description",
            "image"
        ]

    def clean(self):
        data = self.cleaned_data
        name = data["name"]
        bord = data["bord"]
        version = data["version"]

        if Device.objects.filter(name=name, bord=bord, version__name=version):
            raise ValidationError(f"Такое изделие уже есть! Наименование + версия + плата должно быть уникально!")
        else:
            return data


class DeviceUpdateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            "name",
            "version",
            "bord",
            "firmware",
            "decimal_num",
            "type_release",
            "description",
            "image"
        ]

    def clean(self):
        data = self.cleaned_data
        name = data["name"]
        bord = data["bord"]
        version = data["version"]

        if Device.objects.filter(name=name, bord=bord, version__name=version):
            raise ValidationError(f"Такое изделие уже есть!\n Наименование + версия + плата должно быть уникально!")
        else:
            return data

