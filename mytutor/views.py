from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
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



class TutoriaDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_tutorial(self,pk):
        try:
            return Tutorial.objects.get(pk=pk)
        except Tutorial.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        tutorial = self.get_tutorial(pk)
        serializer =  TutorialSerializer(tutorial)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        tutorial = self.get_tutorial(pk)
        serializer =  TutorialSerializer(tutorial,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        