from django.db import models
from django.contrib.auth.models import User


class IHA(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Marka")
    model_name = models.CharField(max_length=100, verbose_name="Model")
    cruising_speed = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Seyir Hızı (mach)")
    max_speed = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Maksimum Hız (mach)")
    flight_duration = models.DurationField(verbose_name="Uçuş Süresi")
    max_payload_capacity = models.DecimalField(max_digits=5, decimal_places=2,
                                               verbose_name="Maksimum Yük Kapasitesi (kilogram)")
    operational_altitude = models.CharField(max_length=100, verbose_name="Operasyonel İrtifa")
    iha_type = models.CharField(max_length=50, verbose_name="İHA Türü")
    production_date = models.DateField(verbose_name="Üretim Tarihi")
    status = models.CharField(max_length=20, choices=[
        ("active", "Aktif"),
        ("rented", "Bakımda"),
    ], default="active", verbose_name="Durum")

    def __str__(self):
        return f"{self.brand} {self.model_name} - Seri No: {self.serial_number}"


class IHAUser(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE, verbose_name="Kiralanan İHA")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kiralayan Üye")
    rental_date_start = models.DateField(verbose_name="Kiralama Tarihi Başlangıç")
    rental_date_end = models.DateField(verbose_name="Kiralama Tarihi Bitiş")



