# Generated by Django 4.0.3 on 2022-04-18 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klinik', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=20, unique=True)),
                ('full_name', models.TextField(verbose_name='Nama Lengkap')),
            ],
        ),
        migrations.CreateModel(
            name='RekamanMedis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.JSONField(default=list, verbose_name='Fields')),
                ('time_created', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klinik.tenagamedisprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rekammedis.pasien')),
            ],
        ),
    ]
