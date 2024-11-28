from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from si_tests import views


app_name = "si_tests"


urlpatterns = [
    path("<int:pk>/update", views.TestUpdateView.as_view(), name="test-update"),
    path("create", views.TestCreateView.as_view(), name="test-create"),
    path("<int:pk>", views.DetailView.as_view(), name="test-detail"),
    path("", views.TestListView.as_view(), name="test-list"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)