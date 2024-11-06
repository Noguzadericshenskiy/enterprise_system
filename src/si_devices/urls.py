from django.urls import path

from si_devices import views


app_name = 'si_devices'


urlpatterns = [
    path("versions/success/<int:pk>", views.SuccessVersionView.as_view(), name="version_success"),
    path("versions/edit/<int:pk>", views.VersionEditView.as_view(), name="version_edit"),
    path("versions/create/", views.VersionCreateView.as_view(), name="version_create"),
    path("versions/", views.VersionListView.as_view(), name="version_list"),

    path("devices/<int:pk>/update/", views.DeviceUpdateView.as_view(), name="device_edit"),
    path("devices/create/", views.DeviceCreateView.as_view(), name="device_create"),
    path("devices/", views.DeviceListView.as_view(), name="device_list"),
]
