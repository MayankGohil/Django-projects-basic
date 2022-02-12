from django.shortcuts import render
from Apptwo.models import User
from Apptwo.forms import NewUserForm

def users(request):
    
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit='TRUE')
            return index(request)
        else:
            print("Error Data invalid")
    
    return render(request, 'Protwo/User.html', {'form':form} )


    

def index(request):
    return render(request, 'Protwo/index.html')
