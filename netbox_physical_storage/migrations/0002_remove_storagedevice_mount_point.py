# Generated by Django 4.2.8 on 2023-12-31 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_physical_storage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storagedevice',
            name='mount_point',
        ),
    ]
