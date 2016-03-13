from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape

class Notify(models.Model):
 
    NOTIFY_TYPES = (
        
        ('LIKE', 'Like'),
        ('FAVORITE', 'Favorite'),
        )

    user = models.ForeignKey(User)
    notify_type = models.CharField(max_length=1, choices=NOTIFY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    feed = models.IntegerField(null=True, blank=True)

 

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

    _LIKED_TEMPLATE = u'<a href="/{0}/">{1}</a> liked your post: <a href="/feeds/{2}/">{3}</a>'
    _COMMENTED_TEMPLATE = u'<a href="/{0}/">{1}</a> commented on your post: <a href="/feeds/{2}/">{3}</a>'
   
    

    def __unicode__(self):
        if self.notification_type == self.LIKED:
            return self._LIKED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.feed.pk,
                escape(self.get_summary(self.feed.post))
                )
        elif self.notification_type == self.COMMENTED:
            return self._COMMENTED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.feed.pk,
                escape(self.get_summary(self.feed.post))
                )
      
       
        
        
        else:
            return 'Ooops! Something went wrong.'

    def get_summary(self, value):
        summary_size = 50
        if len(value) > summary_size:
            return u'{0}...'.format(value[:summary_size])
        else:
            return value
