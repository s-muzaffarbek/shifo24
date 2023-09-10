from rest_framework import serializers

from .models import Doctor, WorkPlace, Specialty


class DoctorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url if obj.image else None
        return request.build_absolute_uri(image_url) if image_url else None

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
