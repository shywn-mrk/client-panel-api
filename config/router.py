from rest_framework import routers
from clients.api.viewsets import ClientViewSet

router = routers.DefaultRouter()

router.register('clients', ClientViewSet, basename='clients')
