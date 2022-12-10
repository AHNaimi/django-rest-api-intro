from .models import UserModel
from rest_framework import serializers


class HelloSrz(serializers.Serializer):
    name = serializers.CharField(max_length=40)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

        def create(self, validated_data):
            user = UserModel.objects.create_user(
                email=validated_data["email"],
                name=validated_data['name'],
                password=validated_data['password']
            )
            return user
