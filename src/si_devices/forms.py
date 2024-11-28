from django import forms
from django.core.exceptions import ValidationError

from si_devices.models import Device, Version, CHOICES_DEVICE_TYPE_RELEASE


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
    decimal_num = forms.CharField(widget=forms.TextInput(), required=False)
    constructor = forms.CharField(widget=forms.TextInput(), required=False)
    description = forms.CharField(widget=forms.TextInput(), required=False)
    image = forms.ImageField(widget=forms.FileInput(), required=False)

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
    # name = forms.CharField(widget=forms.TextInput(attrs={}),)
    # version = forms.CharField(widget=forms.CharField(choices=Version.name, attrs={}),)
    # bord = forms.CharField(widget=forms.TextInput(),)
    # firmware = forms.CharField(widget=forms.TextInput(),)
    decimal_num = forms.CharField(widget=forms.TextInput(), required=False)
    constructor = forms.CharField(widget=forms.TextInput(), required=False)
    # type_release = forms.CharField(widget=forms.CharField(choices=CHOICES_DEVICE_TYPE_RELEASE,),)
    description = forms.CharField(widget=forms.TextInput(), required=False)
    image = forms.ImageField(widget=forms.FileInput(), required=False)

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
