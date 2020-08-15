from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

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
                user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()     
               
        else:
             messages.info(request, 'Password doesnt match')   
             return redirect('registeration')
        return redirect('/login')     
        


    else:
        return render(request, 'registeration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('success')
        else:
            messages.info(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    return redirect('login') 


def success(request):
    return render(request, 'success.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('registeration')

def home(request):
    return render(request, 'home.html')




