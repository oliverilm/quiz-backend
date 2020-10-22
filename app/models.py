from django.db import models

# Create your models here.

class Quiz(models.Model):

    name = models.CharField(max_length=255)
    show = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_value = models.TextField()

    def __str__(self):
        return self.quiz.name + " - " + self.question_value 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class AnswerOption(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    correct = models.BooleanField()

    def __str__(self):
        return self.value + " - " + str(self.correct)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'AnswerOption'
        verbose_name_plural = 'AnswerOptions'


class QuestionAnswered(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'QuestionAnswered'
        verbose_name_plural = 'QuestionAnswereds'