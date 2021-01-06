from django import forms

from .models import *

class QueForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'subj', 'answer', 'easy', 'medium', 'hard')

        answer = forms.CharField(widget=forms.Textarea)
        easy = forms.BooleanField()
        medium = forms.BooleanField()
        hard = forms.BooleanField()