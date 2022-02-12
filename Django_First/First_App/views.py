from django.shortcuts import render
from First_App.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):

    webpage_list = AccessRecord.objects.order_by('date')
    date_dic = { 'access_records' : webpage_list }
    return render(request, 'Django_First/index.html', context = date_dic)

def help(request):
    help_dic = { 'help_me' : "HELP PAGE!" }
    return render(request, 'Django_First/help.html', context = help_dic)
