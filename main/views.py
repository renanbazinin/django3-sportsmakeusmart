from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import MindGames, MindGameswins
import random

# Create your views here.
def main(request):
    if User is not None:
        UserName = request.user.username
        lastscore = MindGameswins.objects.filter(title = UserName).order_by('wons')[:3]
        lastscore = lastscore
    
    games = MindGames.objects.all()
    x = games[0].textlist
    x = x.split()
    list1 =[]
    for i in range(1,12):
        list1.append(x[random.randint(1,999)])

    return render(request, 'main/home.html', {'games' : list1 , 'lastscore' : lastscore })  

def about(request):
    return render(request, 'main/about.html')

def signin(request):
    


    games = MindGames.objects.all()

    if request.method == 'GET':
        return render(request, 'main/signin.html', {'games' : games })     
    elif 'register' in request.POST:  
        try:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'] )
            user.save()
            login(request,user)
            return redirect('main')
        except IntegrityError:
            return render(request, 'main/signin.html', {'error':'Username or password wrong'} )      
        return render(request, 'main/home.html')
    elif 'login' in request.POST:
        user = authenticate(request, username = request.POST['username1'], password = request.POST['password3'] )
        if user is None:
            return render(request, 'main/signin.html', {'error':'User or password wrong '} )   
        login(request,user)   
        return redirect('main')

        #return render(request, 'main/signin.html', {'error': 'something was wrong '} )      

#def read_file(request):
 #   f = open('path/text.txt', 'r')
  #  file_content = f.read()
   # f.close()
    #return render(file_content, content_type="text/plain")


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'main/home.html')

def sendscore(request):
    if request.method == "POST":
        MindGameswinsScore = MindGameswins.objects.create(title = str(request.POST['usernamewon']),wons=request.POST['sendresult'])
        return redirect('main')


