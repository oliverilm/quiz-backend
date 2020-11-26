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


class QuestionInSessionSerializer(serializers.ModelSerializer):
    answer_correct = serializers.SerializerMethodField()
    answer_value = serializers.SerializerMethodField()

    class Meta:
        model = QuestionAnswerInSession
        fields = "__all__"

    def get_answer_correct(self, obj):
        return obj.answer.correct

    def get_answer_value(self, obj):
        return obj.answer.value


class SessionSerializer(serializers.ModelSerializer):

    questions_answered = serializers.SerializerMethodField()
    quiz_name = serializers.SerializerMethodField()
    total_questions = serializers.SerializerMethodField()

    class Meta:
        model = QuizSession
        fields = "__all__"

    def get_questions_answered(self, obj):
        return QuestionInSessionSerializer(QuestionAnswerInSession.objects.filter(session_id=obj.pk), many=True).data

    def get_quiz_name(self, obj):
        return obj.quiz.name

    def get_total_questions(self, obj):
        return len(Question.objects.filter(quiz=obj.quiz))
