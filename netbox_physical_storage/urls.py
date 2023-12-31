from netbox.views.generic import ObjectChangeLogView
from django.urls import path
from . import models, views

urlpatterns = (
    path('physical-storage/', views.StorageDeviceListView.as_view(), name='storagedevice_list'),
    path('physical-storage/add/', views.StorageDeviceEditView.as_view(), name='storagedevice_add'),
    path('physical-storage/<int:pk>/', views.StorageDeviceView.as_view(), name='storagedevice'),
    path('physical-storage/<int:pk>/edit/', views.StorageDeviceEditView.as_view(), name='storagedevice_edit'),
    path('physical-storage/<int:pk>/delete/', views.StorageDeviceDeleteView.as_view(), name='storagedevice_delete'),
    path('physical-storage/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagedevice_changelog', kwargs={
        'model': models.StorageDevice
    })
)