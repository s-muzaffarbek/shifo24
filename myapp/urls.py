from django.urls import path, include
from rest_framework.routers import SimpleRouter

from myapp.views import doctor_list, doctor_detail, WorkPlaceViewSet, SpecialtyViewSet

router = SimpleRouter()
router.register(r'workplase', WorkPlaceViewSet, basename='workplace')
router.register(r'specialty', SpecialtyViewSet, basename='specialty')

urlpatterns = [
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/<int:id>/', doctor_detail, name='doctor_detail'),
    path('', include(router.urls)),
]
