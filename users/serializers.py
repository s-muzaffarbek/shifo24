from .models import Admin, CustomUser, Doctor
from rest_framework import serializers

class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['username', 'phone', 'password', 'workplace']

    def create(self, validated_data):
        user = Admin(
            username=validated_data["username"],
            password=validated_data["password"],
            phone=validated_data["phone"],
        )
        password = validated_data["password"]
        user.user.set_password(password)
        user.save()
        return user
class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'