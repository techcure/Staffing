
from django.shortcuts import  render, redirect
from .forms import *
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django import template
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def index(request):
    return render(request, "Rec/index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}

    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))



@login_required

def new_question(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        form = QueForm(request.POST, request.FILES)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # messages= "Saved"
            messages.success(request, 'Your question has saved Successfully!.')
        return render(request, 'Rec/index.html', {'form': form})
    else:
            form = QueForm()
    # import pdb; pdb.set_trace()
    queryset = Question.objects.all()
    #my_total = Question.objects.count()
    context = {'data':queryset, 'form':form}
    return render(request, 'layouts/add-questions.html', context)

@login_required

def question_view(request):
    queryset = Question.objects.filter(id = 7)
    context = {'data':queryset}
    #context["data"] = queryset
    # import pdb;pdb.set_trace()
    fom = QueForm()
    return render(request, "layouts/view-question.html", context)