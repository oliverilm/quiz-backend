from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *


class QuizListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Quiz.objects.filter(show=True).order_by("-pk")
    serializer_class = QuizListSerializer


class QuizView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        selectedQuiz = Quiz.objects.get(pk=self.kwargs.get("pk"))
        return Response(QuizSerializer(selectedQuiz).data)

    # def post(self, request, *args, **kwargs):
    #     # add question to the quiz


class HideQuizView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            pk = request.data.get("id")
            quiz = Quiz.objects.get(pk=pk)
            quiz.show = False
            quiz.save()

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "error": str(e)})


class AddAnswerOptionToQuiz(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            quizId = request.data.get("quizId")
            question = request.data.get("value")
            answers = request.data.get("answers")
            quizObj = Quiz.objects.get(pk=request.data.get("quizId"))

            questionObj = Question(
                quiz=quizObj,
                question_value=request.data.get("value")
            )
            questionObj.save()

            for answer in request.data.get("answers"):
                AnswerOption(
                    question=questionObj,
                    value=answer.get("value"),
                    correct=answer.get("correct")
                ).save()

            return Response({"status": "OK", "quiz": QuizSerializer(quizObj).data})
        except Exception as e:
            return Response({"status": "error", "error": str(e)})
        pass


class AddStat(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data.get("quizId")
        quiz = Quiz.objects.get(pk=data)
        session = QuizSession(
            quiz=quiz
        )
        session.save()

        session.save()
        qArr = []
        for qa in request.data.get("answers"):
            questionsAnswered = QuestionAnswerInSession(
                session=session,
                answer=AnswerOption.objects.get(pk=qa["id"])
            )
            questionsAnswered.save()
        return Response({"status": "OK", "session": SessionSerializer(session).data})

    def get(self, request, *args, **kwargs):
        return Response({"status", "ok"})


class GetStats(generics.ListAPIView):
    queryset = QuizSession.objects.all()
    serializer_class = SessionSerializer


class GetStatsForQuiz(generics.ListAPIView):
    queryset = QuizSession.objects.all()
    serializer_class = SessionSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return QuizSession.objects.filter(pk=self.kwargs.get("pk"))
