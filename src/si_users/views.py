from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from si_users.models import User
from si_users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user:
                # добавть доп проверку если пользователь одобрен
                # if user.approved:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                # else:
                #     context = {
                #         "form": form,
                #         "error_messages": {
                #             "not_approved": "Пользователь не аккредитован!"
                #             "Обратитесь к администратору для получения аккредитации.",
                #         },
                #     }
                #     render(request, "si_users/login.html", context)
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "si_users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались! Для активации аккаунта необходимо сообщить администратору!")
            # Изменить переход на перевести пользователя на страницу вывода сообщения
            # об ожидании подтверждения регистрации
            return HttpResponseRedirect(reverse("si_users:login"))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "si_users/registration.html", context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("si_users:profile"))

    form = UserProfileForm(instance=request.user)
    context = {"title": "Профиль пользователя", "form": form}
    return render(request, "si_users/profile.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("si_users:login"))
