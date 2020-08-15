from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate
from users.models import UserProfile
from django.http import HttpResponse

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            try:
                user = User.objects.get(username=username)
            except user.DoesNotExist:
                return username
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def page1(request):
    
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST['lname']
        ph_no = request.POST['phno']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']

        try:
            user = User.objects.get(username=email)
            return HttpResponse('<h2>User exists</h2>')
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, password=password)
            user.save()
        profile = UserProfile(f_name=f_name, l_name=l_name, ph_no=ph_no, email=email, gender=gender, user=user)
        profile.save()

        return redirect('page1')
    else:
        return render(request, 'page1.html')


def page2(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            profile = UserProfile.objects.get(email=email)
            return render(request, 'Page3.html', {'profile': profile, 'message': 'Found user!'})
        except UserProfile.DoesNotExist:
            return render(request, 'Page3.html', {'message': 'Sorry no user with the entered email found'})

    else:
        return render(request, 'Page2.html')

def page3(request):
    return render(request, 'page3.html')
        