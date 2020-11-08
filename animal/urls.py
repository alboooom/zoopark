from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet, PlacelViewSet, WorkerViewSet, KindViewSet, ConnectionViewSet
router = DefaultRouter()
router.register(r'place', PlacelViewSet)
router.register(r'animals', AnimalViewSet)
router.register(r'worker', WorkerViewSet)
router.register(r'kind', KindViewSet)
router.register(r'connection', ConnectionViewSet)

urlpatterns = [
    url(r'', include(router.urls)),

]