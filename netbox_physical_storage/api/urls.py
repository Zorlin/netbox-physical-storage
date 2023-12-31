from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_physical_storage'

router = NetBoxRouter()
router.register('storage-devices', views.StorageDeviceViewSet)

urlpatterns = router.urls