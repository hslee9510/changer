from django import forms

from .models import Daily,Todo

class DailyForm(forms.ModelForm):

    class Meta:
        model = Daily
        fields = ('title','text')

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title','text','duedate')
