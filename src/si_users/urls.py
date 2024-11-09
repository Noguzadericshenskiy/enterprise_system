from django.urls import path

from si_users.views import login, registration, profile, logout

app_name = "si_users"

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
]
