from netbox.views.generic import ObjectChangeLogView
from django.urls import path
from . import models, views

urlpatterns = (
    path('bays/', views.StorageBayListView.as_view(), name='storagebay_list'),
    path('bays/add/', views.StorageBayEditView.as_view(), name='storagebay_add'),
    path('bays/<int:pk>/', views.StorageBayView.as_view(), name='storagebay'),
    path('bays/<int:pk>/edit/', views.StorageBayEditView.as_view(), name='storagebay_edit'),
    path('bays/<int:pk>/delete/', views.StorageBayDeleteView.as_view(), name='storagebay_delete'),
    path('bays/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagebay_changelog', kwargs={
        'model': models.StorageBay
    }),
    path('devices/', views.StorageDeviceListView.as_view(), name='storagedevice_list'),
    # path('devices/associate/', views.StorageDeviceAssociateView.as_view(), name='storagedevice_associate'),
    path('devices/add/', views.StorageDeviceEditView.as_view(), name='storagedevice_add'),
    path('devices/<int:pk>/', views.StorageDeviceView.as_view(), name='storagedevice'),
    path('devices/<int:pk>/edit/', views.StorageDeviceEditView.as_view(), name='storagedevice_edit'),
    path('devices/<int:pk>/delete/', views.StorageDeviceDeleteView.as_view(), name='storagedevice_delete'),
    path('devices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagedevice_changelog', kwargs={
        'model': models.StorageDevice
    }),
    path('manufacturers/', views.StorageManufacturerListView.as_view(), name='storagemanufacturer_list'),
    path('manufacturers/add/', views.StorageManufacturerEditView.as_view(), name='storagemanufacturer_add'),
    path('manufacturers/<int:pk>/', views.StorageManufacturerView.as_view(), name='storagemanufacturer'),
    path('manufacturers/<int:pk>/edit/', views.StorageManufacturerEditView.as_view(), name='storagemanufacturer_edit'),
    path('manufacturers/<int:pk>/delete/', views.StorageManufacturerDeleteView.as_view(), name='storagemanufacturer_delete'),
    path('manufacturers/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagemanufacturer_changelog', kwargs={
        'model': models.StorageManufacturer
    }),
    path('device-types/', views.StorageDeviceTypeListView.as_view(), name='storagedevicetype_list'),
    path('device-types/add/', views.StorageDeviceTypeEditView.as_view(), name='storagedevicetype_add'),
    path('device-types/<int:pk>/', views.StorageDeviceTypeView.as_view(), name='storagedevicetype'),
    path('device-types/<int:pk>/edit/', views.StorageDeviceTypeEditView.as_view(), name='storagedevicetype_edit'),
    path('device-types/<int:pk>/delete/', views.StorageDeviceTypeDeleteView.as_view(), name='storagedevicetype_delete'),
    path('device-types/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagedevicetype_changelog', kwargs={
        'model': models.StorageDeviceType
    })
)