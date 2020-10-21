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
    queryset = Quiz.objects.filter(show=True)
    serializer_class = QuizListSerializer


class QuizView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        selectedQuiz = Quiz.objects.get(pk=self.kwargs.get("pk"))
        return Response( QuizSerializer(selectedQuiz).data)
    
    # def post(self, request, *args, **kwargs):
    #     # add question to the quiz

class HideQuizView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            pk = request.data.get("id")
            quiz= Quiz.objects.get(pk=pk)
            quiz.show = False
            quiz.save()

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "error": str(e)})


class AddAnswerOptionToQuiz(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        quiz = Quiz.objects.get(pk=request.data.get("quizId"))
        question = Question(
            quiz=quiz,
            question_value=request.data.get("question")
        ).save()
        for answer in request.data.get("answers"):
            AnswerOption(
                question=question,
                value=answer.get("value"),
                correct=answer.get("correct")
            ).save()
        # quizId
        # Question String
        # array of answers [{answer value, boolean if correct}]
        return Response({"status": "OK"})
        pass