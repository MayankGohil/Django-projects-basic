from django.shortcuts import render
from form_app import forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'form_app/index.html')

def form_fun(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid:
            print("VALIDATION SUCCESS!")
            print("NAME : "+form.cleaned_data['name'])
            print("EMAIL : "+form.cleaned_data['email'])
            print("TEXT : "+form.cleaned_data['text'])

    return render(request, 'form_app/form_page.html', {'form':form})
