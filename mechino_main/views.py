from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home page of the website
def index(request):
    return HttpResponse('Hello this is the index of Mechino!')

# User login page
def user_login(request):
    return HttpResponse('Hello this is the user login')

# User home page for after the log in.
# This will also contain a list of their vehicles and have the option to add or remove vehicles
def user_home(request):
    return HttpResponse('Hello this is the user home')

# User creation for new accounts
def user_signup(request):
    return HttpResponse('User Creation')

# User info editing
# change phone-number and/or email
def user_edit(request):
    return HttpResponse('User Editing')

# Add vehicle page for entering vehicle details DALYN WAS HERE!!!!!
def user_add_vehicle(request):
    return HttpResponse('User add vehicle')

