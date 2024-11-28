from django.db import models
from django.utils import timezone


CHOICES_DEVICE_TYPE_RELEASE = (
    ("1", "Серия"),
    ("2", "Опытное"),
    ("3", "Иное"),
)


# переопределение QuerySet для Devices
# class DeviceQuerySet(models.QuerySet):
#     def total_quantity(self):
#         return sum(device for device in self.all())


class Device(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    version = models.ForeignKey("Version", on_delete=models.PROTECT, verbose_name="Версия")
    bord = models.CharField(max_length=100, verbose_name="Плата", null=True, blank=True)
    firmware = models.CharField(max_length=50, verbose_name="Прошивка", null=True, blank=True)
    decimal_num = models.CharField(max_length=150, verbose_name="Децимальный номер")
    constructor = models.CharField(max_length=200, verbose_name="Конструктор")
    engineer = models.CharField(max_length=200, verbose_name="Изменил", null=True, blank=True)
    type_release = models.CharField(max_length=50, choices=CHOICES_DEVICE_TYPE_RELEASE, default="1", verbose_name="Вид выпуска")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    changed_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    image = models.ImageField(verbose_name="Рисунок", upload_to="devices_images", null=True, blank=True)
    # type_device = models.CharField(max_length=250, verbose_name="Тип изделия", null=True, blank=True)

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"

    @property
    def full_name(self):
        if self.version.name == "00":
            return f"{self.name} {self.bord}"
        else:
            return f"{self.name} исп.{self.version.name} {self.bord}"

    def __str__(self):
        if self.version.name == "00":
            return f"{self.name}"
        else:
            return f"{self.name} исп.{self.version.name}"


class Version(models.Model):
    name = models.CharField(max_length=10, verbose_name="Версия изделия", unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    changed_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения", null=True, blank=True)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.name}"


class Bord(models.Model):
    name = models.CharField(max_length=50, verbose_name="Версия изделия", unique=True)
    description = models.CharField(max_length=250, verbose_name="Описание", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    changed_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения", null=True, blank=True)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.name}"




