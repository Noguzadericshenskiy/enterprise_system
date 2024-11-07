from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from si_users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        "required": "required"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "required": "required"
    }))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Введите фамилию"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Введите E-Mail"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль",}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Подтвердите пароль",}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Введите фамилию"}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "readonly": True,
        "placeholder": "Введите имя пользователя"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"required": False,}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Введите E-Mail"}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "image"]
