from django.shortcuts import render
from django.http import HttpResponse   # added
from .models import Intern_other


# Create your views here.

def home(request):
    return render(request, 'home.html')

def main(request):
    title = 'Main Page'
    intern_list = Intern_other.objects.all()
    context = {'title': title,
	               'intern_list': intern_list}
    return render(request,'InternShip/main.html',context )

def user_info(request):
    return render(request, 'internship/user_info.html')
