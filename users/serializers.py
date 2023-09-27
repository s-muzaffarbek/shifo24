from .models import AdminUser
from rest_framework import serializers

from rest_framework import serializers
from .models import AdminUser

class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['username', 'phone', 'password', 'workplace']

    def create(self, validated_data):
        user = AdminUser(
            username=validated_data["username"],
            password=validated_data["password"],
            phone=validated_data["phone"],
        )
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user
class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'
