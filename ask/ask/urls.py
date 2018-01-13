"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'(^$|^login/|^signup/|^question/|^ask/|^popular/|^new/)', include('qa.urls')),
]
"""

from django.conf.urls import include, url
from qa import views

urlpatterns = [
    url(r'^$', views.main_view, name='main_view'),
    url(r'^popular/$', views.popular_view, name='popular_view'),
    url(r'^question/(?P<q_number>\d+)/', views.question_view, name='question_view'),
    url(r'^ask/$', views.ask_view, name='ask_view'),
]

