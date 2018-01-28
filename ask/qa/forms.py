from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        text = self.cleaned_data.get('text')
        if not text:
            raise forms.ValidationError('Need text')
        if "script" in text:
            raise forms.ValidationError('Incorrect text')

    def save(self):
        # self.cleaned_data['author_id'] = '1'
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        text = self.cleaned_data.get('text')
        if not text:
            raise forms.ValidationError('Need text')
        if "script" in text:
            raise forms.ValidationError('Incorrect text')


    def save(self):
        # self.cleaned_data['author_id'] = '1'
        self.cleaned_data['question_id'] = self.cleaned_data['question']
        del self.cleaned_data['question']
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Enter another username')
        return username

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Invalid username or password')
