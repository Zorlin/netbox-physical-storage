from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from django import forms
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

    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_physical_storage:storagemanufacturer', args=[self.pk])

class StorageDeviceType(NetBoxModel):
    name = models.CharField(
        max_length=100
    )

    manufacturer = models.ForeignKey(
        to='StorageManufacturer',
        on_delete=models.PROTECT
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

    # TODO: Protocol might not be the best name here, we may consider switching this to "technology" or something similar later.
    protocol_choices = [
        ('SATA', 'SATA'),
        ('NVMe', 'NVMe'),
        ('SAS', 'SAS'),
    ]

    protocol = models.CharField(
        max_length=50,
        choices=protocol_choices,
        default='SATA'
    )

    model_number = models.CharField(
        max_length=100
    )
    
    part_number = models.CharField(
        max_length=100,
        blank=True,
    )

    # Stored in bytes so we can represent GiB, TiB, etc.
    size = models.BigIntegerField(
        validators=[MinValueValidator(0)]
    )

    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_physical_storage:storagedevicetype', args=[self.pk])


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

class StorageDevice(NetBoxModel):
    name = models.CharField(
        max_length=100
    )

    storage_device_model = models.ForeignKey(
        to='StorageDeviceType',
        null=True,
        on_delete=models.PROTECT
    )

    serial_number = models.CharField(
        max_length=100,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )

    # We can optionally associate a particular storage device with a storage bay
    storage_bay = models.ForeignKey(
        to='StorageBay',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    @property
    def protocol(self):
        if self.storage_device_model:
            # Access the associated protocol through the model relationship
            return self.storage_device_model.protocol
        else:
            return None

    @property
    def form_factor(self):
        if self.storage_device_model:
            # Access the associated device through the model relationship
            return self.storage_device_model.form_factor
        else:
            return None

    @property
    def device(self):
        # Check if a storage_bay is associated with this StorageDevice
        if self.storage_bay:
            # Access the associated device through the storage_bay relationship
            return self.storage_bay.device
        else:
            return None

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_physical_storage:storagedevice', args=[self.pk])
