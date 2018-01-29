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
from .forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login


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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            author_id = request.user.id
            answer = form.save(author_id)
            return HttpResponseRedirect("/question/{}/".format(q_number))
    else:
        form = AnswerForm(initial={'question' : q_number})
    return render(request, 'qa/question_view.html', {'question' : question, 'answers' : answers, 'form': form})


def ask_view(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            author_id = request.user.id
            question = form.save(author_id)
            return HttpResponseRedirect("/question/{}/".format(question.id))
    else:
        form = AskForm()
    return render(request, 'qa/ask_view.html', {'form': form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignupForm()
    return render(request, 'qa/signup_view.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, 'qa/login_view.html', {'form': form})
