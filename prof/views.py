from django.shortcuts import render_to_response
from prof.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.template import RequestContext

def signup(request):
    ## here post request.....
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render_to_response('signup.html', {'form': form},context_instance=RequestContext(request))
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)## user has been added to the current session
            login(request, user)
            return HttpResponseRedirect('/')
    ## get request......        
    else:
        form=SignUpForm()
        return render_to_response( 'signup.html', {'form':form},context_instance=RequestContext(request))

def Cover(request):
    return render_to_response("cover.html",{},context_instance=RequestContext(request))
