from django.shortcuts import render


def index(request):
    return render(request, "si_system/index.html")
