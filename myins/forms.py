from django import forms

from .models import Daily,Todo_Trophy,Wish, Inspiration,Reference,Trophy

class DailyForm(forms.ModelForm):

    class Meta:
        model = Daily
        fields = ('title','text')

class Todo_TrophyForm(forms.ModelForm):

    class Meta:
        model = Todo_Trophy
        fields = ('title','text','duedate','success')

class WishForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ('title','text')

class InspirationForm(forms.ModelForm):

    class Meta:
        model = Inspiration
        fields = ('title','text')

class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ('title','text')

class TrophyForm(forms.ModelForm):

    class Meta:
        model = Trophy
        fields = ('title','text')
