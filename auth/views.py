from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from auth.forms import SignUpForm, SingInForm
from profiles.models import Profile


def sign_in(request):
    if request.method == 'POST':
        form = SingInForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('posts:index')
        else:
            form._errors = "Please enter a correct username and password"
    else:
        form = SingInForm()
    return render(request, 'auth/sign_in.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('posts:index')
    else:
        form = SignUpForm()
    return render(request, 'auth/sign_up.html', {'form': form})


def sign_out(request):

    if request.method == 'POST':
        logout(request)
        return redirect('posts:index')
