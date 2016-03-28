from django.shortcuts import render_to_response
from notify.models import Notification
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from friend.decorators import ajax_required

## checking user login or not....
@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)
    not_read= Notification.objects.filter(to_user=user, is_read=False)
    for notification in not_read:
        notification.is_read = True
        notification.save()        
    return render_to_respone('notification.html', {'notifications': notifications})

@login_required
@ajax_required
def last_notifications(request):
    user = request.user## logged in user
    notifications = Notification.objects.filter(to_user=user, is_read=False)[:5] ## we 're fetching ist five user 
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return render_to_response('last_notifications.html', {'notifications': notifications})

@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user, is_read=False)[:5]
    return HttpResponse(len(notifications))
