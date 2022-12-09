from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets


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


class HelloViewSet(viewsets.ViewSet):
    """test API ViewSet"""
    class_srz = serializers.HelloSrz

    def list(self, request):
        """return a hello msg and its methode is get"""
        x = [
            'viewsets not use for complex functions',
            'for simple api you can use viewset '
        ]

        return Response({"msg": "some msg", "viewset": x})

    def create(self, request):
        """this function roles POST methode function"""
        srz = self.class_srz(data=request.data)
        if srz.is_valid():
            name = srz.validated_data.get('name')
            msg = f'hello {name}'
            return Response({"msg": msg})
        else:
            return Response(
                srz.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, requests, pk=None):
        return Response({"methode": "get"})

    def update(self, request, pk=None):
        return Response({"methode": "put"})

    def partial_update(self, request, pk=None):
        return Response({"methode": "patch"})

    def destroy(self, request, pk=None):
        return Response({"methode": "delete"})
