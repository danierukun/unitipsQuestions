from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Answer

from .forms import AnswerForm

# Create your views here.


def general_question_view(request):
    """
    Lists all questions currently stored in the database
    """
    questions = Question.objects.all()
    return render(
        request,
        'quiz/question_view.html',
        {'questions': questions}
    )


def single_question_view(request, question_id):
    """
    Displays a single question with its answers
    """
    if request.method == 'POST':
        print(request.POST)
        form = AnswerForm(request.POST)
        form.fields['answer'].queryset = Answer.objects.filter(question__id=question_id)
        if form.is_valid():
            is_correct = form.cleaned_data['answer'].is_correct
        else:
            return HttpResponse(status_code=400)
            
        return render(request, 'quiz/answer.html', {'is_correct': is_correct})
    else:
        form = AnswerForm()
        form.fields['answer'].queryset = Answer.objects.filter(question__id=question_id)
        form.fields['answer'].label = Question.objects.get(id=question_id).text

    return render(request, 'quiz/single_question.html', {'form': form})
