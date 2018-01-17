from django import forms
from .models import Question, Answer


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
        self.cleaned_data['author_id'] = '1'
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
        self.cleaned_data['author_id'] = '1'
        self.cleaned_data['question_id'] = self.cleaned_data['question']
        del self.cleaned_data['question']
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
