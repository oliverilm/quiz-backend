from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import *
from .serializers import *

# Create your views here.


class QuizListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizListSerializer


class QuizView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        selectedQuiz = Quiz.objects.get(pk=self.kwargs.get("pk"))
        
        return Response( QuizSerializer(selectedQuiz).data)

    # def post(self, request, *args, **kwargs):
    #     # add question to the quiz

