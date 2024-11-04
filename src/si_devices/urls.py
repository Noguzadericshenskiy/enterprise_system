from django.urls import path

from si_devices import views


app_name = 'si_devices'


urlpatterns = [
    path("create/version/", views.CreateVersionView.as_view(), name='create_version'),

]
