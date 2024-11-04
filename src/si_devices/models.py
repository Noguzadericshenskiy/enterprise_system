from django.db import models
from django.utils import timezone


CHOICES_DEVICE_TYPE_RELEASE = (
    ("1", "Серия"),
    ("2", "Опытное"),
    ("3", "Иное"),
)


class Device(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    version = models.ForeignKey("Version", on_delete=models.DO_NOTHING, verbose_name="Версия")
    title = models.CharField(verbose_name="Название", null=True, blank=True)
    bord = models.CharField(verbose_name="Плата", null=True, blank=True)
    firmware = models.CharField(verbose_name="Прошивка", null=True, blank=True)
    designer = models.CharField(max_length=200, verbose_name="Конструктор")
    engineer = models.CharField(max_length=200, verbose_name="Изменил", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    date_changed = models.DateTimeField(verbose_name="Дата изменения", null=True, blank=True)
    type_device = models.CharField(verbose_name="Тип изделия", null=True, blank=True)
    type_release = models.CharField(choices=CHOICES_DEVICE_TYPE_RELEASE, default="1", verbose_name="Вид выпуска")
    decimal_num = models.CharField(verbose_name="Децимальный номер")

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"

    @property
    def full_name(self):
        return f"{self.name} {self.version.name} {self.bord}"

    def __str__(self):
        return f"{self.name} {self.version.name} {self.bord}"

    # def name_version(self):
    #     return f"{self.name} {self.version.name}"


class Version(models.Model):
    name = models.CharField(max_length=10, verbose_name="Версия изделия", unique=True)
    title = models.CharField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Версия"

    def __str__(self):
        return f"{self.name}"
