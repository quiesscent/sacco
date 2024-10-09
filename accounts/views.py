from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser, MemberProfile, MemberDependent, Contributions, OverallContribution
from .modules import generate_unique_membership_number
from .forms import MemberProfileForm
from django.contrib.auth.decorators import user_passes_test



def admin_check(user):
    return user.is_superuser

# Create your views here.
def chart_data(request):
    contributions = OverallContribution.objects.latest('id')
    data = {
            'funeral_kitty': contributions.funeral_kitty,
            'monthly_contributions':contributions.monthly_contributions,
            'expenditure': contributions.expenditure,
            'savings': contributions.savings,
    }
    return JsonResponse(data)

def index(request):
    if request.user.is_superuser:
        members = CustomUser.objects.all()
        contributions = OverallContribution.objects.latest('id')

        context = {
            "members": members,
            'funeral_kitty': contributions.funeral_kitty,
            'monthly_contributions':contributions.monthly_contributions,
            'expenditure': contributions.expenditure,
            'savings': contributions.savings,
        }
        chart = chart_data(request)

    else:
        user = request.user.id
        contributions = Contributions.objects.filter(user=user)
        dependants = MemberDependent.objects.filter(user=user)

        context = {
            'dependents': dependants,
            'contributions': contributions,
        }

    return render(request, 'home.html', context)

def login_(request):
    if request.method == 'POST':
        username = request.POST['username']  # Could be email or ID number
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page or other
        else:
            # Invalid login error
            return JsonResponse({'error': 'Invalid credentials'})
            # return render(request, 'login.html', {'error': 'Invalid credentials'})

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
            messages.error(request, 'Passwords do not match')
        else:
            user = CustomUser.objects.create_user(
                            username=username,
                            id_number=idNo,
                            email=email,
                            password=password2,
                            member_no=membership_no,
                )
            user.save()
            messages.success(request, 'Member Registration Success !! Login for Member Activation')
            return redirect('register')

    return render(request, 'register.html')

# @user_passes_test(admin_check)
def update_profile(request):
    user_profile = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = MemberProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('update')  # Redirect to same profile page

    else:
        form = MemberProfileForm(instance=user_profile)
        dependents = MemberDependent.objects.filter(user=user_profile.user)
        context = {
                'dependents': dependents,
                'form': form
            }
    return render(request, 'update.html')

def add_dependant(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    if request.method == 'POST' and request.FILES.get('proof_file'):
        name = request.POST['name']
        relationship = request.POST['relationship']
        proof_file = request.FILES['proof_file']
        dependent = MemberDependent(user=user, name=name, relationship=relationship, proof=proof_file)
        dependent.save()
        messages.success(request, 'Dependent Added Successfully')
        return redirect('update')


def logout_(request):

    logout(request)
    return redirect('home')
