
from modeltranslation.translator import TranslationOptions, translator
from .models import Specialty, WorkPlace, Doctor

class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name',)
class WorkPlaceTranslationOptions(TranslationOptions):
    fields = ('name',)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'work_experience')

translator.register(Specialty, SpecialtyTranslationOptions)
translator.register(WorkPlace, WorkPlaceTranslationOptions)
translator.register(Doctor, DoctorTranslationOptions)