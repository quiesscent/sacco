from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser
from .modules import generate_unique_membership_number

def index(request):
	return render(request, 'index.html')

def login_(request):
    if request.method == 'POST':
        username = request.POST['username']  # Could be email or ID number
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or other
        else:
            # Invalid login error
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def register_(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        idNo = request.POST['idNo']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        membership_no = generate_unique_membership_number()

        if password2 != password1:
            # messages.error(request, 'Passwords do not match')
            print('Passwords do not match')
        else:
            user = CustomUser.objects.create_user(
                            username=username,
                            id_number=idNo,
                            email=email,
                            password=password2,
                            membership_no=membership_no,
                        )
            user.save()
            messages.success(request, 'Member Registration Success !! Login for Member Activation')
            return redirect('home')

    return render(request, 'register.html')