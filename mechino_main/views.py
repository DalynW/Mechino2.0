from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home page of the website
def index(request):
    return render(request, 'mechino/index.html')

# User login page
def user_login(request):
    return render(request, 'mechino/login.html')

# User home page for after the log in.
# This will also contain a list of their vehicles and have the option to add or remove vehicles
def user_home(request):
    return render(request, 'mechino/userHome.html')

# User creation for new accounts
def user_signup(request):
    return render(request, 'mechino/signup.html')

# User info editing
# change phone-number and/or email
def user_edit(request):
    return render(request, 'mechino/userEdit.html')

# User vehicle view
# Better view of their vehicles
def vehicle_view(request):
    return render(request, 'mechino/vehicleView.html')

# Add vehicle page for entering vehicle details DALYN WAS HERE!!!!!
def user_add_vehicle(request):
    return render(request, 'mechino/vehicleAdd.html')

#edit a vehicle
def user_edit_vehicle(request):
    return render(request, 'mechino/vehicleEdit.html')

