from typing import ContextManager
from django.shortcuts import render , redirect , get_object_or_404
from .models import Notice
from django.contrib.auth.models import User 
from django.contrib import auth

def signup(request):
    if request.method == 'POST' :
        id = request.POST["username"]
        pw = request.POST["password"]
        User.objects.create_user(username = id , password = pw)
        return redirect('/')
    else :
        return render(request , 'signup.html')

def login(request):
    if request.method == 'POST' :
       id = request.POST["username"]
       pw = request.POST["password"]
       user = auth.authenticate(request , username = id , password = pw)

       if user is None :
           return render(request , "login.html")
       else :
           auth.login(request, user)
           return redirect("/")
    else :
        user = request.user
        if str(user) == "AnonymousUser" :
            return render(request , 'login.html')
        else :
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')    

def home(request):
    #if request.method == "POST":
    contents = Notice.objects.filter()
    return render(request , 'notice.html' , { 'contents' : contents })

def write(request):
    if request.method == 'POST':
        t = request.POST['title']
        b = request.POST['board']
        i = request.FILES['images']
        u = request.user.username
        Notice.objects.create(title = t , body = b , userName = u , images = i)
        return redirect('/')
    else :
        return render(request , 'write.html')

def update(request , pk):
    contents = get_object_or_404(Notice , pk = pk)
    if request.method == 'POST' :
       contents.title = request.POST['title']
       contents.body = request.POST['board']
       contents.images = request.FILES['images']
       contents.save()
       return redirect('/')
    else :
        return render(request , 'update.html' , { "contents" : contents})   