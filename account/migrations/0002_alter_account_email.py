# Generated by Django 4.0.3 on 2022-03-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "Email ini sudah digunakan"},
                max_length=254,
                unique=True,
            ),
        ),
    ]
