
from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.home , name = 'notice'),
    path('write/', views.write , name = 'write'),
    path('signup/' , views.signup , name = 'signup'),
    path('login/' , views.login , name = 'login'),
    path('logout/' , views.logout , name = 'logout'),
    path('update/<int:pk>' , views.update , name = 'update' )
]
