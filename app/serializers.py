from rest_framework import serializers
from .models import *

class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = "__all__"

    def get_questions(self, obj):
        return QuestionSerializer(Question.objects.filter(quiz=obj), many=True).data


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self, obj):
        return AnswerSerializer(AnswerOption.objects.filter(question=obj), many=True).data


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerOption
        fields = "__all__"



class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = "__all__"