from django.db import models
from django.contrib.auth.models import User


class IHA(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Marka")
    model_name = models.CharField(max_length=100, verbose_name="Model")
    cruising_speed = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Seyir Hızı (mach)", null=True, blank=True)
    max_speed = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Maksimum Hız (mach)", null=True, blank=True)
    flight_duration = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Uçuş Süresi (saat)", null=True, blank=True)
    max_payload_capacity = models.DecimalField(max_digits=7, decimal_places=2,
                                               verbose_name="Maksimum Yük Kapasitesi (kilogram)", null=True, blank=True)
    operational_altitude = models.CharField(max_length=100, verbose_name="Operasyonel İrtifa (feet)", null=True, blank=True)
    iha_type = models.CharField(max_length=50, choices=[
        ("military", "askeri"),
        ("drone", "drone"),
        ("space", "uzay"),
        ("commercial", "ticari"),
        ("education", "eğitim")], verbose_name="İHA Türü", null=True, blank=True),
    production_date = models.DateField(verbose_name="Üretim Tarihi", null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ("active", "Aktif"),
        ("rented", "Kiralandı"),
    ], default="active", verbose_name="Durum", null=True, blank=True)
    slug = models.CharField(max_length=250, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"


class IHAUser(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE, verbose_name="Kiralanan İHA")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kiralayan Üye")
    rental_date_start = models.DateField(verbose_name="Kiralama Tarihi Başlangıç")
    rental_date_end = models.DateField(verbose_name="Kiralama Tarihi Bitiş")


class UserActions(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    iha = models.ForeignKey(IHA, on_delete=models.DO_NOTHING, null=True)
    action_type = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)


