from django.urls import path, include
from rest_framework.routers import SimpleRouter

from myapp.views import DoctorViewSet, WorkPlaceViewSet, SpecialtyViewSet

router = SimpleRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'workplase', WorkPlaceViewSet, basename='workplace')
router.register(r'specialty', SpecialtyViewSet, basename='specialty')

urlpatterns = [
    path('', include(router.urls)),
]
