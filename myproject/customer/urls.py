from django.urls import path
from . import views




urlpatterns = [

path('registration',views.signup,name='signup'),
path('log',views.logup,name='logup'),
path('display',views.display_form,name='display_form'),
path('editt',views.edit,name='edit'),




]