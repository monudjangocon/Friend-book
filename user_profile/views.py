from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib import messages
from PIL import Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings as django_settings
from feed.models import Feed
from feed.views import feeds

from user_profile.forms import ProfileForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
import os

@login_required
def profile(request, username):
    user=request.user
    page_user = get_object_or_404(User, username=username)
    all_feeds = Feed.get_feeds().filter(user=page_user)
    paginator = Paginator(all_feeds,8)
    feeds = paginator.page(1)
    from_feed = -1
    if feeds:
        from_feed = feeds[0].id
    return render(request, 'profile.html', {
        'page_user': page_user,
        'feeds': feeds,
        'from_feed': from_feed,
        'page': 1,
        'user':user
        })

@login_required
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been  successfully edited.')
    else:
        form = ProfileForm(instance=user, initial={
            'location': user.profile.location
            })
    return render_to_response('setting.html', {'form':form})

@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True
    except Exception, e:
        pass
    return render_to_response('picture.html', {'uploaded_picture': uploaded_picture})

@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your password has been  successfully changed....')
    else:
        form = ChangePasswordForm(instance=user)
    return render_to_response('password.html', {'form':form})



def log_out(request):
    user=request.user
    return render_to_response('core/logout.html',{'user':user})
