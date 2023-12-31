# Generated by Django 4.2.5 on 2023-09-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iha", "0006_alter_iha_brand_alter_iha_model_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="iha",
            name="brand",
            field=models.CharField(default=1, max_length=100, verbose_name="Marka"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="iha",
            name="cruising_speed",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Seyir Hızı (mach)",
            ),
        ),
        migrations.AlterField(
            model_name="iha",
            name="flight_duration",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Uçuş Süresi (saat)",
            ),
        ),
        migrations.AlterField(
            model_name="iha",
            name="max_payload_capacity",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=7,
                null=True,
                verbose_name="Maksimum Yük Kapasitesi (kilogram)",
            ),
        ),
        migrations.AlterField(
            model_name="iha",
            name="max_speed",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Maksimum Hız (mach)",
            ),
        ),
        migrations.AlterField(
            model_name="iha",
            name="model_name",
            field=models.CharField(default="a", max_length=100, verbose_name="Model"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="iha",
            name="operational_altitude",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="Operasyonel İrtifa (feet)",
            ),
        ),
        migrations.AlterField(
            model_name="iha",
            name="production_date",
            field=models.DateField(blank=True, null=True, verbose_name="Üretim Tarihi"),
        ),
        migrations.AlterField(
            model_name="iha",
            name="slug",
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="iha",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("active", "Aktif"), ("rented", "Kiralandı")],
                default="active",
                max_length=20,
                null=True,
                verbose_name="Durum",
            ),
        ),
    ]
