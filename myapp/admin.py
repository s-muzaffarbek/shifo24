from django.contrib import admin
from .models import Doctor, WorkPlace, Specialty
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', )
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'specialties')


admin.site.register(WorkPlace)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialty)
