from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello this is the index of Mechino!')

def user_login(request):
    return HttpResponse('Hello this is the user login')

def user_home(request):
    return HttpResponse('Hello this is the user home')

