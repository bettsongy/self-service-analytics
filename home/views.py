from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(requset):
    # return HttpResponse('Hello world!')
    return render(requset, 'home/welcome.html', {'today' : datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/restricted.html', {})

