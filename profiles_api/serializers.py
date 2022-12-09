
from rest_framework import serializers


class HelloSrz(serializers.Serializer):
    name = serializers.CharField(max_length=40)


