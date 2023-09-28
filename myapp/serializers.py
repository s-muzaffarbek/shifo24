from rest_framework import serializers

from .models import WorkPlace, Specialty
from users.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    workplace = serializers.SerializerMethodField()
    specialties = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url if obj.image else None
        return request.build_absolute_uri(image_url) if image_url else None

    def get_workplace(self, obj):
        workplaces = obj.workplace.all()
        serialized_workplaces = [
            {
                "name": wp.name,
                "lat": wp.latitude,
                "lot": wp.longitude,
                "id": wp.id
            }
            for wp in workplaces
        ]
        return serialized_workplaces

    def get_specialties(self, obj):
        specialties = obj.specialties.all()

        serialized_specialties = [
            {
                "name": sp.name,
                "id": sp.id
            }
            for sp in specialties
        ]
        return serialized_specialties
    class Meta:
        model = Doctor
        fields = '__all__'


class WorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = '__all__'


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
