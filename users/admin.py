from django.contrib import admin
from .models import CustomUser, Admin, Doctor, User

admin.site.register(User)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'is_active')
#     # list_display_links = ('first_name', 'last_name')
#     # search_fields = ('first_name', 'specialties')

admin.site.register(Doctor)
admin.site.register(CustomUser)
admin.site.register(Admin)
