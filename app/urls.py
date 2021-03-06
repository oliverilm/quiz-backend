"""quizmaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("quiz-list-create", QuizListView.as_view()),
    path("quiz-detail/<int:pk>", QuizView.as_view()),
    path("delete-quiz", HideQuizView.as_view()),
    path("add-answer", AddAnswerOptionToQuiz.as_view()),
    path("add-stat", AddStat.as_view()),
    path("get-stats", GetStats.as_view()),
    path("get-stats/<int:pk>", GetStatsForQuiz.as_view()),
]
