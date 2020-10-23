from django.contrib import admin
from .models import *

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(QuestionAnswered)
admin.site.register(QuizSession)
admin.site.register(QuestionAnswerInSession)

# Register your models here.
