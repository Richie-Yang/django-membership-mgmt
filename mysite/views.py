from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.


def homepage(request):
    # ηΎε¨ζι
    now = datetime.now()
    context = {'now': now}
    return render(request, 'homepage.html', context)
