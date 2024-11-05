from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from si_devices.models import Device, Version


class CreateVersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ["name", "title"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput()
        }

    def clean_name(self):
        name = self.cleaned_data["name"]

        if Version.objects.filter(name=name):
            raise ValidationError("Такая версия уже есть")