# Generated by Django 4.2.7 on 2023-11-22 04:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_uploadfilemodel"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UploadFileModel",
        ),
    ]
