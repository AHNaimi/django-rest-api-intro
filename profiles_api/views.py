from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


class HelloApiView(APIView):

    def get(self, request):
        first = [
            "hello"
            "bye"
        ]
        return Response({"first": first, "second": "this is just a sentence"})

    def post(self, request):
        srz_class = serializers.HelloSrz(data=request.data)
        if srz_class.is_valid():
            name = srz_class.validated_data.get('name')
            msg = f"hello {name}"
            return Response({"msg": msg})
        else:
            return Response(
                srz_class.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({"methode": "put"})

    def depatch(self, request, pk=None):
        return Response({"methode": "dispatch"})

    def delete(self, request, pk=None):
        return Response({"methode": "delete"})
