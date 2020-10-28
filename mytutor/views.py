from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tutorial
from .serializer import TutorialSerializer
# Create your views here.

class TutorialList(APIView):
    def get(self, request, format=None):
        all_tutorial = Tutorial.objects.all()
        serializers = TutorialSerializer(all_tutorial,many =True)
        return Response(serializers.data)