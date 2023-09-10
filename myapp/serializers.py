from rest_framework import serializers

from .models import Doctor, WorkPlace, Specialty

class DoctorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url


class WorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = '__all__'

class SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialty
        fields = '__all__'



