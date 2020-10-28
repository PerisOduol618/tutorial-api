from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tutorial
from .serializer import TutorialSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.

class TutorialList(APIView):
    def get(self, request, format=None):
        all_tutorial = Tutorial.objects.all()
        serializers = TutorialSerializer(all_tutorial,many =True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)


    def post(self,request,formart=None):
        serializers = TutorialSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



