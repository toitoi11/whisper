# Generated by Django 4.2.7 on 2023-12-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0010_script_delete_audiofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="EngScript",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name="Script",
            new_name="KorScript",
        ),
    ]
