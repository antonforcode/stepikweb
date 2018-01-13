from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        if "script" in title and "script" in text:
            raise forms.ValidationError('Incorrect text')

    def save(self):
        self.cleaned_data['author_id'] = '1'
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        text = self.cleaned_data['text']
        if "script" in text:
            raise forms.ValidationError('Incorrect text')

    def save(self):
        self.cleaned_data['author_id'] = '1'
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
