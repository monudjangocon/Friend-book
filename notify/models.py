from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape

class Notify(models.Model):
 
    NOTIFY_TYPES = (
        ('FAVORITE', 'Favorite'),
        ('LIKE', 'Like'),
        
        )

    user = models.ForeignKey(User)
    notify_type = models.CharField(max_length=1, choices=NOTIFY_TYPES)
    feed = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
  

 

    def __unicode__(self):
        return self.notify_type

class Notification(models.Model):

  
    NOTIFICATION_TYPES = (
        ('LIKED', 'Liked'),
        ('COMMENTED', 'Commented'),
      
        )
        
        
    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name="+")
    date = models.DateTimeField(auto_now_add=True)
    feed = models.ForeignKey('feeds.Feed', null=True, blank=True)
    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)

    liked= u'<a href="/{0}/">{1}</a> liked your post: <a href="/feeds/{2}/">{3}</a>'
    comment= u'<a href="/{0}/">{1}</a> commented on your post: <a href="/feeds/{2}/">{3}</a>'
   
    

    def __unicode__(self):
        if self.notification_type == self.LIKED:
            return self.liked.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.feed.pk,
                escape(self.item(self.feed.post))
                )
        elif self.notification_type == self.COMMENTED:
            return self.comment.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.feed.pk,
                escape(self.item(self.feed.post))
                )
         else:
            return 'Ooops! Something went wrong. ckeck it'

    def item(self, value):
        temp= 50
        if len(value) > temp:
            return u'{0}...'.format(value[:temp])
        else:
            return value
