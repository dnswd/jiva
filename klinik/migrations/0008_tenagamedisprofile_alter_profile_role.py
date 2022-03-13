# Generated by Django 4.0.3 on 2022-03-09 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("klinik", "0007_stafprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="TenagaMedisProfile",
            fields=[
                (
                    "profile_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="klinik.profile",
                    ),
                ),
            ],
            bases=("klinik.profile",),
        ),
        migrations.AlterField(
            model_name="profile",
            name="role",
            field=models.CharField(
                choices=[
                    ("owner", "Owner"),
                    ("staf", "Staf"),
                    ("tenaga_medis", "Tenaga Medis"),
                ],
                max_length=30,
            ),
        ),
    ]
