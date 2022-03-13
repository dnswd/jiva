# Generated by Django 4.0.3 on 2022-03-11 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klinik', '0008_tenagamedisprofile_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenagamedisprofile',
            name='cabang',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tenaga_medis', to='klinik.cabang'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenagamedisprofile',
            name='sip',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
