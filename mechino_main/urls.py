from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('user/', views.user_home, name='user_home'),
    path('signup/', views.user_signup, name='user_signup'),
    path('user/edit/', views.user_edit, name='user_edit'),
    path('user/vehicles/', views.vehicle_view, name='vehicle_view'),
    path('user/vehicles/add/', views.user_add_vehicle, name='vehicle_add'),
    path('user/vehicles/edit/', views.user_edit_vehicle, name='vehicle_edit'),
]