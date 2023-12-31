from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class StorageDeviceTypeChoices(ChoiceSet):
    key = 'StorageDevice.type'

    CHOICES = [
        ('SAS', 'SAS', 'blue'),
        ('SATA', 'SATA', 'indigo'),
        ('NVMe', 'NVMe', 'purple'),
    ]

class StorageDevice(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    storage_device_type = models.CharField(
        max_length=100,
        choices=StorageDeviceTypeChoices
    )
    serial_number = models.CharField(
        max_length=100,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_physical_storage:storagedevice', args=[self.pk])
    
    def get_storage_device_type_color(self):
        return StorageDeviceTypeChoices.colors.get(self.storage_device_type)
