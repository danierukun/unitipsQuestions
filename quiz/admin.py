from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Question, Answer

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print(request.POST)
        question_id = request.POST['question']

        if Answer.objects.filter(question__id=question_id).count() >= 4:
            return

        if "True" in Answer.objects.filter(question__id=question_id).values_list('is_correct',flat=True):
            return
        obj.save()
