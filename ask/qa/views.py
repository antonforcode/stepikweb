"""
from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')
"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

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
