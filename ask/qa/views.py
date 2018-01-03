"""
from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')
"""

from django.core.paginator import Paginator
from django.shortcuts import render

def main_view(request):
    
