# Generated by Django 4.0.3 on 2022-04-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwalpasien',
            name='jadwalTenagaMedis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jadwal_pasien', to='jadwal.jadwaltenagamedis'),
        ),
    ]
