from django.urls import path

from si_devices import views


app_name = 'si_devices'


urlpatterns = [
    path("versions/success/<int:pk>", views.SuccessVersionView.as_view(), name="version_success"),
    path("versions/create/", views.CreateVersionView.as_view(), name="version_create"),

]
