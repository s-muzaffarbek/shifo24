from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AdminUserView, AdminLoginView, AdminRegisterView, LogoutView, DoctorViewSet

router = SimpleRouter()
router.register(r'admin', AdminUserView, basename='admins')
router.register(r'doctor', DoctorViewSet, basename='doctors')
# router.register(r'user', CustomUserView, basename='users')

urlpatterns = [
    path('admin_register/', AdminRegisterView.as_view(), name='admin-register'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
