# Generated by Django 4.0.2 on 2022-03-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klinik', '0002_alter_profile_account_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='klinik',
            name='sik',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
