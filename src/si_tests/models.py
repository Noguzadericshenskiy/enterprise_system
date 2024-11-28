from django.db import models
from django.utils import timezone

from si_devices.models import Device


CHOICES_STATE_TEST = (
        ("1", "ОК"),
        ("2", "В работе"),
        ("3", "Доработка"),
        ("4", "Не начинали")
    )

CHOICES_STATE_METHOD = (
    ("1", "Соответствует"),
    ("2", "Не соответствует"),
    ("3", "С замечаниями"),
)


class Check(models.Model):
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, db_index=True)
    bord = models.CharField(max_length=50, verbose_name="Плата", db_index=True)
    firmware = models.CharField(max_length=50, verbose_name="Прошивка", db_index=True)
    expected_end_date = models.DateField(verbose_name="Ожидаемая дата", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    changed_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения", null=True, blank=True)
    deadline_data = models.DateField(verbose_name="Дедлайн", null=True, blank=True)
    state = models.CharField(max_length=50, choices=CHOICES_STATE_TEST, default="4", verbose_name="Состояние")
    informathion = models.CharField(max_length=250, verbose_name="Информация", null=True, blank=True)
    change = models.CharField(max_length=250, verbose_name="Изменения", null=True, blank=True, db_index=True)
    result_testing = models.CharField(max_length=250, verbose_name="Результат", null=True, blank=True)
    approved = models.BooleanField(default=False, verbose_name="Одобрено")

    class Meta:
        verbose_name = "Испытание"
        verbose_name_plural = "Испытания"

    def full_name(self):
        if self.device.version.name == "00":
            return f"{self.device.name} {self.bord}"
        else:
            return f"{self.device.name} исп.{self.device.version.name} {self.bord}"

    def __str__(self):
        if self.device.version.name == "00":
            return f"{self.device.name} {self.bord}"
        else:
            return f"{self.device.name} исп.{self.device.version.name} {self.bord}"


class Method(models.Model):
    check_name = models.ForeignKey(
        "Check",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="methods",)
    description = models.CharField(max_length=250, verbose_name="Описание")
    comments = models.CharField(max_length=250, verbose_name="Замечания", null=True, blank=True)
    result = models.CharField(max_length=50, choices=CHOICES_STATE_METHOD, verbose_name="Результат", null=True, blank=True)
    state = models.CharField(max_length=50, choices=CHOICES_STATE_TEST, default="4", verbose_name="Состояние")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    changed_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения", null=True, blank=True)

    class Meta:
        verbose_name = "Метод"
        verbose_name_plural = "Методы"

    def __str__(self):
        return f"{self.description}"