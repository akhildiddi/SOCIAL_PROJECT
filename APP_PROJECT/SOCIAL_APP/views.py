from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or wherever you want
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required
from .models import UserActivity

@login_required
def account(request):
    user_activities = UserActivity.objects.filter(user=request.user)
    return render(request, 'account.html', {'user_activities': user_activities})

@login_required
def submit_activity(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        UserActivity.objects.create(user=request.user, content=content)
    return redirect('account')