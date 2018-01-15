"""
from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')
"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.http import HttpResponseRedirect
from .forms import AskForm

def main_view(request):
    page_number = request.GET.get('page', 1)
    new_questions = Question.objects.new()
    paginator = Paginator(new_questions, 10)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/main_view.html', {'questions' : page.object_list})

def popular_view(request):
    page_number = request.GET.get('page', 1)
    popular_questions = Question.objects.popular()
    paginator = Paginator(popular_questions, 10)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/main_view.html', {'questions' : page.object_list})

def question_view(request, q_number):
    question = get_object_or_404(Question, pk=q_number)
    answers = question.answer_set.all()
    return render(request, 'qa/question_view.html', {'question' : question, 'answers' : answers})

def ask_view(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect("/question/{}/".format(question.id))
    else:
        form = AskForm()
    return render(request, 'qa/ask_view.html', {'form': form})
