from django import forms
from django.core.exceptions import ValidationError

from si_tests.models import Check


class CheckCreateForm(forms.ModelForm):
    dev_name = forms.CharField
    class Meta:
        model = Check
        fields = [
            "device",
            "bord",
            "firmware",
            "expected_end_date",
            "deadline_data",
            "state",
            "informathion",
            "change",
            "result_testing",
        ]
        widgets = {
            "expected_end_date": forms.SelectDateWidget(),
            "deadline_data": forms.SelectDateWidget(),

        #     "name": forms.TextInput(attrs={"class": "col-lg-1"}),
        #     "description": forms.TextInput(attrs={"class": "col-lg-4"})
        }

    # def clean(self):
    #     data = self.cleaned_data
    #     name = self.cleaned_data["name"]
    #
    #     if Version.objects.filter(name=name):
    #         raise ValidationError("Такая версия уже есть")
    #     return data