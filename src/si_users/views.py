from django.shortcuts import render


def login(request):
    return render(request, "si_users/login.html")


def registration(request):
    return render(request, "si_users/registration.html")
