# Generated by Django 4.0.3 on 2022-03-06 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("klinik", "0004_merge_0003_alter_klinik_owner_0003_klinik_sik"),
    ]

    operations = [
        migrations.AlterField(
            model_name="klinik",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="klinik.ownerprofile"
            ),
        ),
    ]
