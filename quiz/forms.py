from django import forms

from .models import Question, Answer

class AnswerForm(forms.Form):
    """
    Manages the answer of single questions
    """

    answer = forms.ModelChoiceField(queryset=Answer.objects.none())
