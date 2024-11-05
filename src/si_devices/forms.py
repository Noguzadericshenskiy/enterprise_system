import logging

from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from loguru import logger

from si_devices.models import Device, Version


log = logger.debug("form_device")


class CreateVersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ["name", "title"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "col-lg-1"}),
            "title": forms.TextInput(attrs={"class": "col-lg-4"})
        }

    @logger.catch()
    def clean(self):
        data = self.cleaned_data
        name = self.cleaned_data["name"]
        logger.info(name)
        logger.info(self.cleaned_data)

        if Version.objects.filter(name=name):
            raise ValidationError("Такая версия уже есть")
        return data


