from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

def registeration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phoneno = request.POST.get('phoneno')
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('registeration')
           
            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'email is already taken')
                 return redirect('registeration')
               
        else:
             messages.info(request, 'Password doesnt match')   
             return redirect('registeration')
        return redirect('login')     
        


    else:
        return render(request, 'registeration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('page1')
        else:
            messages.info(request, 'invalid credentials')   
            return redirect('login') 
    
        


    else:
        return render(request, 'login.html')    

def success(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.success(request, user)
            return redirect('page1')
        else:
            messages.info(request, 'invalid credentials')   
            return redirect('success') 
    
        


    else:
        return render(request, 'success.html')       
           






