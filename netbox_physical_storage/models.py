from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class StorageManufacturer(NetBoxModel):
    name = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class StorageBay(NetBoxModel):
    device = models.ForeignKey(
        to='dcim.Device',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    name = models.CharField(
        max_length=100
    )

    form_factor_choices = [
        ('sff', 'Small Form Factor (SFF)'),
        ('lff', 'Large Form Factor (LFF)'),
        ('m2', 'M.2'),
        ('u2', 'U.2'),
        ('u3', 'U.3'),
        ('msata', 'mSATA'),
        ('expansion', 'Expansion Card'),
        ('nf1', 'NF1/NGSFF'),
        ('edsff', 'EDSFF'),
    ]

    form_factor = models.CharField(
        max_length=50,
        choices=form_factor_choices,
        default='lff'
    )

    # Whether the bay supports hot swapping of components
    hot_swap_capability = models.BooleanField(
        default=True,
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
        return reverse('plugins:netbox_physical_storage:storagebay', args=[self.pk])

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
