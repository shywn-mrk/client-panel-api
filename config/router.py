from rest_framework import routers
from clients.api.viewsets import ClientViewSet
from user_settings.api.viewsets import SettingsViewSet

router = routers.DefaultRouter()

router.register('clients', ClientViewSet, basename='clients')
router.register('settings', SettingsViewSet, basename='settings')
