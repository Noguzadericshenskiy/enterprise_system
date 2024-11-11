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
    image = forms.ImageField(widget=forms.FileInput(), required=False)
        # "name": "file_device",
        # "class": "form-control"


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


class DeviceEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={}),)
    version = forms.CharField(widget=forms.TextInput(),)
    # bord = forms.CharField(widget=forms.TextInput(),)
    # firmware = forms.CharField(widget=forms.TextInput(),)
    # decimal_num = forms.CharField(widget=forms.TextInput(),)
    # constructor = forms.CharField(widget=forms.TextInput(),)
    # type_release = forms.CharField(widget=forms.TextInput(),)
    # description = forms.CharField(widget=forms.TextInput())
    # image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Device
        fields = [
            "name",
            "version",
            # "bord",
            # "firmware",
            # "decimal_num",
            # "constructor",
            # "type_release",
            # "description",
            # "image"
        ]


