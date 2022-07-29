from django.urls import path
from . import views




urlpatterns = [

path('registration',views.signup,name='signup'),
path('log',views.logup,name='logup'),




]