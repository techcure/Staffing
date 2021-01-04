

# Create your forms here.


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
