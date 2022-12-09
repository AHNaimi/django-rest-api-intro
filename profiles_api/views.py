from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request):
        first = [
            "hello"
            "bye"
        ]
        return Response({"first": first, "second": "this is just a sentence"})
