from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth import authenticate, login
from prof.forms import SignUpForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)## user has been added to the current session
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'signup.html', {'form': SignUpForm()})

def Cover(request):
    return render_to_response("cover.html",{})
