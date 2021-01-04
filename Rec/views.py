
from django.shortcuts import  render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import logout as auth_logout

from django.contrib import messages 

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Rec:index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Rec/dashboard.html", context={"login_form":form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("Rec:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render (request=request, template_name="Rec/register.html", context={"register_form":form})


def login_view(request):

    return redirect("Rec:index")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("Rec:index")


def question_view(request):
    form2 = QuestionForm()

    if request.method == "POST":
        form2 = QuestionForm(request.POST)
        
        if form2.is_valid():
           form2.save()
           messages.success(request, "QuestionForm Saved!" )
           form2 = QuestionForm
    return render (request=request, template_name="Rec/ques.html", context={"ques_form":form2})
