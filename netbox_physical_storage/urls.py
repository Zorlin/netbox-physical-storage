from netbox.views.generic import ObjectChangeLogView
from django.urls import path
from . import models, views

urlpatterns = (
    path('physical-storage/bays/', views.StorageBayListView.as_view(), name='storagebay_list'),
    path('physical-storage/bays/add/', views.StorageBayEditView.as_view(), name='storagebay_add'),
    path('physical-storage/bays/<int:pk>/', views.StorageBayView.as_view(), name='storagebay'),
    path('physical-storage/bays/<int:pk>/edit/', views.StorageBayEditView.as_view(), name='storagebay_edit'),
    path('physical-storage/bays/<int:pk>/delete/', views.StorageBayDeleteView.as_view(), name='storagebay_delete'),
    path('physical-storage/bays/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagebay_changelog', kwargs={
        'model': models.StorageBay
    }),
    path('physical-storage/', views.StorageDeviceListView.as_view(), name='storagedevice_list'),
    path('physical-storage/add/', views.StorageDeviceEditView.as_view(), name='storagedevice_add'),
    path('physical-storage/<int:pk>/', views.StorageDeviceView.as_view(), name='storagedevice'),
    path('physical-storage/<int:pk>/edit/', views.StorageDeviceEditView.as_view(), name='storagedevice_edit'),
    path('physical-storage/<int:pk>/delete/', views.StorageDeviceDeleteView.as_view(), name='storagedevice_delete'),
    path('physical-storage/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagedevice_changelog', kwargs={
        'model': models.StorageDevice
    })
)