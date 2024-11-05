import logging

from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError


from si_devices.models import Device, Version


class CreateVersionForm(ModelForm):
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


