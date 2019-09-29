from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def welcome(request):
    s='<h1>Welcome to the Django class....!Django is python framework<h1>'
    return HttpResponse(s)
def dateinfo(request):
    date=datetime.datetime.now()
    msg='<h1>Good Morning whats the today date and time<h1><hr>'
    msg=msg+'<h1>date is:'+str(date)+'</h1>'
    return HttpResponse(msg)
