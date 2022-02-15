from django import forms
from django.views.decorators.csrf import csrf_exempt

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
