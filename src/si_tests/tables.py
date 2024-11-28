from django_tables2 import tables

from si_tests.models import Check, Method


class CheckTable(tables.Table):
    class Meta:
        model = Check
        template_name = 'django_tables2/bootstrap.html'
        fields = (
            "device",
            "bord",
            "firmware",
            "expected_end_date",
            "deadline_data",
            "state",
            "informathion",
            "change",
            "result_testing",
            "approved",
                  )
