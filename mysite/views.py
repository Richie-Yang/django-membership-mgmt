from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.


def homepage(request):
    # 現在時間
    now = datetime.now()
    context = {'now': now}
    return render(request, 'homepage.html', context)
