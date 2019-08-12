from django import forms
from .models import feedback, Comment
from django.forms import ModelForm, Textarea


class contactForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name','email', 'subject', 'message']
        widgets = {
            'message': Textarea(attrs={'cols':80, 'rows':4})
        }

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content':''}
        widgets = {
            'content': Textarea(attrs={'cols':80, 'rows':3, 'placeholder':'Text goes here'})
        }

