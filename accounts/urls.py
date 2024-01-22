from django.urls import path, include

from . import views


app_name = 'accounts'
urlpatterns = [
    #setup up default django urls
    path('', include('django.contrib.auth.urls')),
    #user registration 
    path('register/', views.register, name='register'), 
]