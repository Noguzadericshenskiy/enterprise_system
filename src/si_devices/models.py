from django.db import models
from django.utils import timezone


CHOICES_DEVICE_TYPE_RELEASE = (
    ("1", "Серия"),
    ("2", "Опытное"),
    ("3", "Иное"),
)


class Device(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    version = models.ForeignKey("Version", on_delete=models.PROTECT, verbose_name="Версия")
    bord = models.CharField(max_length=100, verbose_name="Плата", null=True, blank=True)
    firmware = models.CharField(max_length=50, verbose_name="Прошивка", null=True, blank=True)
    decimal_num = models.CharField(max_length=150, verbose_name="Децимальный номер")
    designer = models.CharField(max_length=200, verbose_name="Конструктор")
    engineer = models.CharField(max_length=200, verbose_name="Изменил", null=True, blank=True)
    type_release = models.CharField(max_length=50, choices=CHOICES_DEVICE_TYPE_RELEASE, default="1", verbose_name="Вид выпуска")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    date_changed = models.DateTimeField(verbose_name="Дата изменения", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    image = models.ImageField(upload_to="devices_images", null=True, blank=True)
    # type_device = models.CharField(max_length=250, verbose_name="Тип изделия", null=True, blank=True)

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"

    @property
    def full_name(self):
        return f"{self.name} {self.version.name} {self.bord}"

    def __str__(self):
        return f"{self.name} {self.version.name} {self.bord}"


class Version(models.Model):
    name = models.CharField(max_length=10, verbose_name="Версия изделия", unique=True)
    description = models.TextField(max_length=250, verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.name}"
