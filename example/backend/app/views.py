from django.shortcuts import render
from .models import Notice
from django.contrib.auth.models import User
def home(request):
    #if request.method == "POST":
    return render(request , 'notice.html')

def write(request):
    if request.method == 'POST':
        t = request.POST['title']
        b = request.POST['board']
        i = request.FILE['image']
        u= request.user.username
        Notice.objects.create(title = c , body = b , userName = u , image = i)
        return redirect('/')
    else :
        return render(request , 'write.html')