from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django_tables2 import SingleTableView

from si_tests.models import Check, Method
from si_tests.forms import CheckCreateForm
from si_tests.tables import CheckTable


class  TestListView(SingleTableView, ListView):
    model = Check
    table_class = CheckTable
    context_object_name = "context"
    template_name = "si_tests/test_list.html"

    def get_queryset(self):
        context = {
            "title": "Список тестирования",
            "checks": Check.objects.order_by("device__name", "device__version", "device__bord"),
            "table": Check.objects.order_by("device__name", "device__version", "device__bord")
        }

        return context


class TestCreateView(CreateView):
    model = Check
    template_name = "si_tests/create_test.html"
    context_object_name = "context"
    form_class = CheckCreateForm

    def get_success_url(self):
        obj = self.object
        return reverse_lazy("si_tests:test-list")


class TestDetailView(DetailView):
    ...


class TestUpdateView(UpdateView):
    ...
