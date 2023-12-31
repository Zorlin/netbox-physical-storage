from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models

class StorageDeviceType(NetBoxObjectType):

    class Meta:
        model = models.StorageDevice
        fields = '__all__'

class Query(ObjectType):
    storage_device = ObjectField(StorageDeviceType)
    storage_device_list = ObjectListField(StorageDeviceType)

schema = Query
